from rules.BaseRule import BaseRule


class BadWordsRule(BaseRule):
    def check(self, context):
        badwords = context['badwords']
        word = context['word']
        return self.pt_normalize(word.text.lower()) in badwords

    def refactor(self, context):
        word = context['word']
        index = context['index']
        response = context['response']

        # response[index] = f"**{word.text}**"
        response[index] = (word.text + " ", "Flexiona Genero", "#afa")
