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
NOTES_DIR = ROOT / "notes"
SITE_URL = "https://davidescarso.github.io"
CACHE_BUST = "20260510a"
HOME_LIMIT = 20

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


def load_notes() -> list[dict]:
    notes = json.loads(NOTES_JSON.read_text(encoding="utf-8"))
    return [n for n in notes if n.get("title") != "[TÍTULO]"]


def label_for(kind: str, lang: str) -> str:
    return LABEL[kind].get(lang, LABEL[kind]["en"])


def render_label(kind: str, lang: str) -> str:
    cls = "label cronica" if kind == "cronica" else "label"
    return f'<p class="{cls}">{html.escape(label_for(kind, lang))}</p>'


def render_cronica_block(note: dict) -> str:
    lang = (note.get("lang") or "en").lower()
    title = html.escape(note.get("title", ""))
    slug = get_slug(note)
    intro_html, was_cut = extract_intro(note.get("body_html", ""))
    date = format_date(note.get("date", ""), lang)
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
        f'<span class="date">{html.escape(date)}</span>'
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
    sep = '<div class="sep" aria-hidden="true">— · — · — · —</div>'
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


def render_note_page(note: dict) -> str:
    lang = (note.get("lang") or "en").lower()
    title = html.escape(note.get("title") or "")
    slug = get_slug(note)
    body_html = note.get("body_html", "") or ""
    body_clean = body_html.replace("<!--more-->", "")
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
    page_title = title if title else "Davide Scarso"
    back = BACK.get(lang, BACK["en"])

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>{page_title} – Davide Scarso</title>
<meta name="description" content="{desc}"/>
<link rel="canonical" href="{canonical}"/>
<meta property="og:title" content="{page_title} – Davide Scarso"/>
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
<div class="entry-foot"><span class="date">{html.escape(date)}</span></div>
</article>
</main>
<footer class="col">
<p class="footer-quote" data-i18n="footer_quote">Antes estavam no Facebook. Um mês de bloqueio sem explicação fez-me mudar de casa.</p>
<div class="footer-bar">
<a class="archive-link" href="../arquivo.html" data-i18n="archive_link">arquivo completo →</a>
<div class="lang-switcher" data-i18n-aria="lang_label">
<a class="lang-opt" data-lang="pt" href="?lang=pt">pt</a>
<span class="lang-sep" aria-hidden="true">·</span>
<a class="lang-opt" data-lang="it" href="?lang=it">it</a>
<span class="lang-sep" aria-hidden="true">·</span>
<a class="lang-opt" data-lang="en" href="?lang=en">en</a>
</div>
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


def main() -> None:
    notes = load_notes()
    update_html_page(INDEX_HTML, "latest", render_mixed(notes, limit=HOME_LIMIT))
    update_html_page(ARQUIVO_HTML, "archive", render_mixed(notes))
    update_html_page(NOTES_HTML, "notes", render_filtered(notes, "nota"))
    update_html_page(CRONICAS_HTML, "cronicas", render_filtered(notes, "cronica"))
    write_note_pages(notes)


if __name__ == "__main__":
    main()
