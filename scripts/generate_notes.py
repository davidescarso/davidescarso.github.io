#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES_JSON = ROOT / "notes.json"
INDEX_HTML = ROOT / "index.html"
ARQUIVO_HTML = ROOT / "arquivo.html"
NOTES_HTML = ROOT / "notas.html"
CRONICAS_HTML = ROOT / "cronicas.html"
FEED_XML = ROOT / "feed.xml"
NOTES_DIR = ROOT / "notes"
SITE_URL = "https://davidescarso.github.io"
CACHE_BUST = "20260510a"
HOME_LIMIT = 20
FEED_LIMIT = 50

LABEL = {
    "cronica": {"pt": "— CRÓNICA", "it": "— CRONACA", "en": "— CHRONICLE"},
    "nota":    {"pt": "— NOTA",    "it": "— NOTA",    "en": "— NOTE"},
    "excerto": {"pt": "— EXCERTO", "it": "— ESTRATTO", "en": "— EXCERPT"},
}

CONTINUE = {"pt": "continuar a ler →", "it": "continuare a leggere →", "en": "continue reading →"}
BACK = {"pt": "← arquivo", "it": "← archivio", "en": "← archive"}

MONTHS = {
    "pt": ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
           "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"],
    "it": ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
           "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"],
    "en": ["january", "february", "march", "april", "may", "june",
           "july", "august", "september", "october", "november", "december"],
}


def slugify(text: str) -> str:
    text = (text or "").strip().lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    return text or "note"


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def format_date(date_str: str, lang: str) -> str:
    date_part = (date_str or "").split(" ")[0]
    try:
        y, m, d = date_part.split("-")
        months = MONTHS.get(lang, MONTHS["en"])
        return f"{int(d)} {months[int(m) - 1]} {y}"
    except (ValueError, IndexError):
        return date_part


def is_cronica(note: dict) -> bool:
    return note.get("category") == "cronica" or bool(note.get("full_page"))


def is_excerto(note: dict) -> bool:
    return note.get("category") == "excerto"


def kind_of(note: dict) -> str:
    if is_cronica(note):
        return "cronica"
    if is_excerto(note):
        return "excerto"
    return "nota"


def get_slug(note: dict) -> str:
    if note.get("slug"):
        return note["slug"]
    return slugify(f"{note.get('date', '')} {note.get('title', '')}")


def extract_intro(body_html: str) -> tuple[str, bool]:
    """Devolve (intro_html, foi_cortado).

    Se houver marcador <!--more-->, devolve tudo antes.
    Senão, corta em ~70 palavras na primeira frase completa após esse limite.
    """
    if not body_html:
        return "", False
    if "<!--more-->" in body_html:
        intro = body_html.split("<!--more-->", 1)[0]
        return intro.strip(), True
    plain = strip_html(body_html)
    words = plain.split()
    if len(words) <= 80:
        return body_html, False
    cut_after = " ".join(words[:70])
    pos = plain.find(cut_after)
    if pos < 0:
        return body_html, False
    tail = plain[pos + len(cut_after):]
    end = re.search(r"[.!?](\s|$)", tail)
    if not end:
        return body_html, False
    excerpt_plain = cut_after + tail[: end.end()]
    return f"<p>{html.escape(excerpt_plain)}</p>", True


URL_AS_TEXT_RE = re.compile(
    r'<a([^>]*?)href="(https?://[^"]+)"([^>]*?)>\s*\2\s*</a>',
    re.IGNORECASE,
)


def beautify_url_links(body: str) -> str:
    """Quando <a href='URL'>URL</a>, troca o texto por 'Link ↗'."""
    return URL_AS_TEXT_RE.sub(r'<a\1href="\2"\3>Link ↗</a>', body)


def get_image_size(path: Path) -> tuple[int, int] | None:
    """Devolve (w, h) para PNG/WebP. None se não detectável."""
    if not path.exists():
        return None
    import struct
    data = path.read_bytes()[:32]
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        w = struct.unpack(">I", data[16:20])[0]
        h = struct.unpack(">I", data[20:24])[0]
        return w, h
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        chunk = data[12:16]
        if chunk == b"VP8L":
            n = struct.unpack("<I", data[21:25])[0]
            return ((n & 0x3FFF) + 1, ((n >> 14) & 0x3FFF) + 1)
        if chunk == b"VP8 ":
            w = struct.unpack("<H", data[26:28])[0] & 0x3FFF
            h = struct.unpack("<H", data[28:30])[0] & 0x3FFF
            return w, h
        if chunk == b"VP8X":
            w = (data[24] | data[25] << 8 | data[26] << 16) + 1
            h = (data[27] | data[28] << 8 | data[29] << 16) + 1
            return w, h
    return None


