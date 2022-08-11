from rules.BaseRule import BaseRule
from functions.checking_person_related_word import check_lowest_common_hypernym

class MeaninglessDetRule(BaseRule):
    def check(self, context):
        after = context["after"]
        word = context["word"]
        return (
            (word.pos_ == "DET")
            and (after.pos_ in "NOUN"))
           
    def refactor(self, context):
        word = context["word"]
        after = context["after"]
        badwords = context["badwords"]

        index = context["index"]
        response = context["response"]
        transformed_txt = context["transformed_txt"]

        #Sugere remoção de artigos relacionados a substantivos que flexionam gênero
        if self.pt_normalize(after.text.lower()) in badwords:
            response[index] = (word.text + " ", "Pode ser Ocultado", "#faa")
            transformed_txt[index] = f""
        
        #Sugere remoção de artigos relacionados a substantivos que não flexionam gênero mas estão relacionados a pessoas
        if self.pt_normalize(after.text.lower()) not in badwords:
            if check_lowest_common_hypernym(after.text.lower(), support_bol=False) == True:
                response[index] = (word.text + " ", "Pode ser Ocultado", "#faa")
                transformed_txt[index] = f""

