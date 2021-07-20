from rules.BaseRule import BaseRule
from functions.relativePronoun_w_indicativeVerb import neutralize_noun


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
        # response[index] = f"**{word.text}**"
        response[index] = (word.text + " ", "Flexiona Genero", "#afa")

        transformed_txt[index] = neutralize_noun(context)