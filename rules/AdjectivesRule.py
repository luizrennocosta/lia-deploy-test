from rules.BaseRule import BaseRule
from functions.adjectives_with_gender import adjectives_with_gender
import pandas as pd


class AdjectivesRule(BaseRule):
    def check(self, context):
        word = context["word"]
        badwords = context["badwords"]

        if word.pos_ == 'ADJ':
            noun_related = str([t.text for t in word.children if t.pos_ == 'NOUN'][0]).lower()
            if noun_related in badwords:
                return word 

    def refactor(self, context):
        word = context["word"]
        response = context["response"]
        transformed_txt = context["transformed_txt"]
        index = context["index"]

        response[index] = (word.text + " ", "Flexiona Gênero", "#afa")
        normalized_word = self.pt_normalize(word.text.lower())
        refact_txt = adjectives_with_gender(normalized_word)
        transformed_txt[index] = refact_txt


