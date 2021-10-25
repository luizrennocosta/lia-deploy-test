from rules.BaseRule import BaseRule
from functions.adjectives_with_gender import adjectives_with_gender

class AdjectivesRule(BaseRule):
    def check(self, context):
        after = context["after"]
        word = context["word"]
        before = context["before"]
        badwords = context["badwords"]
        return ((word.pos_ == "ADJ") and ((after.pos_ in "NOUN" and after.text.lower() in badwords) or (before.pos_ in "NOUN" and before.text.lower() in badwords)))

    def refactor(self, context):
        word = context["word"]
        response = context["response"]
        transformed_txt = context["transformed_txt"]
        index = context["index"]

        response[index] = (word.text + " ", "Flexiona Gênero", "#afa")
        normalized_word = self.pt_normalize(word.text.lower())
        refact_txt = adjectives_with_gender(normalized_word)
        transformed_txt[index] = refact_txt


