# Decisões Arquiteturais (ADR) — Site GitHub (repo3)

## ADR-001 — 2026-02-02 — Site estático em HTML puro
**Contexto**
O repositório contém páginas HTML estáticas e scripts simples de manutenção, sem SSG.

**Decisão**
Manter o site como HTML estático (sem Jekyll/Hugo) no curto prazo.

**Consequências**
Atualizações são diretas mas manuais; scripts continuam a ser a principal automação.

## ADR-002 — 2026-02-02 — Sistema de notas via `notes.json`
**Contexto**
As notas são geradas a partir de `notes.json` para `notas.html` e páginas individuais em `notes/`.

**Decisão**
Manter o fluxo de geração de notas via `scripts/generate_notes.py`.

**Consequências**
Qualquer mudança no formato de `notes.json` exige atualização do gerador.

## ADR-003 — 2026-02-02 — Versionamento ativo é repo3
**Contexto**
Existem múltiplas versões do site em `site_github/`, com a versão ativa declarada como `repo3`.

**Decisão**
Usar `davidescarso.github.io_repo3` como base de trabalho.

**Consequências**
Outras versões ficam apenas como referência/backup.
