# https://www.speakingbrazilian.com/post/how-to-identify-the-gender-of-words
# Como regra geral, as palavras terminadas em -A são femininas, e as palavras terminadas em -O são masculinas, mas há muitas palavras com diferentes terminações.
# Palavras terminadas em -OR são masculinas e palavras terminadas em  -ORA são femininas.
# Palavras terminadas em -ANTE, -ENTE e -ISTA não variam e podem ser usadas para os dois gêneros.
# Palavras terminadas em -AGEM, -IDADE e -ÇÃO são femininas.

from unicodedata import normalize
from pysinonimos.sinonimos import Search
import pandas as pd

df = pd.read_csv("4variation_nouns.csv")

def synonyms_for_gender_nouns(word):
    if df.loc[df["noun"] == word].shape[0] != 0:
        palavra_suporte = df.loc[df["noun"] == word].support
        sinonimos = Search(palavra_suporte.values[0]).synonyms()

        substituto_list = []
        for sinonimo in sinonimos:
            if sinonimo.endswith(("ante", "ente", "ista")):
                if word[-1] == "s":
                    substituto_list.append(sinonimo + "s")
                else:
                    substituto_list.append(sinonimo)

        if len(substituto_list) > 0:
            return substituto_list[0]
    else:
        return word
