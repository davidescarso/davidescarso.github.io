# Projeto: Site Pessoal GitHub

Site pessoal hospedado em GitHub Pages: davidescarso.github.io

## Contexto

Site académico/profissional para:
- Apresentação pessoal (about)
- Publicações e research (research.html)
- Notas e blog (notas.html)
- Contacto (contact - provavelmente via index.html)

## Estrutura

**VERSÃO ATIVA: davidescarso.github.io_repo3** (esta pasta)

Outras versões existentes (NÃO USAR sem confirmar):
- `../davidescarso.github.io/` - Sem git, versão antiga
- `../davidescarso.github.io_repo/` - Com git, tem estrutura EN/PT
- `../davidescarso.github.io_repo2/` - Com git, versão anterior
- `../davidescarso.github.io_repo2_backup_20260127/` - Backup

### Ficheiros Principais (repo3)
- `index.html` - Página inicial
- `research.html` - Publicações e projetos
- `notas.html` - Blog/notas (ficheiro grande, ~728KB)
- `notes/` - Pasta com notas individuais (provavelmente)
- Assets: CSS, JS, imagens (verificar estrutura)

## Stack Técnico

**Aparentemente:**
- HTML estático puro (GitHub Pages)
- Sem Jekyll, Hugo ou outro SSG (Static Site Generator)
- Provavelmente CSS custom + possivelmente algum framework leve

**Git:**
- Remote: `https://davidescarso@github.com/davidescarso/davidescarso.github.io.git`
- Branch principal: verificar se é `main` ou `gh-pages`

## Workflow

### Antes de Modificar HTML
1. **Preview local**: Abrir ficheiro no browser antes de commit
2. **Responsividade**: Se modificar layout, testar em mobile/desktop
3. **Links**: Verificar que links internos funcionam (especialmente se mover ficheiros)
4. **Encodings**: Manter UTF-8 para caracteres portugueses (à, ç, etc.)

### Ao Modificar Conteúdo
- **research.html**: Cuidado com formatação de citações académicas
- **notas.html**: Ficheiro MUITO grande (728KB) - mudanças podem ser lentas
  - Considerar: será que deve ser dividido em ficheiros separados?
  - Ou usar paginação/índice?
- **Manter estilo existente**: Não alterar design sem pedir

### Git e Deploy
- Commits: Mensagens em PT-PT (seguir convenção do projeto)
- **NÃO fazer push sem confirmar** - vai direto para o site público
- GitHub Pages faz deploy automático após push para branch principal
- Deploy demora ~1-2 minutos após push

### Backups
- Antes de mudanças estruturais grandes: considerar criar backup com data
  - Exemplo: `cp -r ../davidescarso.github.io_repo3 ../davidescarso.github.io_repo3_backup_YYYYMMDD`

## Preferências de Design (a confirmar com utilizador)

Assumindo baseado no perfil:
- Estilo minimalista/académico
- Tipografia legível, sem decorações excessivas
- Foco no conteúdo textual
- Provavelmente sem muitos gráficos/animações

**Antes de:**
- Mudar cores ou layout principal
- Adicionar JavaScript pesado
- Mudar estrutura de navegação
- Adicionar fontes web (Google Fonts, etc.)

→ **Confirmar com utilizador**

## Manutenção de Conteúdo

### Adicionar Nova Publicação (research.html)
1. Seguir formato de entradas existentes
2. Manter ordem cronológica (ou outra lógica existente)
3. Verificar links para PDFs/DOIs
4. Conferir acentuação e formatação

### Adicionar Nova Nota (notas.html)
1. **ATENÇÃO**: Ficheiro muito grande
2. Adicionar no topo (mais recente primeiro) ou no fundo?
3. Verificar se há índice/tabela de conteúdos a atualizar
4. Considerar meta-informação (data, tags?)

### Imagens e Assets
- Otimizar imagens antes de adicionar (comprimir JPG/PNG)
- Usar caminhos relativos (não absolutos)
- Manter estrutura de pastas consistente

## Tecnologias a Considerar (futuro)

Se o site crescer muito, pode valer a pena:
- **Jekyll/Hugo**: Geração estática com templates
- **Pagination**: Para notas.html (está muito grande)
- **Search**: Busca client-side para notas
- **RSS feed**: Para blog/notas

Mas: não adicionar complexidade sem necessidade clara.

## Dados Sensíveis

- Nenhum esperado (site é público)
- Cuidado ao adicionar emails pessoais (usar emails institucionais/públicos)
- Não incluir dados de analytics (Google Analytics ID) sem confirmar

## Comandos Úteis

```bash
# Ver status
git status

# Preview local (abrir no browser)
firefox index.html

# Ver histórico de commits
git log --oneline -10

# Ver diferenças antes de commit
git diff research.html

# Commit e push (CUIDADO - vai para produção!)
git add .
git commit -m "Atualiza research com nova publicação"
# git push  # NÃO executar sem confirmação!
```

---

**Ver também:** `~/Claude.md` para preferências gerais do utilizador.
