from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup


def next_page(n):
    if n == 1:
        url = "https://www.conjugacao.com.br/verbos-populares/"
    else:
        url = f"https://www.conjugacao.com.br/verbos-populares/{n}"

    response = urlopen(url)
    html = response.read()
    return BeautifulSoup(html, "html.parser")


if __name__ == "__main__":
    verbos = []
    for n in range(1, 207):
        soup = next_page(n)
        for node in soup.findAll("li"):
            verbos.append(node.get_text())

    df = pd.DataFrame(verbos, columns=["verbos_infinito"])
    df.to_csv("data/infinitive_verbs.csv", index=False)