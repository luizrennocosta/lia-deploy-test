import pandas as pd
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet as wn
from googletrans import Translator
import time

def translate_to_english(word):
    """
    This function uses googletrans, a Python lib based on the official Goggle Translate API.
    googletrans is not recommended for projects which need stability of service translation.
    The time.sleep is a trick to avoid the too many requests (429) error. It greatly increases execution time, but as this function is supposed to be rarely used, that is not a problem right now.
    The function receives a word in Portuguese and translates to English.
    """   
    translator = Translator()
    time.sleep(2)
    translation = translator.translate(word, src='pt', dest='en').text
    return  translation

def check_lowest_common_hypernym(row):
    """
    This function uses wordnet synonyms sets to define a certain word and the method lowest_common_hypernyms to find out
    if the word "person" is the most common "ancestor" word between person itself and the bad word checked. 
    Thus, it is possible to check if a bad word is related to human beings.
    """
    word_to_check = row.support
    try:
        check = wn.synset('person.n.01') in wn.synset(f'{translate_to_english(word_to_check)}.n.01').lowest_common_hypernyms(wn.synset('person.n.01'))
    except:
        check = 'Lemma não encontrado'
    return check

def main():
    bad_words_df = pd.read_csv("4plus_variation_nouns.csv")
    print(bad_words_df)

    bad_words_df['is_human_related'] = bad_words_df.apply(lambda row: check_lowest_common_hypernym(row), axis=1)
    print(bad_words_df)

    human_related_trues = (bad_words_df.is_human_related == True)
    bad_words_df_true = bad_words_df[human_related_trues]
    print(bad_words_df_true)

    bad_words_df_true.to_csv("4plus_variation_nouns_human_related.csv", index=False)

if __name__ == "__main__":
    main()