from rules.BaseRule import BaseRule
import mlconjug3
import nltk
from nltk.stem.snowball import SnowballStemmer

nltk.download("punkt")


class BadWordsRule(BaseRule):
    def check(self, context):
        badwords = context["badwords"]
        word = context["word"]
        return self.pt_normalize(word.text.lower()) in badwords

    def refactor(self, context):
        def _get_infinitive_verb(word):
            """
            PT: Converte o pronome em verbo no infinitivo
            EN: GConvert the noun into infinitive verb
            """
            stemmer = SnowballStemmer("portuguese")
            stem = stemmer.stem(word)
            return word[word.index(stem) : word.index(stem) + 1 + len(stem)] + "r"

        after = context["after"]
        before = context["before"]
        word = context["word"]
        index = context["index"]
        response = context["response"]
        transformed_txt = context["transformed_txt"]

        # response[index] = f"**{word.text}**"
        response[index] = (word.text + " ", "Flexiona Genero", "#afa")
        verb = _get_infinitive_verb(str(word))
        conjugator = mlconjug3.Conjugator(language="pt")

        if after.pos_ == "AUX":
            tense = after.morph.get("Tense")
            mood = after.morph.get("Mood")
            verbform = after.morph.get("VerbForm")

            if tense == ["Past"] or tense == ["Imp"] or mood == ["Cnd"]:
                conj_verb = conjugator.conjugate(verb).conjug_info["Indicativo"][
                    "Indicativo pretérito imperfeito"
                ]["3s"]
            elif tense == ["Pres"] or verbform == ["Inf"]:
                conj_verb = conjugator.conjugate(verb).conjug_info["Indicativo"][
                    "Indicativo presente"
                ]["3s"]
            elif tense == ["Fut"]:
                conj_verb = conjugator.conjugate(verb).conjug_info["Indicativo"][
                    "Indicativo Futuro do Presente Simples"
                ]["3s"]
        else:
            conj_verb = conjugator.conjugate(verb).conjug_info["Indicativo"][
                "Indicativo presente"
            ]["3s"]

        transformed_txt[index] = f"**quem {conj_verb}**"
        if before.text[0].isupper():
            transformed_txt[index] = f"**Quem {conj_verb}**"