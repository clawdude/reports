#!/usr/bin/env python3
"""Generate a static GitHub Pages-compatible report index.

Expected report layout for new reports:
  reports/YYYY/MM/<slug>/index.html

The builder also lists legacy root-level HTML reports so old files are not lost.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import argparse
import html
import re

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
REPORTS_DIR = SCRIPT_DIR
INDEX_FILE = ROOT / "index.html"
TITLE_RE = re.compile(rb"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
DATE_RE = re.compile(r"(20\d{2})[-/](\d{2})[-/](\d{2})")


@dataclass(frozen=True)
class Report:
    title: str
    href: str
    path: Path
    mtime: float
    size: int
    date_hint: str | None


def title_from_file(path: Path) -> str:
    try:
        head = path.read_bytes()[:65536]
        match = TITLE_RE.search(head)
        if match:
            raw = re.sub(rb"\s+", b" ", match.group(1)).strip()
            return html.unescape(raw.decode("utf-8", errors="replace"))
    except OSError:
        pass
    stem = path.parent.name if path.name == "index.html" else path.stem
    return stem.replace("-", " ").replace("_", " ").title()


def date_hint(path: Path) -> str | None:
    rel = path.relative_to(ROOT).as_posix()
    match = DATE_RE.search(rel)
    if match:
        y, m, d = match.groups()
        return f"{y}-{m}-{d}"

    parts = path.relative_to(ROOT).parts
    for i in range(len(parts) - 2):
        if re.fullmatch(r"20\d{2}", parts[i]) and re.fullmatch(r"\d{2}", parts[i + 1]):
            return f"{parts[i]}-{parts[i + 1]}"
    return None


def discover_reports(root: Path) -> list[Report]:
    candidates: list[Path] = []

    if REPORTS_DIR.exists():
        candidates.extend(
            p for p in REPORTS_DIR.rglob("*.html")
            if p.is_file() and not p.name.startswith(".")
        )

    # Legacy support: include old flat reports in the site root, but not the generated index.
    candidates.extend(
        p for p in root.glob("*.html")
        if p.is_file() and p.name.lower() != "index.html"
    )

    reports: list[Report] = []
    seen: set[Path] = set()
    for path in candidates:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        stat = path.stat()
        href = path.relative_to(root).as_posix()
        reports.append(
            Report(
                title=title_from_file(path),
                href=href,
                path=path,
                mtime=stat.st_mtime,
                size=stat.st_size,
                date_hint=date_hint(path),
            )
        )

    return sorted(reports, key=lambda r: (r.date_hint or "", r.mtime), reverse=True)


def render_index(reports: list[Report], root: Path) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    if reports:
        rows = []
        for r in reports:
            modified = datetime.fromtimestamp(r.mtime).strftime("%Y-%m-%d %H:%M")
            size = f"{r.size / 1024:.1f} KB"
            date = r.date_hint or modified.split(" ", 1)[0]
            rows.append(
                "<li>"
                f"<a href=\"{html.escape(r.href, quote=True)}\">"
                f"{html.escape(r.title)}"
                f"<small>{html.escape(r.href)}</small>"
                "</a>"
                f"<span>{html.escape(date)}</span>"
                f"<span>{html.escape(size)}</span>"
                "</li>"
            )
        body = "\n".join(rows)
    else:
        body = '<li class="empty">No HTML reports found yet.</li>'

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Reports</title>
  <style>
    :root {{ color-scheme: dark; --bg:#0b1020; --panel:#111831; --text:#e8eefc; --muted:#aab6d3; --line:#2a355d; --blue:#79c0ff; }}
    body {{ margin:0; background:linear-gradient(180deg,#080c18,#0b1020 240px); font:16px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif; color:var(--text); }}
    main {{ max-width:960px; margin:0 auto; padding:40px 20px; }}
    h1 {{ font-size:clamp(2rem,5vw,3.5rem); letter-spacing:-.04em; margin:0 0 8px; }}
    p {{ color:var(--muted); margin:0 0 24px; }}
    code {{ color:#d8e2ff; }}
    ul {{ list-style:none; padding:0; margin:0; background:var(--panel); border:1px solid var(--line); border-radius:18px; overflow:hidden; }}
    li {{ display:grid; grid-template-columns:1fr auto auto; gap:16px; align-items:center; padding:14px 16px; border-bottom:1px solid var(--line); }}
    li:last-child {{ border-bottom:0; }}
    a {{ color:var(--blue); text-decoration:none; font-weight:650; }}
    a:hover {{ text-decoration:underline; }}
    small {{ display:block; margin-top:2px; color:var(--muted); font-weight:400; overflow-wrap:anywhere; }}
    span {{ color:var(--muted); font-size:.92rem; white-space:nowrap; }}
    .empty {{ display:block; color:var(--muted); }}
    footer {{ color:var(--muted); margin-top:18px; font-size:.9rem; }}
    @media(max-width:640px) {{ li {{ grid-template-columns:1fr; gap:4px; }} span {{ white-space:normal; }} }}
  </style>
</head>
<body>
  <main>
    <h1>Reports</h1>
    <p>Static index generated from <code>reports/</code>. Add a report, run <code>python3 build_index.py</code>, publish to GitHub Pages.</p>
    <ul>{body}</ul>
    <footer>Last built: {html.escape(now)} · {len(reports)} report{'s' if len(reports) != 1 else ''}</footer>
  </main>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate static reports index.html")
    parser.add_argument("--root", type=Path, default=ROOT, help="reports site root")
    args = parser.parse_args()

    root = args.root.expanduser().resolve()
    reports = discover_reports(root)
    output = render_index(reports, root)
    (root / "index.html").write_text(output, encoding="utf-8")
    print(f"Wrote {root / 'index.html'} with {len(reports)} reports")


if __name__ == "__main__":
    main()
