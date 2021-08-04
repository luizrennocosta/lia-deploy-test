from unicodedata import normalize
from pysinonimos.sinonimos import Search
import pandas as pd

df = load_nouns()

def person_noun(word):
    if df.loc[df["noun"] == word].shape[0] != 0:
        word = df.loc[df["noun"] == word].support

        def add_number_to_lemma(word, plural):
            return word + ("as" if plural else "a") 

        def get_lemma_from_support(support_word):
            vowels = ['a', 'e', 'i', 'o', 'u']
            return word[:-1] if word[-1] in vowels else word

        plural = False
        if palavra[-1] == "s":
            plural = True

        person = "pessoas" if plural else "pessoa"
        support_lemma = get_lemma_from_support(palavra_suporte.values[0])
        number = add_number_to_lemma(support_lemma, plural=plural)
  
        substitute = f"{person} {number}"
        
        return substitute
    else: 
        return word

