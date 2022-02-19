import streamlit as st

badwords_rule = """
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
    Essa função adiciona a palavra "pessoa" no devido número (plural ou singular) seguida da palavra original em concordância com a palavra "pessoa".
    Uma frase que seria neutralizada usando essa etapa de refatoração, por exemplo, é:

    "Os brasileiros estão trabalhando" > "As pessoas brasileiras estão trabalhando"
    """

meaninglessdet_rule = """
    A Regra de 'Meaningless Det' verifica se a palavra analisada é um artigo e a palavra posterior é um substantivo.
    Se a verificação se confirmar, a refatoração sugere remover o artigo.
    Uma frase que seria neutralizada usando essa regra, por exemplo, é:

    "Buscamos tratar os clientes bem" > "Buscamos tratar clientes bem"
    """

thatwho_rule = """
    A Regra de 'That Who' verifica se a palavra analisada é "que" e a palavra anterior é "aquele", sinalizando para a existência da expressão "aquele que" na frase.
    Se a verificação se confirmar, a refatoração substitui a expressão "aquele que" por "quem". 
    Uma frase que seria neutralizada usando essa regra, por exemplo, é:

    "Aquele que sorri" > "Quem sorri"
    """

thisgroup_rule = """
    A Regra de 'ThisGroupRule' verifica se a palavra analisada é "eles".
    Se a verificação se confirmar, a refatoração sugere substituição de "eles" por "o grupo".

    "Eles chegaram cedo" > "O grupo chegou cedo"
    """

def app():
    st.title("Fluxo da Aplicação e Regras")
    st.header("Como LIA funciona?")
    st.write("O fluxo abaixo representa a arquitetura e módulos presentes em LIA. A seguir, cada uma das regras de neutralidade é detalhada.")
    st.image("img/LIA.jpg")
    
    with st.expander("BadWordsRule"):
        st.write(badwords_rule)
    
    with st.expander("MeaninglessDetRule"):
        st.write(meaninglessdet_rule)

    with st.expander("ThatWhoRule"):
        st.write(thatwho_rule)
    
    with st.expander("ThisGroupRule"):
        st.write(thisgroup_rule)
