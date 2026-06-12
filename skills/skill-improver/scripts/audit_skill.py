#!/usr/bin/env python3
"""Deterministic structural audit for a Claude skill.

Checks the mechanically verifiable quality criteria so human/model judgment
can be spent on the qualitative ones. Advisory: WARN findings are prompts
for judgment, not automatic defects.

Usage:
    python audit_skill.py <path-to-skill-directory>
    python audit_skill.py <path-to-skill-directory> --json

Exit codes: 0 = no ERROR-level findings, 1 = at least one ERROR, 2 = usage error.
Stdlib-only. Non-interactive. Output: human-readable report to stdout
(or JSON with --json); diagnostics to stderr.
"""

import argparse
import ast
import json
import re
import sys
from pathlib import Path

STDLIB_HINT = {
    "os", "sys", "re", "json", "csv", "math", "pathlib", "argparse", "subprocess",
    "shutil", "itertools", "functools", "collections", "datetime", "time", "typing",
    "io", "tempfile", "glob", "zipfile", "textwrap", "string", "random", "logging",
    "urllib", "http", "hashlib", "base64", "unicodedata", "statistics", "dataclasses",
    "enum", "copy", "traceback", "abc", "contextlib", "uuid", "platform", "struct",
    "ast", "html", "fnmatch", "concurrent", "select", "webbrowser", "socket",
    "signal", "threading", "multiprocessing", "queue", "warnings", "inspect",
    "pickle", "sqlite3", "xml", "email", "mimetypes", "configparser", "getpass",
    "difflib", "filecmp", "stat", "errno", "operator", "heapq", "bisect", "array",
}

findings = []


def add(severity, code, message, location=None):
    findings.append({
        "severity": severity, "code": code, "message": message,
        "location": str(location) if location else None,
    })


def parse_frontmatter(text):
    """Minimal YAML frontmatter parser (top-level key: value only)."""
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return None
    fm = {}
    current_key = None
    for line in m.group(1).splitlines():
        if re.match(r"^\S[^:]*:", line):
            key, _, value = line.partition(":")
            current_key = key.strip()
            fm[current_key] = value.strip()
        elif current_key and line.startswith((" ", "\t")):
            fm[current_key] = (fm[current_key] + " " + line.strip()).strip()
    return fm


def check_frontmatter(skill_dir, text):
    fm = parse_frontmatter(text)
    if fm is None:
        add("ERROR", "FM01", "SKILL.md has no parseable YAML frontmatter (--- block at top)")
        return {}
    name = fm.get("name", "")
    desc = fm.get("description", "")
    if not name:
        add("ERROR", "FM02", "Frontmatter missing required 'name' field")
    if not desc:
        add("ERROR", "FM03", "Frontmatter missing required 'description' field")
        return fm
    if name and name != skill_dir.name:
        add("WARN", "FM04",
            f"Frontmatter name '{name}' != directory name '{skill_dir.name}'; "
            "different surfaces derive the invocation name from different places — align them")
    if name and not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        add("WARN", "FM05", f"Name '{name}' is not lowercase-hyphenated")
    if name in {"helper", "utils", "tools", "assistant", "skill"}:
        add("WARN", "FM06", f"Name '{name}' is too vague to route on")

    # Description checks
    if len(desc) > 1024:
        add("ERROR", "DS01", f"Description is {len(desc)} chars (>1024; will be rejected/truncated on some surfaces)")
    elif len(desc) > 800:
        add("WARN", "DS02", f"Description is {len(desc)} chars; consider tightening (limit 1024)")
    first_sentence = re.split(r"(?<=[.!?])\s", desc, maxsplit=1)[0]
    if len(first_sentence) > 250:
        add("WARN", "DS03",
            f"First sentence is {len(first_sentence)} chars; some surfaces truncate aggressively — "
            "make the first sentence self-sufficient")
    if len(desc) < 60:
        add("WARN", "DS04", f"Description is only {len(desc)} chars; likely too thin to route reliably")
    if not re.search(r"\buse (this skill )?when(ever)?\b|\buse when\b|\buse for\b|\buse this (skill )?if\b|\btrigger\b", desc, re.IGNORECASE):
        add("WARN", "DS05", "Description has no explicit 'use when...' trigger guidance")
    if not re.search(r"\bdo not use\b|\bnot for\b|\bdon't use\b|\bdo NOT\b", desc, re.IGNORECASE):
        add("INFO", "DS06",
            "Description states no negative scope ('Do not use for...'); "
            "fine for a lone skill, risky in a library of overlapping skills")
    if re.match(r"^\s*(I |My |This is me)", desc):
        add("WARN", "DS07", "Description appears to be first-person; write it in third person")
    raw = re.search(r"^description:\s*(.*)$", text.split("---")[1], re.MULTILINE)
    if raw and not raw.group(1).strip().startswith(('"', "'", "|", ">")) and ": " in raw.group(1):
        add("ERROR", "DS08",
            "Unquoted description contains ': ' which breaks YAML parsing — "
            "quote the value, use a block scalar, or replace the colon")
    return fm


