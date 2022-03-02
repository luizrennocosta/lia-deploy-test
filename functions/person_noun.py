from unicodedata import normalize

import pandas as pd
from pysinonimos.sinonimos import Search

df = pd.read_csv("4plus_variation_nouns.csv")


def person_noun(word):
    if df.loc[df["noun"] == word].shape[0] != 0:
        palavra_suporte = df.loc[df["noun"] == word].support

        def add_number_to_lemma(word, plural):
            return word + ("as" if plural else "a")

        def get_lemma_from_support(support_word):
            vowels = ["a", "e", "i", "o", "u"]
            return support_word[:-1] if support_word[-1] in vowels else support_word

        plural = False
        if word[-1] == "s":
            plural = True

        person = "pessoas" if plural else "pessoa"
        support_lemma = get_lemma_from_support(palavra_suporte.values[0])
        number = add_number_to_lemma(support_lemma, plural=plural)

        substitute = f"{person} {number}"

        return substitute
    else:
        return word
