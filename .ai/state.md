# Estado do Projeto — Site GitHub (repo3)

## Resumo
Site pessoal/académico em GitHub Pages, modelo **diarista-minimalista**.
Coluna 1000px, sans-serif system-ui, paleta austera com ferrugem
`#B85820` como acento pontual. Crónicas + excertos + notas misturados
em ordem cronológica inversa.

## Stack
- HTML estático puro (`.nojekyll`)
- CSS único: `assets/css/style.css` (cache bust via `?v=20260510f`,
  bumpar em mudanças visuais)
- JS: `assets/js/main.js` (i18n + email obfuscation; switcher de língua
  removido)
- Conteúdo das notas em `notes.json`, regenerado por
  `scripts/generate_notes.py`
- RSS: `feed.xml` gerado automaticamente (últimas 50 entradas)
- Backup do CSS antigo em `_archive/old-styles.css`

## Estrutura de páginas
- `/` (`index.html`) — listagem misturada, top 20 mais recentes
- `/arquivo.html` — listagem completa (96 entradas)
- `/notas.html` — só notas curtas e excertos (89)
- `/cronicas.html` — só crónicas (7)
- `/research.html` — publicações académicas; 7 entradas 2019+ com
  excerpt (4 curados pelo autor + 3 extraídos via pdftotext) e link
  "continuar a ler →" para o PDF
- `/about.html` — bio trilíngue (PT/IT/EN, via `.lang-block`)
- `/contact.html` — email pessoal (`dascarso@mailbox.org`) e afiliação
  institucional (DCSA, CIUHCT). **Página órfã** — só acessível por URL
  directo; email exposto no rodapé de todas as páginas
- `/howtos.html` — vazio mas presente; sem link no menu
- `/altopiano-1916.html` — página órfã auto-contida (guia de férias
  Altopiano di Asiago 1916 / Vicenza, partilhada com o filho). Só por
  URL directo; sem link no menu nem no sitemap. Design próprio (fontes
  Oswald/Spectral, não usa `style.css`); 16 imagens em base64
- `/notes/{slug}.html` — página individual para cada uma das 96 entradas
- `/feed.xml` — RSS 2.0 com as 50 mais recentes

## Categorias de conteúdo
- **Crónica** (`category: "cronica"` em `notes.json`, marcador
  `<!--more-->` no body): label "— CRÓNICA" em ferrugem, título 28px,
  intro até ao corte, link "continuar a ler →" + data e (quando aplica)
  origem de publicação ("· Público" / "· Direitos Digitais")
- **Excerto** (`category: "excerto"`): citação ou texto não-próprio.
  Label "— EXCERTO" cinzento, body com border-left subtil, indent
- **Nota**: label "— NOTA" cinzento, body completo
- Separador entre entradas: `· — · — ·` em ferrugem, 22px, centrado
- URLs externos no body são re-renderizados como "Link ↗" pelo script

## Imagens
- `<figure>` com auto-classificação: imagens panorâmicas (W/H > 1.3)
  ganham `figure-wide` (max-width 400px); restantes 280px
- Float right por defeito, texto envolve à esquerda
- Em mobile (<640px): float removido, full-width centrada
- `class="figure-left"` para flutuar à esquerda
- Imagens guardadas em `assets/images/` com paths relativos à raiz
  (`assets/...`); script reescreve `../assets/...` para uso em
  `/notes/{slug}.html`

## Tipografia (escala)
- Body / nota-body: 19px, line-height 1.65
- Crónica-body / excerto-body / pub-list: 18-19px, line-height 1.65-1.75
- Pub-abstract: 17px
- Brand "davide scarso": 21px sans, lowercase via CSS
- Cronica-title: 28px serif
- Nav menu: 15px regular (sem itálico)
- Labels (— CRÓNICA, etc.): 12px tracking 1.5px uppercase ferrugem/cinza
- Entry-foot (continue-link, date): 13px tracking 0.3px
- Stack: `system-ui, -apple-system, "Segoe UI", "Noto Sans",
  "Helvetica Neue", Helvetica, Arial, sans-serif`

## Cabeçalho
- Brand "davide scarso" 21px à esquerda; nav direita
- Items: notas / crónicas / pesquisa / sobre
- Item activo a `var(--ink)`; outros a `var(--muted)`
- Sem barra ferrugem nem border-bottom

## Rodapé
- 48px de margem superior, 28px de padding vertical
- Border-top 0.5px `var(--rule)`
- Single bar: "arquivo completo →" à esquerda + "contato →" à direita
- Sem switcher de língua (auto-detecta via browser)
- Sem frase de origem (foi removida)

## Datas
- Localizadas em minúsculas: "10 outubro 2025" / "10 ottobre 2025" /
  "10 october 2025"

## Fluxo de manutenção
- Adicionar/editar em `notes.json`
- Para crónicas: `category: "cronica"`, `<!--more-->` no body, `slug`
- Para excertos: `category: "excerto"`
- Imagens: pôr em `assets/images/`, referenciar com `src="assets/..."`
- Correr `python3 scripts/generate_notes.py`
- Bumpar cache `v=...` ao alterar CSS/JS
- Commit em PT-PT
- `git push origin main` → produção (GitHub Pages, ~1-2 min)

## Git
- **`main`** sincronizada com `origin/main` (publicada).
- Branch `redesign-2026` arquivada localmente e em `origin/`
  (estado anterior ao merge, para histórico).
- Conta `davidescarso` (dona do repo) ↔ commits autorados por
  `ds451 <ds451@mailbox.org>` (split intencional: humano vs. site).
- Repo antigo `ds451/davidescarso.github.io` foi apagado em 2026-05-10
  (mirror obsoleto).

## Estratégia de distribuição (POSSE)
- Site é canónico; redes sociais são spokes
- Bluesky / Mastodon recomendado (FB e X evitados por coerência política)
- Substack: não usar (duplicaria infraestrutura)
- RSS já implementado: feed.xml + auto-discovery via `<link
  rel="alternate">`
- Email institucional substituído por pessoal `dascarso@mailbox.org`

## Versão ativa
- `/home/ds451/code/site_github/davidescarso.github.io_repo3`
- Live: https://davidescarso.github.io
