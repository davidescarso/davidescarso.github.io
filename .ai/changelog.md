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

## 2026-05-10 — redesign v2 (branch `redesign-2026`, sem push)
Rewrite radical para modelo diarista-minimalista (Craig Mod / Robin Sloan).
- `prep: backup do CSS antigo em _archive/` (`ff63ff9`)
- `tipografia e layout: serif, coluna 580px, paleta minimalista` (`0d93bf6`)
- `templates: header/rodapé minimalistas em todos os HTMLs` (`43608ea`)
- `script: gera todas as 95 notas individualmente; nova listagem misturada` (`ab109b0`)
- `crónicas: marca category + insere cortes <!--more-->` (`186d7ff`)
- `i18n: renomeia ensaios → crónicas, adiciona frase do rodapé` (`7469a8b`)

Mudanças estruturais:
- `ensaios.html` → `cronicas.html`
- Cada nota ganha página própria em `notes/{slug}.html` (95 ficheiros)
- `index.html` passa a ser listagem misturada (notas + crónicas)
- Menu reduzido a 4 items (notas/crónicas/pesquisa/sobre)
- Switcher de língua move para o rodapé
- Fonte: só serif (Iowan Old Style → Palatino → Georgia)
- Coluna fixa 580px
- Frase de origem no rodapé sobre a saída do Facebook (PT/IT/EN)
