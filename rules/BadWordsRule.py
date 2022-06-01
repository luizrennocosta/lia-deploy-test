from functions.person_noun import person_noun
from functions.synonyms_for_gender_nouns import synonyms_for_gender_nouns
from functions.who_w_indicativeVerb import who_w_indicativeVerb
from rules.BaseRule import BaseRule

import pandas as pd

class BadWordsRule(BaseRule):
    def check(self, context):
        badwords = context["badwords"]
        word = context["word"]
        return self.pt_normalize(word.text.lower()) in badwords

    def refactor(self, context):
        word = context["word"]
        response = context["response"]
        transformed_txt = context["transformed_txt"]
        index = context["index"]
        df = pd.read_csv("4plus_variation_nouns.csv")
        df_words_freq = pd.read_csv("data/words_frequency.csv")

        response[index] = (word.text + " ", "Flexiona Genero", "#fea")
        normalized_word = self.pt_normalize(word.text.lower())
        refact_txt_synonums = synonyms_for_gender_nouns(df, df_words_freq, word, normalized_word)
        refact_txt_indicativeVerb = who_w_indicativeVerb(context, df_words_freq)
        refact_txt_person = person_noun(df, normalized_word) 

        transformed_txt[index] = ''
        if refact_txt_synonums != word.text:
            transformed_txt[index] = refact_txt_synonums
        if refact_txt_indicativeVerb != word.text:
            if transformed_txt[index] == '':
                transformed_txt[index] = refact_txt_indicativeVerb
            else:
                transformed_txt[index] = transformed_txt[index] + ', ' + refact_txt_indicativeVerb
        if refact_txt_person != " ":
            if transformed_txt[index] == '':
                    transformed_txt[index] = refact_txt_person
            else:
                transformed_txt[index] = transformed_txt[index] + ', ' + refact_txt_person
