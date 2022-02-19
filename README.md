# LI²A: Linguagem Inclusiva com Inteligência Artificial

Ferramenta de linguagem inclusiva em Português

## Dados
all_nouns.csv:
  Palavras que são flexionadas por gênero (4 variações). Inclui a coluna 'meaning' com o significado de dicionário de cada palavra do arquivo.

4plus_variation_nouns.csv:
  Subset de all_nouns com palavras que são flexionadas por gênero (4+ variações).


## Como Executar a Aplicação
Para rodar a aplicação, primeiro instale o poetry (https://python-poetry.org/docs/).
No Mac pode ser instalado via Brew:
`$ brew install poetry`

Em seguida execute:
```
$ poetry install
$ poetry run streamlit run app.py
```

Se você preferir utilizar um requirements.txt para instalar dependências, pode executar os seguintes comandos para criar o requirements.txt.
`$ poetry export -f requirements.txt > requirements.txt`


## Fluxo da Aplicação

<p align="center">
  <img src="img/LIA.jpg" width="600">
</p>

[Link do arquivo .drawio para editar o fluxo](https://drive.google.com/file/d/16eAe_DxUXD3WKhiTgltBbe9OE9i-_I7K/view?usp=sharing)
