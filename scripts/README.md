# Scripts

Pequenos utilitarios para manter o site.

## update_random_images.sh

Gera automaticamente a lista de imagens aleatorias usada na home.

O script:
- lê `assets/images/random/`
- gera `assets/js/random_images.js`

Uso:
```
./scripts/update_random_images.sh
```

## generate_notes.py

Gera a pagina de notas estáticas e as paginas individuais para notas longas.

O script:
- lê `notes.json`
- atualiza `notas.html` com a lista renderizada (estático)
- cria `notes/*.html` para notas com `full_page: true`

Uso:
```
python3 scripts/generate_notes.py
```

## generate_sitemap.py

Gera `sitemap.xml` com as paginas principais e notas individuais.

Uso:
```
python3 scripts/generate_sitemap.py
```
