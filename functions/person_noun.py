from unicodedata import normalize
from pysinonimos.sinonimos import Search
import pandas as pd

df = pd.read_csv("4variation_nouns.csv")


def person_noun(palavra):
    # palavra = normalize("NFKD", word).encode("ASCII", "ignore").decode("ASCII").lower()

    if df.loc[df["noun"] == palavra].shape[0] != 0:
        palavra_suporte = df.loc[df["noun"] == palavra].support

        if palavra[-1] == "s":
            substituto = "pessoas " + palavra_suporte.values[0][:-1] + "as"
        else:
            substituto = "pessoa " + palavra_suporte.values[0][:-1] + "a"

        return substituto
    else:
        return palavra
