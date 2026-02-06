# Decisões Arquiteturais (ADR) — Site GitHub (repo3)

## Regras operacionais (2026-02-05)
**Decisão**
Ao retomar trabalho, consultar `.ai/state.md` e `.ai/decisions.md`. Após mudanças estruturais, atualizar `.ai/state.md` e, quando relevante, `Claude.md`. Após reorganizações estruturais, anotar no `.ai/changelog.md`.

**Consequências**
Reduz perda de contexto após hiatos e mantém documentação mínima coerente.

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
