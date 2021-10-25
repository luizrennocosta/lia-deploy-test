from unicodedata import normalize
import pandas as pd
import requests
from pandas import json_normalize
from Levenshtein import ratio

def adjectives_with_gender(word):

    #procura sinonimos
    url = 'https://significado.herokuapp.com/synonyms/'+word
    response = requests.get(url)
    synonyms_list = response.json()

    substituto=[]
    for i in synonyms_list:
        if i.endswith(('ante', 'ente', 'ista', 'antes', 'entes','istas', 'e', 'es', 'l', 'ais', 'm', 'ar', 'ares' 'z', 'zes')) :
            if ratio(word, i) <= 0.4:
                substituto.append(i) 

        if bool(substituto) == True:
            break

    if bool(substituto) == False:

        #procura significado
        url = 'https://significado.herokuapp.com/'+word
        response = requests.get(url)
        response_dict = response.json()
        df = pd.json_normalize(response_dict)
        substituto.append(df.meanings[0][0])        
    
    return substituto[0]       
    