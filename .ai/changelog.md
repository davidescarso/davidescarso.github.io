# Changelog — Site GitHub (repo3)

## 2026-02-02
- Criada estrutura `.ai/` e registado estado inicial do projeto.

## 2026-02-05
- Regras adicionadas para retoma (`.ai/state.md`, `.ai/decisions.md`) e atualização após mudanças estruturais.

## 2026-05-09
- Cor de acento laranja-ferrugem `#B85820` introduzida em links de corpo,
  barra do header, datas das notas (commit `cb98a7f`).
- Criada secção Ensaios (`ensaios.html`) e link Howtos retirado do menu
  (commit `1c2d280`).
- Microajustes: brand serif, divisores subtis, datas localizadas, switcher
  trilíngue PT·IT·EN no header (commit `17832a2`).
- Hero da home reduzido e depois removido (commits `54cb7a6`, `996b291`).
- Fix de especificidade CSS do `.brand` (commit `c34d7f1`).

## 2026-05-10 — redesign v2 (branch `redesign-2026`)
Rewrite radical para modelo diarista-minimalista (Craig Mod / Robin Sloan).
- `prep: backup do CSS antigo em _archive/` (`ff63ff9`)
- `tipografia e layout: serif, coluna 580px, paleta minimalista` (`0d93bf6`)
- `templates: header/rodapé minimalistas em todos os HTMLs` (`43608ea`)
- `script: gera todas as 95 notas individualmente; nova listagem misturada` (`ab109b0`)
- `crónicas: marca category + insere cortes <!--more-->` (`186d7ff`)
- `i18n: renomeia ensaios → crónicas, adiciona frase do rodapé` (`7469a8b`)
- `docs: actualiza .ai/state.md e .ai/changelog.md` (`f600c29`)
- `layout: coluna 580→680→740→800→1000px` (vários, iterações)
- `categoria excerto` para 27 entradas (citações) (`5550c50`)
- `home limitada a 20`, novo `arquivo.html` (`17471f2`)
- Promoção da nota Câmara de Lisboa a crónica D3 (`34c42f2`)
- `tipografia: corpo +2px, brand 17→21px` (`0d28f49`)
- Separador `· — · — ·` em ferrugem (após várias iterações)
- Niobe + Musk com `<figure>` float right; auto-class figure-wide
  (`118a20b`, `d511559`, `4354dbe`, `e497a1b`)
- Brand lowercase via CSS (`ac51500`)
- Crónica nova: "A política como representação" (`eb0b9e7`)
- Fonte: serif → Charter → Noto Serif → **sans-serif (system-ui)**
  (`693307e`, `db6cc01`, `c65a220`)
- Reduce margem entre entradas (96→64px) (`88609b9`)
- `pesquisa: excertos + continuar a ler` (`11ee6e8`, `014c14f`)
- Títulos todos lowercase (`0663fa8`)

## 2026-05-10 — Merge redesign-2026 → main, publish
- Fast-forward main para 2bc0702; `git push origin main`
- Site live em https://davidescarso.github.io
- Branch `redesign-2026` também push para origem (arquivo histórico)
- Apaga repo antigo `ds451/davidescarso.github.io` (mirror obsoleto)

## 2026-05-12 — Polimento pós-publicação
- Removido switcher pt · it · en (sem traduções reais) (`523119d`)
- Data Elon Musk corrigida 2025-10-10 → 2025-01-05 (`a77d67d`)
- Crónicas indicam origem ("· Público" / "· Direitos Digitais")
  ao lado da data (`66021ba`)
- RSS 2.0 em `/feed.xml` + auto-discovery via `<link rel="alternate">`
  (`3bc4217`)
- Email institucional → pessoal `dascarso@mailbox.org`;
  "contato →" no rodapé (`7cf3b7d`)
- Texto do /sobre passa a 18px (igual aos crónica-body) (`f608c2f`)
- Frase do Facebook movida para /sobre e depois removida
  (`733c8f6`, `c670ae2`, `4ae94dd`, `1e62f41`)
- Rodapé sem frase de origem, mais perto do corpo
- ds451/davidescarso.github.io apagado via gh repo delete
