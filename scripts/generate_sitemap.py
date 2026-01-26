#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from datetime import datetime, UTC

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://davidescarso.github.io"

PAGES = [
    "index.html",
    "notas.html",
    "research.html",
    "about.html",
    "contact.html",
]


def iso_date(path: Path) -> str:
    ts = path.stat().st_mtime
    return datetime.fromtimestamp(ts, UTC).strftime("%Y-%m-%d")


def main() -> None:
    urls = []
    for page in PAGES:
        path = ROOT / page
        if path.exists():
            urls.append((f"{SITE_URL}/{page}", iso_date(path)))

    notes_dir = ROOT / "notes"
    if notes_dir.exists():
        for note in sorted(notes_dir.glob("*.html")):
            urls.append((f"{SITE_URL}/notes/{note.name}", iso_date(note)))

    lines = ["<?xml version=\"1.0\" encoding=\"UTF-8\"?>", "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">"]
    for loc, lastmod in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append("  </url>")
    lines.append("</urlset>")

    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
