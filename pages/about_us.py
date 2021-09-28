import streamlit as st


def app():
    st.title("Sobre LIA")
    st.header("Pequenos hábitos que causam impacto")
    
    sentence = """
    LIA (Linguagem Inclusiva com Assistência) é uma ferramenta que revisa textos dando dicas de como torná-lo mais inclusivo.

    A linguagem inclusiva e neutra busca a comunicação sem exclusão ou invisibilidade de qualquer grupo, de forma respeitosa e abrangente. 

    A língua portuguesa é generalista usando o masculino para grupos mistos ou que não sabemos qual a identidade de gênero de quem falamos. Um exemplo é quando dizemos que em uma sala com mulheres, homens e pessoas não binárias usamos o termo "alunos" para se referir a todas as pessoas, invisibilizando o gênero feminino e não binário.

    Sabemos o quanto pode ser desafiador adotar uma linguagem neutra para pessoas que tem como idioma nativo a língua portuguesa e outras similares, mas temos o objetivo de construirmos uma cultura na qual nos comunicamos sem usarmos termos que trazem uma bagagem de preconceitos ou que impõe um discurso sexista e/o não-binário.

    Por isso, o time de Ciência de Dados da Loft iniciou o projeto LIA com a motivação de poder unir conhecimento técnico com causas que fortaleçam a inclusão.

    Topam construir uma comunicação inclusiva conosco?
    """
    st.write(sentence)
