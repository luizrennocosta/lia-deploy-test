from rules.BaseRule import BaseRule
from functions.adjectives_with_gender import adjectives_with_gender
import pandas as pd


class AdjectivesRule(BaseRule):
    def check(self, context):
        word = context["word"]
        before = context["before"]
        after = context["after"]
        badwords = context["badwords"]
        before2 = context["before2"]

        if word.pos_ == 'ADJ':
            if word.dep_ == 'amod':
                if after.pos_ == 'NOUN':
                    noun_related = after.text  
                elif before.pos_ == 'NOUN':
                    noun_related = before.text
                elif before.pos_ == 'ADP' and before2.pos_ == 'NOUN':
                    noun_related = before2.text
                else: noun_related = "não identificada" 
            elif word.dep_ == 'ROOT':
                noun_related = str([t.text for t in word.children if (t.pos_ == 'NOUN' or t.pos_ == 'PRON')][0]).lower()
            else:
                noun_related = "não identificada"
            if noun_related in badwords:
                return word 

    def refactor(self, context):
        word = context["word"]
        response = context["response"]
        transformed_txt = context["transformed_txt"]
        index = context["index"]

        response[index] = (word.text + " ", "Flexiona Gênero", "#fea")
        normalized_word = self.pt_normalize(word.text.lower())
        refact_txt = adjectives_with_gender(normalized_word)
        transformed_txt[index] = refact_txt


