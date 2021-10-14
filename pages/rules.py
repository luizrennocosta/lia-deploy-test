import streamlit as st

BadWords_rule = """
    A Regra de 'Bad Words' verifica se a palavra analisada está na lista de palavras que flexiona gênero. 
    Se a verificação se confirmar, a refatoração primeiro busca por um sinônimo neutro da palavra usando a função synonyms_for_gender_nouns(). 
    Uma frase que seria neutralizada usando essa etapa de refatoração, por exemplo, é:

    "Os alunos gostam de programação" > "Estudantes gostam de programação"
    
    Caso um sinônimo neutro não seja encontrado, transfere-se a palavra original para a próxima função: who_w_indicativeVerb().
    Essa função utiliza o processo de lemmatização para identificar o radical da palavra analisada. 
    O lemma é passado para uma função que busca um verbo no infinitivo que seja próximo à palavra.
    Caso seja encontrado, substitui a palavra não neutra pelo pronome "quem" seguida da ação que caracteriza essa palavra (o verbo encontrado conjugado).
    Uma frase que seria neutralizada usando essa etapa de refatoração, por exemplo, é:

    "Os montadores chegaram" > "Quem monta chegou"

    Se mesmo assim, a palavra analisada permanecer não refatorada, transfere-se a palavra original para uma terceira função: person_noun().
    Essa função adiciona a palavra "pessoa" no devido número (plural ou singular) seguida da palavra original em concordância com a palavra pessoa.
    Uma frase que seria neutralizada usando essa etapa de refatoração, por exemplo, é:

    "Os brasileiros estão trabalhando" > "As pessoas brasileiras estão trabalhando"
    """



def app(BadWords_rule=BadWords_rule):
    st.title("Fluxo da Aplicação e Regras")
    st.header("Como LIA funciona?")
    st.write("O fluxo abaixo representa a arquitetura e módulos presentes em LIA. A seguir, cada uma das regras de neutralidade é detalhada.")
    st.image("img/LIA.jpg")
    
    with st.expander("BadWordsRule"):
        st.write(BadWords_rule)
