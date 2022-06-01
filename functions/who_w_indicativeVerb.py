import mlconjug3
import pandas as pd
from Levenshtein import ratio


def who_w_indicativeVerb(context, df_words_freq):
    def _get_infinitive_verb(word, verbs):
        metric = 0
        for candidate in verbs:
            new_metric = ratio(word, candidate)
            if new_metric > metric:
                metric = new_metric
                predicted_word = candidate
        if metric >= 0.75:
            return predicted_word
        else:
            return word

    verbs = pd.read_csv("data/infinitive_verbs.csv")["verbos_infinito"].tolist()
    after = context["after"]
    word = context["word"]

    lemma = word.lemma_
    verb = _get_infinitive_verb(lemma, verbs)

    if word.text != verb:
        try:
            conjugator = mlconjug3.Conjugator(language="pt")

            if after.pos_ == "AUX":
                tense = after.morph.get("Tense")
                mood = after.morph.get("Mood")
                verbform = after.morph.get("VerbForm")

                if tense == ["Past"] or tense == ["Imp"] or mood == ["Cnd"]:
                    conj_verb = conjugator.conjugate(verb).conjug_info["Indicativo"]["Indicativo pretérito imperfeito"][
                        "3s"
                    ]
                elif tense == ["Pres"] or verbform == ["Inf"]:
                    conj_verb = conjugator.conjugate(verb).conjug_info["Indicativo"]["Indicativo presente"]["3s"]
                elif tense == ["Fut"]:
                    conj_verb = conjugator.conjugate(verb).conjug_info["Indicativo"][
                        "Indicativo Futuro do Presente Simples"
                    ]["3s"]
            else:
                conj_verb = conjugator.conjugate(verb).conjug_info["Indicativo"]["Indicativo presente"]["3s"]


            
            # verificando se verbo conjugado tem score de frequencia maior ou igual a threshold
            df_freq_verb = df_words_freq.query(' words == @conj_verb')
            df_freq_verb = df_freq_verb.query(' percentil >= 0.7')
            if df_freq_verb.shape[0]>0:
                refact_txt = f"quem {conj_verb}"
                return refact_txt
            else:
                return word.text
        except:
            return word.text
    elif word.text == verb:
        return word.text
