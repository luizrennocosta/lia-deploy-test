from unicodedata import normalize
import base64


import streamlit as st
import streamlit.components.v1 as components

import spacy
from spacy import displacy
import pandas as pd


# Remover acentuação
def pt_normalize(txt):
    return normalize("NFKD", txt).encode("ASCII", "ignore").decode("ASCII")


nlp = spacy.load("pt_core_news_lg")  # Carrega o spacy
nouns = pd.read_csv("4variation_nouns.csv").noun.tolist()  # Carrega as palavras "bad list"

st.header("Eta lele")  # Titulo da pagina
txt = st.text_area("Text to analyze")  # Area para o usuário escrever
corpus = nlp(txt)  # Processamento do spacy
response = []  # texto de sáida

# For para analisar cada palavra e popular o texto de saída
for index, word in enumerate(corpus):
    response.append(word.text)

    before = corpus[index - 1] if index > 0 else word  # Palavra anterior
    after = corpus[index + 1] if index < len(corpus) - 1 else word  # Palavra seguinte

    # Se a palavra tá na badlist -> Marca ela
    if pt_normalize(word.text.lower()) in nouns:
        response[index] = f"**{word.text}**"

    # TODO
    # if word.pos_ == "DET" and (after.dep_ in 'nsubj'):
    #     response[index] = f"**{word.text}**"

response = " ".join(response)
st.markdown(response)


def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

with st.beta_expander("More details"):
    st.write("""
            Aqui a gente consegue debugar nossa inabilidade linguística
    """)
    html = displacy.render(corpus, style="dep")  # svg object
    # Double newlines seem to mess with the rendering
    html = html.replace("\n\n", "\n")
    render_svg(html)

# svg = displacy.render(corpus, style="ent")
# output_path = Path("/sentence.svg")
# output_path.open("w", encoding="utf-8").write(svg)