def check_body(skill_dir, text):
    lines = text.splitlines()
    n = len(lines)
    if n > 500:
        add("WARN", "BD01", f"SKILL.md is {n} lines (>500); move branch-specific detail into references/")
    elif n > 800:
        add("ERROR", "BD01", f"SKILL.md is {n} lines (>800); this loads on every invocation")

    body = re.sub(r"\A---.*?\n---\s*\n", "", text, flags=re.DOTALL)
    caps = re.findall(r"\b(ALWAYS|NEVER|MUST)\b", body)
    if len(caps) >= 8:
        add("INFO", "BD02",
            f"{len(caps)} all-caps ALWAYS/NEVER/MUST in body; heavy command density is a yellow flag — "
            "check whether explaining the why would generalize better")

    if not re.search(r"^#{1,3}\s", body, re.MULTILINE):
        add("WARN", "BD03", "Body has no headings; likely an essay rather than a navigable workflow")

    # Internal reference checks: markdown links are real pointers (ERROR if broken);
    # backtick mentions may be illustrative examples (INFO if absent).
    md_links = re.findall(r"\[[^\]]*\]\(([^)#][^)]*)\)", body)
    tick_mentions = re.findall(r"`((?:references|scripts|assets)/[^`\s]+)`", body)
    referenced = set()
    for ref in md_links:
        if ref.startswith(("http://", "https://", "mailto:")):
            continue
        referenced.add(ref)
        if not (skill_dir / ref).exists():
            add("ERROR", "RF01", f"SKILL.md links to '{ref}' which does not exist")
        if ref.count("/") > 2:
            add("WARN", "RF02", f"Reference '{ref}' is nested deep; keep references one level down")
    for ref in tick_mentions:
        referenced.add(ref)
        if not (skill_dir / ref).exists():
            add("INFO", "RF05",
                f"SKILL.md mentions '{ref}' which does not exist — fine if illustrative, "
                "a problem if the model is expected to read/run it")

    # Orphan supporting files (never mentioned anywhere in SKILL.md text)
    for sub in ("references", "assets"):
        d = skill_dir / sub
        if d.is_dir():
            for f in d.rglob("*"):
                if f.is_file():
                    rel = f.relative_to(skill_dir).as_posix()
                    if rel not in body and f.name not in body:
                        add("WARN", "RF03",
                            f"'{rel}' is never mentioned in SKILL.md; it will never be loaded (dead weight)",
                            rel)

    # Large reference files without a TOC
    rdir = skill_dir / "references"
    if rdir.is_dir():
        for f in rdir.glob("*.md"):
            rl = f.read_text(encoding="utf-8", errors="replace").splitlines()
            if len(rl) > 300:
                head = "\n".join(rl[:40]).lower()
                if "contents" not in head and "table of contents" not in head:
                    add("INFO", "RF04", f"'{f.name}' is {len(rl)} lines with no table of contents", f.name)


def check_scripts(skill_dir):
    sdir = skill_dir / "scripts"
    if not sdir.is_dir():
        return
    for f in sorted(sdir.rglob("*.py")):
        rel = f.relative_to(skill_dir).as_posix()
        src = f.read_text(encoding="utf-8", errors="replace")
        calls_input = False
        try:
            tree = ast.parse(src)
            calls_input = any(
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == "input"
                for node in ast.walk(tree)
            )
        except SyntaxError:
            add("WARN", "SC00", f"'{rel}' is not valid Python (syntax error); could not analyze", rel)
        if calls_input:
            add("ERROR", "SC01",
                f"'{rel}' calls the interactive input() builtin; prompts hang agents — use args/flags", rel)
        if "argparse" not in src and "--help" not in src and "sys.argv" not in src and len(src.splitlines()) > 40:
            add("WARN", "SC02", f"'{rel}' has no CLI handling; agents read --help instead of source", rel)
        imports = set(re.findall(r"^\s*(?:import|from)\s+([A-Za-z_][A-Za-z0-9_]*)", src, re.MULTILINE))
        third_party = sorted(i for i in imports if i not in STDLIB_HINT and not (sdir / f"{i}.py").exists()
                             and not (sdir / i).is_dir() and i != "scripts")
        if third_party:
            add("INFO", "SC03",
                f"'{rel}' imports possibly non-stdlib modules: {', '.join(third_party)}. "
                "Fine if declared; remember the Claude API runtime has no network/package installs", rel)


def main():
    ap = argparse.ArgumentParser(
        description="Deterministic structural audit for a Claude skill directory.",
        epilog="Example: python audit_skill.py ./my-skill --json")
    ap.add_argument("skill_dir", help="Path to the skill directory (containing SKILL.md)")
    ap.add_argument("--json", action="store_true", help="Emit findings as JSON instead of a text report")
    args = ap.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    skill_md = skill_dir / "SKILL.md"
    if not skill_dir.is_dir():
        print(f"error: '{skill_dir}' is not a directory", file=sys.stderr)
        return 2
    if not skill_md.is_file():
        print(f"error: no SKILL.md found in '{skill_dir}'", file=sys.stderr)
        return 2

    text = skill_md.read_text(encoding="utf-8", errors="replace")
    check_frontmatter(skill_dir, text)
    check_body(skill_dir, text)
    check_scripts(skill_dir)

    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    findings.sort(key=lambda x: order[x["severity"]])

    if args.json:
        print(json.dumps({"skill": skill_dir.name, "findings": findings}, indent=2))
    else:
        print(f"Structural audit: {skill_dir.name}")
        print(f"{'-' * 40}")
        if not findings:
            print("No findings. Structure looks clean — proceed to the qualitative audit.")
        for f in findings:
            loc = f" [{f['location']}]" if f["location"] else ""
            print(f"{f['severity']:5} {f['code']}{loc}: {f['message']}")
        errs = sum(1 for f in findings if f["severity"] == "ERROR")
        warns = sum(1 for f in findings if f["severity"] == "WARN")
        print(f"{'-' * 40}")
        print(f"{errs} error(s), {warns} warning(s), "
              f"{len(findings) - errs - warns} info. "
              "Findings are advisory — apply judgment, then run the qualitative rubric.")
    return 1 if any(f["severity"] == "ERROR" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
