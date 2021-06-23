from rules.BaseRule import BaseRule


class MeaninglessDetRule(BaseRule):
    def check(self, context):
        after = context['after']
        word = context['word']
        return (word.pos_ == "DET") and (after.dep_ in 'nsubj')

    def refactor(self, context):
        word = context['word']
        index = context['index']
        response = context['response']
        transformed_txt = context['transformed_txt']

        response[index] = (word.text + " ", "Pode ser Ocultado", "#faa")
        transformed_txt[index] = f""