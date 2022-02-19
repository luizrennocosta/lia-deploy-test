import pandas as pd

all_nouns = pd.read_csv("all_nouns.csv")

plus_4_variation_nouns = all_nouns.query("variation >= 4")

plus_4_variation_nouns.to_csv("4plus_variation_nouns.csv", index=False)
