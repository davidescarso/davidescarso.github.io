# Estado do Projeto — Site GitHub (repo3)

## Resumo
Site pessoal/académico hospedado em GitHub Pages. Modelo diarista-minimalista
(redesign 2026-05): coluna 580px, só serif, paleta austera com ferrugem
`#B85820` como acento pontual.

## Stack
- HTML estático puro (sem Jekyll, `.nojekyll` activo)
- CSS único: `assets/css/style.css` (~250 linhas; backup do anterior em
  `_archive/old-styles.css`)
- Multilingue client-side: `assets/js/main.js` (PT/IT/EN via `data-i18n`,
  `data-lang` para `.lang-block` em about)
- Conteúdo das notas em `notes.json`, regenerado por `scripts/generate_notes.py`
- Sem fontes externas. Sem sans-serif. Apenas peso 400.

## Estrutura de páginas
- `index.html` — listagem misturada (crónicas + notas) cronológica inversa,
  separador asterisco `∗`
- `notas.html` — só notas curtas
- `cronicas.html` — só crónicas (substitui o antigo `ensaios.html`)
- `research.html` — publicações
- `about.html`, `contact.html`, `howtos.html` — estáticas
- `notes/{slug}.html` — 95 páginas individuais (uma por entrada de `notes.json`)

## Categorias de conteúdo
- **Crónica** (`category: "cronica"` em `notes.json`, com marcador
  `<!--more-->` no `body_html`): label "— CRÓNICA" em ferrugem, título 28px,
  intro até ao marcador, link "continuar a ler →"
- **Nota** (sem `category`): label "— NOTA" em cinzento, body completo
- Asterisco `∗` em ferrugem entre entradas

## Menu
`notas / crónicas / pesquisa / sobre` (4 items, em itálico). "Howtos" e
"contato" continuam acessíveis por URL mas fora do menu.

## Rodapé
- Frase de origem em itálico (PT/IT/EN, `data-i18n="footer_quote"`)
- "arquivo completo →" à esquerda, switcher `pt · it · en` à direita
- Switcher de língua só no rodapé (saiu do header)

## Fluxo de manutenção
- Adicionar/editar conteúdo em `notes.json`
- Para crónicas: pôr `category: "cronica"` e inserir `<!--more-->` no body
- Correr `python3 scripts/generate_notes.py` (regenera `index.html`,
  `notas.html`, `cronicas.html` e os ficheiros em `notes/`)
- Commit (mensagens em PT-PT)
- `git push` = produção (deploy GitHub Pages ~1-2 min)

## Branch e estado git
- **`redesign-2026`** (local, sem push): branch com o redesign completo,
  6 commits à frente de `main`. Aguarda pull request / merge.
- `main`: estado anterior (cores ferrugem, ensaios, switcher no header,
  layout antigo). 7 commits à frente de `origin/main`.

## Problemas conhecidos
- Em `file://` o switcher de língua usa `?lang=xx` que actualiza a URL via
  `history.replaceState`; funciona mas o reload pelo URL não trabalha em
  file:// (works no servidor)
- `assets/fonts/inter/` e `assets/fonts/fira-code/` ainda no disco
  (não são carregadas — limpeza posterior opcional)
- Não há dark mode

## Versão ativa
- `/home/ds451/code/site_github/davidescarso.github.io_repo3`
