import mlconjug3
import nltk
from nltk.stem.snowball import SnowballStemmer

nltk.download("punkt")


def neutralize_noun(context):
    def _get_infinitive_verb(word):
        """
        PT: Converte o pronome em verbo no infinitivo
        EN: Convert the noun into infinitive verb
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

    refact_txt = f"**quem {conj_verb}**"
    if before.text[0].isupper():
        refact_txt = f"**Quem {conj_verb}**"
    return refact_txt