def auto_class_figure(body: str) -> str:
    """Adiciona class='figure-wide' a figures com imagens panorâmicas (W/H > 1.3)."""
    def repl(m: re.Match) -> str:
        attrs, inner = m.group(1), m.group(2)
        src_match = re.search(r'src="([^"]+)"', inner)
        if not src_match:
            return m.group(0)
        src = src_match.group(1)
        if src.startswith("http"):
            return m.group(0)
        path = ROOT / src.lstrip("/").lstrip("./")
        size = get_image_size(path)
        if not size or size[1] == 0:
            return m.group(0)
        if size[0] / size[1] <= 1.3:
            return m.group(0)
        if 'class="' in attrs:
            new_attrs = re.sub(r'class="([^"]*)"', r'class="\1 figure-wide"', attrs)
        else:
            new_attrs = attrs + ' class="figure-wide"'
        return f"<figure{new_attrs}>{inner}</figure>"
    return re.sub(r"<figure([^>]*)>(.*?)</figure>", repl, body, flags=re.DOTALL)


def load_notes() -> list[dict]:
    notes = json.loads(NOTES_JSON.read_text(encoding="utf-8"))
    notes = [n for n in notes if n.get("title") != "[TÍTULO]"]
    for n in notes:
        if n.get("body_html"):
            body = beautify_url_links(n["body_html"])
            body = auto_class_figure(body)
            n["body_html"] = body
    return notes


def label_for(kind: str, lang: str) -> str:
    return LABEL[kind].get(lang, LABEL[kind]["en"])


def render_label(kind: str, lang: str) -> str:
    cls = "label cronica" if kind == "cronica" else "label"
    return f'<p class="{cls}">{html.escape(label_for(kind, lang))}</p>'


PUBLISHED_SOURCES = {"Público", "Direitos Digitais"}


def render_date_meta(note: dict, lang: str) -> str:
    date = format_date(note.get("date", ""), lang)
    source = note.get("source")
    if source in PUBLISHED_SOURCES:
        return f'<span class="date">{html.escape(date)} · {html.escape(source)}</span>'
    return f'<span class="date">{html.escape(date)}</span>'


def render_cronica_block(note: dict) -> str:
    lang = (note.get("lang") or "en").lower()
    title = html.escape(note.get("title", ""))
    slug = get_slug(note)
    intro_html, was_cut = extract_intro(note.get("body_html", ""))
    cont = CONTINUE.get(lang, CONTINUE["en"])
    foot_left = (
        f'<a class="continue-link" href="notes/{slug}.html">{html.escape(cont)}</a>'
        if was_cut else '<span></span>'
    )
    return (
        f'<article class="entry cronica" data-lang="{html.escape(lang)}">'
        f'{render_label("cronica", lang)}'
        f'<h2 class="cronica-title"><a href="notes/{slug}.html">{title}</a></h2>'
        f'<div class="cronica-body">{intro_html}</div>'
        f'<div class="entry-foot">'
        f'{foot_left}'
        f'{render_date_meta(note, lang)}'
        f'</div>'
        f'</article>'
    )


def render_nota_block(note: dict) -> str:
    lang = (note.get("lang") or "en").lower()
    body = note.get("body_html", "")
    date = format_date(note.get("date", ""), lang)
    return (
        f'<article class="entry nota" data-lang="{html.escape(lang)}">'
        f'{render_label("nota", lang)}'
        f'<div class="nota-body">{body}</div>'
        f'<div class="nota-foot">{html.escape(date)}</div>'
        f'</article>'
    )


def render_excerto_block(note: dict) -> str:
    lang = (note.get("lang") or "en").lower()
    body = note.get("body_html", "")
    date = format_date(note.get("date", ""), lang)
    return (
        f'<article class="entry excerto" data-lang="{html.escape(lang)}">'
        f'{render_label("excerto", lang)}'
        f'<div class="excerto-body">{body}</div>'
        f'<div class="nota-foot">{html.escape(date)}</div>'
        f'</article>'
    )


