import numpy as np
import pandas as pd
import re
from collections import Counter

def open_corpusbrasileiro_txt(fname):
    with open(fname) as f:
        lines = f.readlines()

    words = []
    freq = []

    for row in lines[1:]:
        words.append(row.strip('\n').split('\t')[0])
        freq.append(row.strip('\n').split('\t')[1])
    
    df = pd.DataFrame({'words': words, 'freq': freq})
    df = df[df.words.notnull()]
    df['words'] = df.words.str.lower()
    df['freq'] = df['freq'].astype(int)
    return df

def word_count_folha_txt(fname):
    with open(fname) as f:
        corpus = f.read()
        transformed_corpus = re.sub('<[^>]+>', '', corpus)
        transformed_corpus = transformed_corpus.replace(',', '')
        transformed_corpus = transformed_corpus.replace('(', '')
        transformed_corpus = transformed_corpus.replace(')', '')
        counter_words =  Counter(transformed_corpus.split())
        df = pd.DataFrame.from_dict(counter_words, orient='index').reset_index()
        df.columns = ['words', 'freq']
        df['words'] = df.words.str.lower()
        df['freq'] = df['freq'].astype(int)
        return df
    


def main():
    df_folha = word_count_folha_txt('data/folha.txt')
    df_puc = open_corpusbrasileiro_txt('data/freq_corpus.txt')
    
    df = pd.concat([df_folha, df_puc])
    
    df = df.groupby('words').sum().reset_index()
    df = df[df.words.str.len()>1]
    df['percentil'] = pd.qcut(df['freq'], 750, duplicates='drop', labels=np.linspace(0.1,1,100))
    df['percentil'] = df['percentil'].astype(float)
    df.sort_values(['freq'], ascending=False, inplace=True)
    df.to_csv('data/words_frequency.csv', index = False)

if __name__ == "__main__":
    main()