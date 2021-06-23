from rules.BaseRule import BaseRule


class ThatWhoRule(BaseRule):
    def check(self, context):
        before = context['before']
        word = context['word']
        return (word.text.lower() == "que") and (before.text.lower() == "aquele")

    def refactor(self, context):
        before = context['before']
        word = context['word']
        index = context['index']
        response = context['response']
        transformed_txt = context['transformed_txt']

        #response[index] = f"**{word.text}**"
        #response[index - 1] = f"**{before.text}**"
        response[index] = (word.text + " ", "Redivo Hates this too", "#fea")
        response[index - 1] = (before.text + " ", "Redivo Hates this", "#fea")
        transformed_txt[index] = f""

        transformed_txt[index - 1] = f"**quem**"
        if before.text[0].isupper():
            transformed_txt[index - 1] = f"**Quem**"