def render_block(note: dict) -> str:
    kind = kind_of(note)
    if kind == "cronica":
        return render_cronica_block(note)
    if kind == "excerto":
        return render_excerto_block(note)
    return render_nota_block(note)


def join_with_sep(blocks: list[str]) -> str:
    if not blocks:
        return ""
    sep = '<div class="sep" aria-hidden="true">· — · — ·</div>'
    parts: list[str] = []
    for i, b in enumerate(blocks):
        parts.append(b)
        if i < len(blocks) - 1:
            parts.append(sep)
    return "\n".join(parts)


def render_mixed(notes: list[dict], limit: int | None = None) -> str:
    sorted_notes = sorted(notes, key=lambda n: (n.get("date") or ""), reverse=True)
    if limit is not None:
        sorted_notes = sorted_notes[:limit]
    return join_with_sep([render_block(n) for n in sorted_notes])


def render_filtered(notes: list[dict], kind: str) -> str:
    if kind == "cronica":
        filtered = [n for n in notes if is_cronica(n)]
    else:
        filtered = [n for n in notes if not is_cronica(n)]
    sorted_notes = sorted(filtered, key=lambda n: (n.get("date") or ""), reverse=True)
    return join_with_sep([render_block(n) for n in sorted_notes])


def replace_section(content: str, div_id: str, inner: str) -> str:
    pattern = re.compile(
        r'(<div id="' + div_id + r'"[^>]*>)(.*?)(</div>\s*</main>)',
        re.DOTALL,
    )
    return pattern.sub(lambda m: f"{m.group(1)}\n{inner}\n{m.group(3)}", content)


def update_html_page(path: Path, div_id: str, inner: str) -> None:
    if not path.exists():
        return
    content = path.read_text(encoding="utf-8")
    new = replace_section(content, div_id, inner)
    path.write_text(new, encoding="utf-8")


def rewrite_paths_for_subdir(body: str) -> str:
    """For pages inside /notes/, rewrite root-relative asset paths to ../assets/."""
    return re.sub(r'(src|href)="(assets/)', r'\1="../\2', body)


