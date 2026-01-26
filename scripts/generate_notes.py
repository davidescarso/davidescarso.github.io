#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES_JSON = ROOT / "notes.json"
NOTES_HTML = ROOT / "notas.html"
NOTES_DIR = ROOT / "notes"

READ_MORE = {
    "pt": "Ler mais",
    "en": "Read more",
    "it": "Leggi",
}


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    return text or "note"


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def build_excerpt(text: str, limit: int = 320) -> str:
    if len(text) <= limit:
        return text
    cut = text[:limit]
    if " " in cut:
        cut = cut.rsplit(" ", 1)[0]
    return f"{cut}…"


def load_notes() -> list[dict]:
    return json.loads(NOTES_JSON.read_text(encoding="utf-8"))


def get_cache_bust() -> str:
    content = NOTES_HTML.read_text(encoding="utf-8")
    match = re.search(r"style\.css\?v=([^\"\s]+)", content)
    return match.group(1) if match else "1"


def render_meta(note: dict) -> str:
    parts: list[str] = []
    date_raw = note.get("date", "") or ""
    date = date_raw.split(" ")[0]
    lang = (note.get("lang") or "").upper()
    if date:
        parts.append(date)
    if lang:
        parts.append(f'<span class="lang-tag">{lang}</span>')
    source = note.get("source")
    if source:
        parts.append(source)
    return " · ".join(parts)


def render_note_list_item(note: dict) -> str:
    title = html.escape(note.get("title", "") or "")
    body_html = note.get("body_html", "") or ""
    meta_html = render_meta(note)
    lang = note.get("lang") or ""
    data_lang = f' data-lang="{html.escape(lang)}"' if lang else ""

    full_page = bool(note.get("full_page"))
    slug = note.get("slug") or slugify(f"{note.get('date','')} {note.get('title','')}")

    if full_page:
        plain = strip_html(body_html)
        excerpt = html.escape(build_excerpt(plain, 640))
        label = READ_MORE.get(lang, READ_MORE["en"])
        body = (
            f'<div class="post-body">'
            f'<p class="excerpt">{excerpt}</p>'
            f'<a class="read-more" href="notes/{slug}.html">{label}</a>'
            f"</div>"
        )
    else:
        body = f'<div class="post-body">{body_html}</div>'

    return (
        f'<article class="post-item"{data_lang}>'
        f'<h2>{title}</h2>'
        f'<p class="meta">{meta_html}</p>'
        f"{body}"
        f"</article>"
    )


def render_notes_list(notes: list[dict]) -> str:
    items: list[str] = []
    filtered = [n for n in notes if n.get("title") != "[TÍTULO]"]
    for idx, note in enumerate(filtered):
        items.append(render_note_list_item(note))
        if idx < len(filtered) - 1:
            items.append('<hr class="post-divider"/>')
    return "\n".join(items)


def render_note_page(note: dict, cache_bust: str) -> str:
    title = html.escape(note.get("title", "") or "")
    body_html = note.get("body_html", "") or ""
    meta_html = render_meta(note)
    lang = (note.get("lang") or "en").lower()

    return f"""<!DOCTYPE html>

<html lang=\"{lang}\">
<head>
<meta charset=\"utf-8\"/>
<meta content=\"width=device-width, initial-scale=1\" name=\"viewport\"/>
<title>{title} – Davide Scarso</title>
<link href=\"../assets/css/style.css?v={cache_bust}\" rel=\"stylesheet\"/>
</head>
<body class=\"page note loading\">
<header>
<div class=\"nav\">
<a class=\"brand\" href=\"../index.html\">Davide Scarso</a>
<nav>
<a data-i18n=\"nav_research\" href=\"../research.html\">Research</a>
<a data-i18n=\"nav_blog\" href=\"../notas.html\">Blog</a>
<a data-i18n=\"nav_about\" href=\"../about.html\">About</a>
<a data-i18n=\"nav_contact\" href=\"../contact.html\">Contact</a>
</nav>
<div aria-label=\"Language\" class=\"lang-toggle\" data-i18n-aria=\"lang_label\">
<button class=\"active\" data-lang=\"en\" type=\"button\">EN</button>
<button data-lang=\"pt\" type=\"button\">PT</button>
</div>
</div>
</header>
<main>
<div class=\"page-top\">
<a class=\"page-brand\" href=\"../index.html\">Davide Scarso</a>
<div class=\"page-top-inner\">
<div class=\"page-nav\">
<a data-i18n=\"nav_research\" href=\"../research.html\">Research</a>
<a class=\"active\" data-i18n=\"nav_blog\" href=\"../notas.html\">Blog</a>
<a data-i18n=\"nav_about\" href=\"../about.html\">About</a>
<a data-i18n=\"nav_contact\" href=\"../contact.html\">Contact</a>
</div>
<div aria-label=\"Language\" class=\"home-lang\" data-i18n-aria=\"lang_label\">
<button data-lang=\"pt\" type=\"button\">PT</button>
<button class=\"active\" data-lang=\"en\" type=\"button\">EN</button>
</div>
</div>
</div>
<article class=\"note-entry\" data-lang=\"{lang}\">
<h1 class=\"note-title\">{title}</h1>
<p class=\"meta\">{meta_html}</p>
<div class=\"post-body\">{body_html}</div>
</article>
</main>
<script src=\"../assets/js/main.js?v={cache_bust}\"></script>
</body>
</html>
"""


def write_note_pages(notes: list[dict], cache_bust: str) -> None:
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    for note in notes:
        if note.get("title") == "[TÍTULO]":
            continue
        if not note.get("full_page"):
            continue
        slug = note.get("slug") or slugify(f"{note.get('date','')} {note.get('title','')}")
        path = NOTES_DIR / f"{slug}.html"
        path.write_text(render_note_page(note, cache_bust), encoding="utf-8")


def update_notes_html(notes: list[dict], cache_bust: str) -> None:
    content = NOTES_HTML.read_text(encoding="utf-8")
    content = re.sub(r'<div id=\"notes\"[^>]*>', '<div id="notes" data-static="true">', content)
    rendered = render_notes_list(notes)
    content = re.sub(
        r"(<div id=\"notes\"[^>]*>)(.*?)(</div>)",
        lambda m: f"{m.group(1)}\n{rendered}\n{m.group(3)}",
        content,
        flags=re.DOTALL,
    )
    NOTES_HTML.write_text(content, encoding="utf-8")


def main() -> None:
    notes = load_notes()
    cache_bust = get_cache_bust()
    update_notes_html(notes, cache_bust)
    write_note_pages(notes, cache_bust)


if __name__ == "__main__":
    main()
