from googletrans import Translator
import time

def translate_pt_to_en(word):
    """
    This function uses googletrans, a Python lib based on the official Google Translate API.
    googletrans is not recommended for projects which need stability of service translation.
    The time.sleep is a trick to avoid the too many requests (429) error. It greatly increases execution time, but as this function is supposed to be rarely used, that is not a problem right now.
    The function receives a word in Portuguese and translates to English.
    """   
    translator = Translator()
    time.sleep(2)
    translation = translator.translate(word, src='pt', dest='en').text
    return  translation