def render_note_page(note: dict) -> str:
    lang = (note.get("lang") or "en").lower()
    title = html.escape(note.get("title") or "")
    slug = get_slug(note)
    body_html = note.get("body_html", "") or ""
    body_clean = body_html.replace("<!--more-->", "")
    body_clean = rewrite_paths_for_subdir(body_clean)
    date = format_date(note.get("date", ""), lang)
    canonical = f"{SITE_URL}/notes/{slug}.html"
    desc = html.escape(strip_html(body_clean)[:200])
    kind = kind_of(note)
    label_text = label_for(kind, lang)
    label_cls = f"label {kind}" if kind in ("cronica", "excerto") else "label"
    title_block = (
        f'<h1 class="cronica-title">{title}</h1>'
        if kind == "cronica" else ""
    )
    body_cls = {"cronica": "cronica-body", "excerto": "excerto-body", "nota": "nota-body"}[kind]
    article_cls = f"entry {kind} single"
    page_title = title if title else "davide scarso"
    back = BACK.get(lang, BACK["en"])

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>{page_title} – davide scarso</title>
<meta name="description" content="{desc}"/>
<link rel="canonical" href="{canonical}"/>
<meta property="og:title" content="{page_title} – davide scarso"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:type" content="article"/>
<meta property="og:url" content="{canonical}"/>
<link href="../assets/css/style.css?v={CACHE_BUST}" rel="stylesheet"/>
</head>
<body class="page note lang-pending">
<header class="col">
<a class="brand" href="../index.html">Davide Scarso</a>
<nav>
<a href="../notas.html" data-i18n="nav_notas">notas</a>
<a href="../cronicas.html" data-i18n="nav_cronicas">crónicas</a>
<a href="../research.html" data-i18n="nav_research">pesquisa</a>
<a href="../about.html" data-i18n="nav_about">sobre</a>
</nav>
</header>
<main class="col">
<a class="back-archive" href="../arquivo.html" data-i18n="back_archive">{back}</a>
<article class="{article_cls}" data-lang="{lang}">
<p class="{label_cls}">{html.escape(label_text)}</p>
{title_block}
<div class="{body_cls}">{body_clean}</div>
<div class="entry-foot">{render_date_meta(note, lang)}</div>
</article>
</main>
<footer class="col">
<p class="footer-quote" data-i18n="footer_quote">Antes estavam no Facebook. Um mês de bloqueio sem explicação fez-me mudar de casa.</p>
<div class="footer-bar">
<a class="archive-link" href="../arquivo.html" data-i18n="archive_link">arquivo completo →</a>
</div>
</footer>
<script src="../assets/js/main.js?v={CACHE_BUST}"></script>
</body>
</html>
"""


def write_note_pages(notes: list[dict]) -> None:
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    seen_slugs: set[str] = set()
    for note in notes:
        slug = get_slug(note)
        # Garante unicidade — concatena com índice se necessário
        base_slug = slug
        i = 2
        while slug in seen_slugs:
            slug = f"{base_slug}-{i}"
            i += 1
        seen_slugs.add(slug)
        note_for_page = dict(note)
        note_for_page["slug"] = slug
        path = NOTES_DIR / f"{slug}.html"
        path.write_text(render_note_page(note_for_page), encoding="utf-8")


import datetime
import email.utils


def to_rfc822(date_str: str) -> str:
    parts = (date_str or "").split(" ")
    date_part = parts[0]
    time_part = parts[1] if len(parts) > 1 else "00:00:00"
    try:
        dt = datetime.datetime.strptime(f"{date_part} {time_part[:8]}", "%Y-%m-%d %H:%M:%S")
        return email.utils.format_datetime(dt.replace(tzinfo=datetime.timezone.utc))
    except ValueError:
        return ""


def absolutize_paths(html_body: str) -> str:
    """Converte 'assets/...' relativos em URLs absolutos para RSS."""
    return re.sub(r'(src|href)="(assets/)', rf'\1="{SITE_URL}/\2', html_body)


def feed_item_title(note: dict) -> str:
    title = (note.get("title") or "").strip()
    if title:
        return title
    plain = strip_html(note.get("body_html", "")).strip()
    if not plain:
        return "(sem título)"
    if len(plain) <= 70:
        return plain
    cut = plain[:70].rsplit(" ", 1)[0]
    return f"{cut}…"


def render_rss_item(note: dict) -> str:
    slug = get_slug(note)
    link = f"{SITE_URL}/notes/{slug}.html"
    pub_date = to_rfc822(note.get("date", ""))
    title = html.escape(feed_item_title(note))
    body = absolutize_paths(note.get("body_html", "").replace("<!--more-->", ""))
    return (
        "<item>\n"
        f"<title>{title}</title>\n"
        f"<link>{link}</link>\n"
        f'<guid isPermaLink="true">{link}</guid>\n'
        f"<pubDate>{pub_date}</pubDate>\n"
        f"<description><![CDATA[{body}]]></description>\n"
        "</item>"
    )


def render_rss(notes: list[dict]) -> str:
    sorted_notes = sorted(notes, key=lambda n: (n.get("date") or ""), reverse=True)
    items = [render_rss_item(n) for n in sorted_notes[:FEED_LIMIT]]
    now = email.utils.format_datetime(datetime.datetime.now(datetime.timezone.utc))
    items_xml = "\n".join(items)
    return f"""<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
<title>davide scarso</title>
<link>{SITE_URL}/</link>
<description>Crónicas, excertos e notas.</description>
<language>pt-PT</language>
<lastBuildDate>{now}</lastBuildDate>
<atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
{items_xml}
</channel>
</rss>
"""


def main() -> None:
    notes = load_notes()
    update_html_page(INDEX_HTML, "latest", render_mixed(notes, limit=HOME_LIMIT))
    update_html_page(ARQUIVO_HTML, "archive", render_mixed(notes))
    update_html_page(NOTES_HTML, "notes", render_filtered(notes, "nota"))
    update_html_page(CRONICAS_HTML, "cronicas", render_filtered(notes, "cronica"))
    write_note_pages(notes)
    FEED_XML.write_text(render_rss(notes), encoding="utf-8")


if __name__ == "__main__":
    main()
