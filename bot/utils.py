import os
import json


def translate(key, lang='fr'):
    '''
        Traduire un mot clé dans données.
    '''
    if not lang:
        # mettre une langue par defaut
        lang = 'fr'

    if not os.path.isfile("langs.json"):
        print("Attention, fichier langs.json n'existe pas")
        return key

    with open("langs.json") as fichier:
        trans = json.load(fichier)

    mot_cle = trans.get(key)

    if mot_cle:
        if mot_cle.get(lang):
            return mot_cle.get(lang)
    return key
