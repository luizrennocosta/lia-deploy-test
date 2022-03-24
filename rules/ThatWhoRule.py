from rules.BaseRule import BaseRule


class ThatWhoRule(BaseRule):
    def check(self, context):
        after = context["after"]
        word = context["word"]
        return (word.text.lower() == "aqueles" or word.text.lower() == "aquele") and (after.text.lower() == "que")

    def refactor(self, context):
        after = context["after"]
        word = context["word"]
        index = context["index"]
        response = context["response"]
        transformed_txt = context["transformed_txt"]
       
        response[index] = (word.text +  " ", "Não neutro", "#fea")
        
        transformed_txt[index] = f"quem"
        if word.text[0].isupper():
            transformed_txt[index] = f"Quem"
