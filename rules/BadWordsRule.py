from functions.person_noun import person_noun
from functions.synonyms_for_gender_nouns import synonyms_for_gender_nouns
from functions.who_w_indicativeVerb import who_w_indicativeVerb
from rules.BaseRule import BaseRule


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

        response[index] = (word.text + " ", "Flexiona Genero", "#fea")
        normalized_word = self.pt_normalize(word.text.lower())
        refact_txt = synonyms_for_gender_nouns(normalized_word)
        transformed_txt[index] = refact_txt

        if refact_txt != word.text:
            transformed_txt[index] = refact_txt
        else:
            refact_txt = who_w_indicativeVerb(context)
            if refact_txt != word.text:
                transformed_txt[index] = refact_txt
            else:
                transformed_txt[index] = person_noun(normalized_word)
