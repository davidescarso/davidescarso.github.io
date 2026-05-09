#!/usr/bin/env python3
"""Gera howtos.html e páginas individuais em howtos/ a partir de howtos.json."""
from __future__ import annotations

import html
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUCOES_JSON = ROOT / "howtos.json"
SOLUCOES_HTML = ROOT / "howtos.html"
SOLUCOES_DIR = ROOT / "howtos"
SITE_URL = "https://davidescarso.github.io"
OG_IMAGE = f"{SITE_URL}/assets/images/random/alcantara2.jpeg"


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    return text or "howto"


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


def text_to_html(text: str) -> str:
    """Converte texto simples para HTML, com suporte a blocos de código (```)."""
    if not text:
        return ""
    parts = []
    in_code = False
    code_lines: list[str] = []
    for line in text.split("\n"):
        if line.strip().startswith("```"):
            if in_code:
                code = html.escape("\n".join(code_lines))
                parts.append(f"<pre><code>{code}</code></pre>")
                code_lines = []
                in_code = False
            else:
                in_code = True
        elif in_code:
            code_lines.append(line)
        elif line.strip():
            parts.append(f"<p>{html.escape(line.strip())}</p>")
    if in_code and code_lines:
        code = html.escape("\n".join(code_lines))
        parts.append(f"<pre><code>{code}</code></pre>")
    return "\n".join(parts)


def render_body_html(sol: dict) -> str:
    """Constrói o body_html completo de uma solução a partir dos campos estruturados."""
    parts = [
        '<p><span class="ccaia-badge">&#x1F916; IA-assistida (CCAIA)</span></p>'
    ]

    for label, key in [
        ("Problema", "problema"),
        ("Contexto", "sistema"),
        ("Solução", "solucao"),
        ("Verificação", "verificacao"),
    ]:
        content = text_to_html(sol.get(key, ""))
        if content:
            parts.append(f'<div class="sol-section"><strong>{label}</strong>{content}</div>')

    notas = text_to_html(sol.get("notas", ""))
    if notas:
        parts.append(f'<div class="sol-section"><strong>Notas</strong>{notas}</div>')

    parts.append(
        '<p class="ccaia-license">Produzido com assistência de IA (Claude). '
        'Licença <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>.</p>'
    )
    return "\n".join(parts)


def load_solucoes() -> list[dict]:
    return json.loads(SOLUCOES_JSON.read_text(encoding="utf-8"))  # noqa: kept name for clarity


def get_cache_bust() -> str:
    content = SOLUCOES_HTML.read_text(encoding="utf-8")
    match = re.search(r"style\.css\?v=([^\"\s]+)", content)
    return match.group(1) if match else "1"


def render_list_item(sol: dict) -> str:
    title = html.escape(sol.get("title", ""))
    date = sol.get("date", "")[:10]
    sistema = html.escape(sol.get("sistema", ""))
    slug = sol.get("slug") or slugify(sol.get("title", ""))

    plain = strip_html(render_body_html(sol))
    excerpt = html.escape(build_excerpt(plain, 400))

    meta_parts = [date]
    if sistema:
        meta_parts.append(sistema)

    return (
        f'<article class="post-item">'
        f'<p class="meta">{" · ".join(meta_parts)}</p>'
        f'<div class="post-body">'
        f'<h2 class="sol-title"><a href="howtos/{slug}.html">{title}</a></h2>'
        f'<p class="excerpt">{excerpt}</p>'
        f'<a class="read-more" href="howtos/{slug}.html">Ver howto</a>'
        f"</div>"
        f"</article>"
    )


def render_list(solucoes: list[dict]) -> str:
    if not solucoes:
        return '<p class="meta">Nenhum howto publicado ainda.</p>'
    items = []
    for idx, sol in enumerate(solucoes):
        items.append(render_list_item(sol))
        if idx < len(solucoes) - 1:
            items.append('<hr class="post-divider"/>')
    return "\n".join(items)


def render_solution_page(sol: dict, cache_bust: str) -> str:
    title = html.escape(sol.get("title", ""))
    date = sol.get("date", "")[:10]
    sistema = html.escape(sol.get("sistema", ""))
    slug = sol.get("slug") or slugify(sol.get("title", ""))
    canonical = f"{SITE_URL}/howtos/{slug}.html"
    body_html = render_body_html(sol)
    desc = html.escape(build_excerpt(strip_html(body_html), 200))

    meta_parts = [date]
    if sistema:
        meta_parts.append(sistema)
    meta_html = " · ".join(meta_parts)

    return f"""<!DOCTYPE html>

<html lang="pt">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>{title} – Davide Scarso</title>
<meta name="description" content="{desc}"/>
<link rel="canonical" href="{canonical}"/>
<meta property="og:title" content="{title} – Davide Scarso"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:type" content="article"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:image" content="{OG_IMAGE}"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{title} – Davide Scarso"/>
<meta name="twitter:description" content="{desc}"/>
<meta name="twitter:image" content="{OG_IMAGE}"/>
<link href="../assets/css/style.css?v={cache_bust}" rel="stylesheet"/>
</head>
<body class="page note loading">
<header>
<div class="nav">
<a class="brand" href="../index.html">Davide Scarso</a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-menu">Menu</button>
<nav id="site-menu">
<a data-i18n="nav_blog" href="../notas.html">Notas</a>
<a data-i18n="nav_research" href="../research.html">Pesquisa</a>
<a class="active" href="../howtos.html">Howtos</a>
<a data-i18n="nav_about" href="../about.html">Sobre</a>
<a data-i18n="nav_contact" href="../contact.html">Contato</a>
</nav>
</div>
</header>
<main>
<article class="note-entry" data-lang="pt">
<h1 class="note-title">{title}</h1>
<p class="meta">{meta_html}</p>
<div class="post-body">{body_html}</div>
</article>
</main>
<script src="../assets/js/main.js?v={cache_bust}"></script>
</body>
</html>
"""


def write_solution_pages(solucoes: list[dict], cache_bust: str) -> None:
    SOLUCOES_DIR.mkdir(parents=True, exist_ok=True)
    for sol in solucoes:
        slug = sol.get("slug") or slugify(sol.get("title", ""))
        path = SOLUCOES_DIR / f"{slug}.html"
        path.write_text(render_solution_page(sol, cache_bust), encoding="utf-8")


def update_solucoes_html(solucoes: list[dict], cache_bust: str) -> None:
    content = SOLUCOES_HTML.read_text(encoding="utf-8")
    rendered = render_list(solucoes)
    content = re.sub(
        r"(<div id=\"solucoes\"[^>]*>)(.*?)(</div>\s*</main>)",
        lambda m: f"{m.group(1)}\n{rendered}\n{m.group(3)}",
        content,
        flags=re.DOTALL,
    )
    SOLUCOES_HTML.write_text(content, encoding="utf-8")


def main() -> None:
    solucoes = load_solucoes()
    cache_bust = get_cache_bust()
    update_solucoes_html(solucoes, cache_bust)
    write_solution_pages(solucoes, cache_bust)
    print(f"✓ {len(solucoes)} howto(s) gerado(s)")


if __name__ == "__main__":
    main()
