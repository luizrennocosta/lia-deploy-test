from rules.BaseRule import BaseRule


class HeSheRule(BaseRule):
    def check(self, context):
        word = context["word"]
        return (word.text.lower() == "eles") or (word.text.lower() == "elas")

    def refactor(self, context):
        before = context["before"]
        word = context["word"]
        index = context["index"]
        response = context["response"]
        transformed_txt = context["transformed_txt"]

        response[index] = (word.text + " ", "Não Neutro", "#faa")
        transformed_txt[index] = f""

        transformed_txt[index - 1] = f"**esse grupo**"
        if before.text[0].isupper():
            transformed_txt[index - 1] = f"**Esse grupo**"