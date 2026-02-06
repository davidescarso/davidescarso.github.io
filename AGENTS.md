# Projeto: Site Pessoal GitHub

Site pessoal hospedado em GitHub Pages: davidescarso.github.io

## Contexto

Site académico/profissional para:
- Apresentação pessoal (about)
- Publicações e research (research.html)
- Notas e blog (notas.html)
- Contacto (contact - provavelmente via index.html)

## Estrutura

**VERSAO ATIVA: davidescarso.github.io_repo3** (esta pasta)

Outras versoes existentes (NAO USAR sem confirmar):
- `../davidescarso.github.io/` - Sem git, versao antiga
- `../davidescarso.github.io_repo/` - Com git, tem estrutura EN/PT
- `../davidescarso.github.io_repo2/` - Com git, versao anterior
- `../davidescarso.github.io_repo2_backup_20260127/` - Backup

### Ficheiros Principais (repo3)
- `index.html` - Pagina inicial
- `research.html` - Publicacoes e projetos
- `notas.html` - Blog/notas (ficheiro grande, ~728KB)
- `notes/` - Pasta com notas individuais (provavelmente)
- Assets: CSS, JS, imagens (verificar estrutura)

## Stack Tecnico

**Aparentemente:**
- HTML estatico puro (GitHub Pages)
- Sem Jekyll, Hugo ou outro SSG (Static Site Generator)
- Provavelmente CSS custom + possivelmente algum framework leve

**Git:**
- Remote: `https://davidescarso@github.com/davidescarso/davidescarso.github.io.git`
- Branch principal: verificar se e `main` ou `gh-pages`

## Workflow

### Antes de Modificar HTML
1. **Preview local**: Abrir ficheiro no browser antes de commit
2. **Responsividade**: Se modificar layout, testar em mobile/desktop
3. **Links**: Verificar que links internos funcionam (especialmente se mover ficheiros)
4. **Encodings**: Manter UTF-8 para caracteres portugueses (a, c, etc.)

### Ao Modificar Conteudo
- **research.html**: Cuidado com formatacao de citacoes academicas
- **notas.html**: Ficheiro MUITO grande (728KB) - mudancas podem ser lentas
  - Considerar: sera que deve ser dividido em ficheiros separados?
  - Ou usar paginacao/indice?
- **Manter estilo existente**: Nao alterar design sem pedir

### Git e Deploy
- Commits: Mensagens em PT-PT (seguir convencao do projeto)
- **NAO fazer push sem confirmar** - vai direto para o site publico
- GitHub Pages faz deploy automatico apos push para branch principal
- Deploy demora ~1-2 minutos apos push

### Backups
- Antes de mudancas estruturais grandes: considerar criar backup com data
  - Exemplo: `cp -r ../davidescarso.github.io_repo3 ../davidescarso.github.io_repo3_backup_YYYYMMDD`
- Ao retomar trabalho: consultar `.ai/state.md` e `.ai/decisions.md`
- Apos reorganizacoes estruturais: anotar no `.ai/changelog.md` e atualizar `.ai/state.md` (e `AGENTS.md` se relevante)

## Preferencias de Design (a confirmar com utilizador)

Assumindo baseado no perfil:
- Estilo minimalista/academico
- Tipografia legivel, sem decoracoes excessivas
- Foco no conteudo textual
- Provavelmente sem muitos graficos/animacoes

**Antes de:**
- Mudar cores ou layout principal
- Adicionar JavaScript pesado
- Mudar estrutura de navegacao
- Adicionar fontes web (Google Fonts, etc.)

-> **Confirmar com utilizador**

## Manutencao de Conteudo

### Adicionar Nova Publicacao (research.html)
1. Seguir formato de entradas existentes
2. Manter ordem cronologica (ou outra logica existente)
3. Verificar links para PDFs/DOIs
4. Conferir acentuacao e formatacao

### Adicionar Nova Nota (notas.html)
1. **ATENCAO**: Ficheiro muito grande
2. Adicionar no topo (mais recente primeiro) ou no fundo?
3. Verificar se ha indice/tabela de conteudos a atualizar
4. Considerar meta-informacao (data, tags?)

### Imagens e Assets
- Otimizar imagens antes de adicionar (comprimir JPG/PNG)
- Usar caminhos relativos (nao absolutos)
- Manter estrutura de pastas consistente

## Tecnologias a Considerar (futuro)

Se o site crescer muito, pode valer a pena:
- **Jekyll/Hugo**: Geracao estatica com templates
- **Pagination**: Para notas.html (esta muito grande)
- **Search**: Busca client-side para notas
- **RSS feed**: Para blog/notas

Mas: nao adicionar complexidade sem necessidade clara.

## Dados Sensiveis

- Nenhum esperado (site e publico)
- Cuidado ao adicionar emails pessoais (usar emails institucionais/publicos)
- Nao incluir dados de analytics (Google Analytics ID) sem confirmar

## Comandos Uteis

```bash
# Ver status
git status

# Preview local (abrir no browser)
firefox index.html

# Ver historico de commits
git log --oneline -10

# Ver diferencas antes de commit
git diff research.html

# Commit e push (CUIDADO - vai para producao!)
git add .
git commit -m "Atualiza research com nova publicacao"
# git push  # NAO executar sem confirmacao!
```

---

**Ver tambem:** `~/Claude.md` para preferencias gerais do utilizador.
