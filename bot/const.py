from utils import translate

#-------------------------------------------------------------------------------------------#
#                                     QUICK KAVIO                                           #
#-------------------------------------------------------------------------------------------#

#-----------------------------------Quick_activités-----------------------------------------#


def get_serie(partie, serie, lang):
    variables = {
        #---------------------PARTIE 1----------------------#
        "serie_1_1": f"""
    -{translate("photograhier",lang).upper()}
    -{translate("trouver",lang).upper()}
    -{translate("batir",lang).upper()}
    -{translate("aider",lang).upper()}
    -{translate("planifier",lang).upper()}
    -{translate("persuader",lang).upper()}""",
        "serie_1_2": f"""
    -{translate("creer",lang).upper()}
    -{translate("expliquer",lang).upper()}
    -{translate("fabriquer",lang).upper()}
    -{translate("renseigner",lang).upper()}
    -{translate("financer",lang).upper()}
    -{translate("marchander",lang).upper()}""",
        "serie_1_3": f"""
    -{translate("illustrer",lang).upper()}
    -{translate("chercher",lang).upper()}
    -{translate("ameliorer",lang).upper()}
    -{translate("conseiller",lang).upper()}
    -{translate("calculer",lang).upper()}
    -{translate("acquerir",lang).upper()}""",
        "serie_1_4": f"""
    -{translate("imaginer",lang).upper()}
    -{translate("inventer",lang).upper()}
    -{translate("construire",lang).upper()}
    -{translate("eduquer",lang).upper()}
    -{translate("gerer",lang).upper()}
    -{translate("vendre",lang).upper()}""",

        #---------------------PARTIE 2-------------------------#
        "serie_2_1": f"""
    -{translate("pratique",lang).upper()}
    -{translate("methodique",lang).upper()}
    -{translate("intelectuel",lang).upper()}
    -{translate("dynamic",lang).upper()}
    -{translate("imaginatif",lang).upper()}
    -{translate("attentionne",lang).upper()}""",
        "serie_2_2": f"""
    -{translate("solide",lang).upper()}
    -{translate("organiser",lang).upper()}
    -{translate("reflechi",lang).upper()}
    -{translate("sur",lang).upper()}
    -{translate("reveur",lang).upper()}
    -{translate("comprehensif",lang).upper()}""",
        "serie_2_3": f"""
    -{translate("manuel",lang).upper()}
    -{translate("serieux",lang).upper()}
    -{translate("objectif",lang).upper()}
    -{translate("convaincant",lang).upper()}
    -{translate("creatif",lang).upper()}
    -{translate("serviable",lang).upper()}""",
        "serie_2_4": f"""
    -{translate("bricoleur",lang).upper()}
    -{translate("honnete",lang).upper()}
    -{translate("observeur",lang).upper()}
    -{translate("combatif",lang).upper()}
    -{translate("emotif",lang).upper()}
    -{translate("sociable",lang).upper()}""",

        #---------------PARTIE 3------------------------------#
        "serie_3_1": f"""
    -{translate("medcin",lang).upper()}
    -{translate("marketing",lang).upper()}
    -{translate("compta",lang).upper()}
    -{translate("cultivateur",lang).upper()}
    -{translate("devweb",lang).upper()}
    -{translate("commedien",lang).upper()}""",
        "serie_3_2": f"""
    -{translate("dentiste",lang).upper()}
    -{translate("dircommercial",lang).upper()}
    -{translate("secretaire",lang).upper()}
    -{translate("btp",lang).upper()}
    -{translate("journalist",lang).upper()}
    -{translate("musicien",lang).upper()}""",
        "serie_3_3": f"""
    -{translate("sagefemme",lang).upper()}
    -{translate("drh",lang).upper()}
    -{translate("avocat",lang).upper()}
    -{translate("agro",lang).upper()}
    -{translate("ingenieur_info",lang).upper()}
    -{translate("photographe",lang).upper()}""",
        "serie_3_4": f"""
    -{translate("educateur",lang).upper()}
    -{translate("guide",lang).upper()}
    -{translate("police",lang).upper()}
    -{translate("maintenance",lang).upper()}
    -{translate("com",lang).upper()}
    -{translate("dessinateur",lang).upper()}"""
    }

    return variables.get(f"serie_{partie}_{serie}")


def get_quick_kavio(identifiant, lang):
    variables = {
        #--------------------------------PARTIE 1---------------------------#
        # serie 1 de la partie 1
        "A_1_1_1": {
            "text": translate("photograhier", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_A_1_1_1_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_A_1_1_1_0"
                }
            ]
        },
        "I_2_1_1": {
            "text": translate("trouver", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_I_2_1_1_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_I_2_1_1_0"
                }
            ]
        },
        "R_3_1_1": {
            "text": translate("batir", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_R_3_1_1_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_R_3_1_1_0"
                }
            ]
        },
        "S_4_1_1": {
            "text": translate("aider", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_S_4_1_1_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_S_4_1_1_0"
                }
            ]
        },
        "C_5_1_1": {
            "text": translate("planifier", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_C_5_1_1_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_C_5_1_1_0"
                }
            ]
        },
        "E_6_1_1": {
            "text": translate("persuader", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_E_6_1_1_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_E_6_1_1_0"
                }
            ]
        },
        # serie 2 de la partie 1
        "A_1_1_2": {
            "text": translate("creer", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_A_1_1_2_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_A_1_1_2_0"
                }
            ]
        },
        "I_2_1_2": {
            "text": translate("expliquer", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_I_2_1_2_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_I_2_1_2_0"
                }
            ]
        },
        "R_3_1_2": {
            "text": translate("fabriquer", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_R_3_1_2_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_R_3_1_2_0"
                }
            ]
        },
        "S_4_1_2": {
            "text": translate("renseigner", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_S_4_1_2_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_S_4_1_2_0"
                }
            ]
        },
        "C_5_1_2": {
            "text": translate("financer", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_C_5_1_2_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_C_5_1_2_0"
                }
            ]
        },
        "E_6_1_2": {
            "text": translate("marchander", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_E_6_1_2_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_E_6_1_2_0"
                }
            ]
        },
        # serie 3 de la partie 1
        "A_1_1_3": {
            "text": translate("illustrer", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_A_1_1_3_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_A_1_1_3_0"
                }
            ]
        },
        "I_2_1_3": {
            "text": translate("chercher", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_I_2_1_3_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_I_2_1_3_0"
                }
            ]
        },
        "R_3_1_3": {
            "text": translate("ameliorer", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_R_3_1_3_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_R_3_1_3_0"
                }
            ]
        },
        "S_4_1_3": {
            "text": translate("conseiller", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_S_4_1_3_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_S_4_1_3_0"
                }
            ]
        },
        "C_5_1_3": {
            "text": translate("calculer", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_C_5_1_3_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_C_5_1_3_0"
                }
            ]
        },
        "E_6_1_3": {
            "text": translate("acquerir", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_E_6_1_3_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_E_6_1_3_0"
                }
            ]
        },
        # serie 4 de la partie 1
        "A_1_1_4": {
            "text": translate("imaginer", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_A_1_1_4_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_A_1_1_4_0"
                }
            ]
        },
        "I_2_1_4": {
            "text": translate("inventer", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_I_2_1_4_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_I_2_1_4_0"
                }
            ]
        },
        "R_3_1_4": {
            "text": translate("construire", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_R_3_1_4_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_R_3_1_4_0"
                }
            ]
        },
        "S_4_1_4": {
            "text": translate("eduquer", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_S_4_1_4_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_S_4_1_4_0"
                }
            ]
        },
        "C_5_1_4": {
            "text": translate("gerer", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_C_5_1_4_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_C_5_1_4_0"
                }
            ]
        },
        "E_6_1_4": {
            "text": translate("vendre", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "👍",
                    "payload": "--**KAVIO_E_6_1_4_1"
                },
                {
                    "content_type": "text",
                    "title": "👎",
                    "payload": "--**KAVIO_E_6_1_4_0"
                }
            ]
        },

        #--------------------PARTIE 2(QUALITÉS)-------------------------------------#
        # serie 1 de la partie 2
        "A_1_2_1": {
            "text": translate("pratique", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_A_1_2_1_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_A_1_2_1_0"
                }
            ]
        },
        "I_2_2_1": {
            "text": translate("methodique", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_I_2_2_1_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_I_2_2_1_0"
                }
            ]
        },
        "R_3_2_1": {
            "text": translate("intelectuel", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_R_3_2_1_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_R_3_2_1_0"
                }
            ]
        },
        "S_4_2_1": {
            "text": translate("dynamic", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_S_4_2_1_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_S_4_2_1_0"
                }
            ]
        },
        "C_5_2_1": {
            "text": translate("imaginatif", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_C_5_2_1_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_C_5_2_1_0"
                }
            ]
        },
        "E_6_2_1": {
            "text": translate("attentionne", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_E_6_2_1_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_E_6_2_1_0"
                }
            ]
        },
        # serie 2 de la partie 2
        "A_1_2_2": {
            "text": translate("solide", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_A_1_2_2_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_A_1_2_2_0"
                }
            ]
        },
        "I_2_2_2": {
            "text": translate("organiser", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_I_2_2_2_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_I_2_2_2_0"
                }
            ]
        },
        "R_3_2_2": {
            "text": translate("reflechi", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_R_3_2_2_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_R_3_2_2_0"
                }
            ]
        },
        "S_4_2_2": {
            "text": translate("sur", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_S_4_2_2_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_S_4_2_2_0"
                }
            ]
        },
        "C_5_2_2": {
            "text": translate("reveur", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_C_5_2_2_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_C_5_2_2_0"
                }
            ]
        },
        "E_6_2_2": {
            "text": translate("comprehensif", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_E_6_2_2_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_E_6_2_2_0"
                }
            ]
        },
        # serie 3 de la partie 2
        "A_1_2_3": {
            "text": translate("manuel", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_A_1_2_3_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_A_1_2_3_0"
                }
            ]
        },
        "I_2_2_3": {
            "text": translate("serieux", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_I_2_2_3_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_I_2_2_3_0"
                }
            ]
        },
        "R_3_2_3": {
            "text": translate("objectif", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_R_3_2_3_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_R_3_2_3_0"
                }
            ]
        },
        "S_4_2_3": {
            "text": translate("convaincant", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_S_4_2_3_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_S_4_2_3_0"
                }
            ]
        },
        "C_5_2_3": {
            "text": translate("creatif", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_C_5_2_3_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_C_5_2_3_0"
                }
            ]
        },
        "E_6_2_3": {
            "text": translate("serviable", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_E_6_2_3_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_E_6_2_3_0"
                }
            ]
        },
        # serie 4 de la partie 2
        "A_1_2_4": {
            "text": translate("bricoleur", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_A_1_2_4_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_A_1_2_4_0"
                }
            ]
        },
        "I_2_2_4": {
            "text": translate("honnete", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_I_2_2_4_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_I_2_2_4_0"
                }
            ]
        },
        "R_3_2_4": {
            "text": translate("observeur", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_R_3_2_4_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_R_3_2_4_0"
                }
            ]
        },
        "S_4_2_4": {
            "text": translate("combatif", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_S_4_2_4_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_S_4_2_4_0"
                }
            ]
        },
        "C_5_2_4": {
            "text": translate("emotif", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_C_5_2_4_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_C_5_2_4_0"
                }
            ]
        },
        "E_6_2_4": {
            "text": translate("sociable", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "😍",
                    "payload": "--**KAVIO_E_6_2_4_1"
                },
                {
                    "content_type": "text",
                    "title": "😉",
                    "payload": "--**KAVIO_E_6_2_4_0"
                }
            ]
        },

        #--------------------PARTIE 3(PROFESSIONS)-------------------------------------#
        # serie 1 de la partie 3
        "A_1_3_1": {
            "text": translate("medcin", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_A_1_3_1_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_A_1_3_1_0"
                }
            ]
        },
        "I_2_3_1": {
            "text": translate("marketing", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_I_2_3_1_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_I_2_3_1_0"
                }
            ]
        },
        "R_3_3_1": {
            "text": translate("compta", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_R_3_3_1_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_R_3_3_1_0"
                }
            ]
        },
        "S_4_3_1": {
            "text": translate("cultivateur", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_S_4_3_1_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_S_4_3_1_0"
                }
            ]
        },
        "C_5_3_1": {
            "text": translate("devweb", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_C_5_3_1_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_C_5_3_1_0"
                }
            ]
        },
        "E_6_3_1": {
            "text": translate("commedien", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_E_6_3_1_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_E_6_3_1_0"
                }
            ]
        },
        # serie 2 de la partie 3
        "A_1_3_2": {
            "text": translate("dentiste", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_A_1_3_2_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_A_1_3_2_0"
                }
            ]
        },
        "I_2_3_2": {
            "text": translate("dircommercial", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_I_2_3_2_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_I_2_3_2_0"
                }
            ]
        },
        "R_3_3_2": {
            "text": translate("secretaire", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_R_3_3_2_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_R_3_3_2_0"
                }
            ]
        },
        "S_4_3_2": {
            "text": translate("btp", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_S_4_3_2_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_S_4_3_2_0"
                }
            ]
        },
        "C_5_3_2": {
            "text": translate("journalist", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_C_5_3_2_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_C_5_3_2_0"
                }
            ]
        },
        "E_6_3_2": {
            "text": translate("musicien", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_E_6_3_2_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_E_6_3_2_0"
                }
            ]
        },
        # serie 3 de la partie 3
        "A_1_3_3": {
            "text": translate("sagefemme", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_A_1_3_3_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_A_1_3_3_0"
                }
            ]
        },
        "I_2_3_3": {
            "text": translate("drh", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_I_2_3_3_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_I_2_3_3_0"
                }
            ]
        },
        "R_3_3_3": {
            "text": translate("avocat", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_R_3_3_3_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_R_3_3_3_0"
                }
            ]
        },
        "S_4_3_3": {
            "text": translate("agro", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_S_4_3_3_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_S_4_3_3_0"
                }
            ]
        },
        "C_5_3_3": {
            "text": translate("ingenieur_info", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_C_5_3_3_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_C_5_3_3_0"
                }
            ]
        },
        "E_6_3_3": {
            "text": translate("photographe", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_E_6_3_3_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_E_6_3_3_0"
                }
            ]
        },
        # serie 4 de la partie 4
        "A_1_3_4": {
            "text": translate("educateur", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_A_1_3_4_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_A_1_3_4_0"
                }
            ]
        },
        "I_2_3_4": {
            "text": translate("guide", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_I_2_3_4_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_I_2_3_4_0"
                }
            ]
        },
        "R_3_3_4": {
            "text": translate("police", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_R_3_3_4_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_R_3_3_4_0"
                }
            ]
        },
        "S_4_3_4": {
            "text": translate("maintenance", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_S_4_3_4_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_S_4_3_4_0"
                }
            ]
        },
        "C_5_3_4": {
            "text": translate("com", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_C_5_3_4_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_C_5_3_4_0"
                }
            ]
        },
        "E_6_3_4": {
            "text": translate("dessinateur", lang).upper(),
            "quick_rep": [
                {
                    "content_type": "text",
                    "title": "🤩",
                    "payload": "--**KAVIO_E_6_3_4_1"
                },
                {
                    "content_type": "text",
                    "title": "😔",
                    "payload": "--**KAVIO_E_6_3_4_0"
                }
            ]
        },
    }

    return variables.get(identifiant)


def persistent_menu(types, lang):
    if types == "PRINCIPALE":
        return [{"locale": "default",
                 "composer_input_disabled": False,
                 "call_to_actions": [{"type": "postback",
                                      "title": "📑" + translate("fiches_metiers",
                                                               lang).upper(),
                                      "payload": "__FICHE_METIER"},
                                     {"type": "postback",
                                      "title": "🏠" + translate("visiter_stands",
                                                               lang).upper(),
                                      "payload": "__VISITE_STAND"},
                                     {"type": "postback",
                                      "title": "🔶" + translate("kavio",
                                                               lang).upper(),
                                      "payload": "__TEST_KAVIO"}]}]


#-------------------------------------------------------------------------------------------#
#                             FONCTIONS ET VARIABLES CONSTANTS                              #
#-------------------------------------------------------------------------------------------#
def retoure(types, lang, *args):
    if types == "FICHES_METIERS":
        return {
            "content_type": "text",
            "title": "⏪" + translate("retoure", lang),
            "payload": "__RETOURE_FICHEMETIER",
        }

    elif types == "FICHES_METIERS_RECHERCHE":
        return {
            "content_type": "text",
            "title": "⏪" + translate("retoure", lang),
            "payload": "__RETOURE_FICHEMETIER_RECHERCHE",
        }

    elif types == "STAND_DEBUT":
        return {
            "content_type": "text",
            "title": "⏪" + translate("retoure", lang),
            "payload": "__RETOURNE_STAND_DEBUT",
        }

    elif types == "STAND_EMPLOI":
        for argument in args:
            id_stand = argument

        return {
            "content_type": "text",
            "title": "⏪" + translate("retoure", lang),
            "payload": f"__RETOURNE_STAND_EMPLOI {id_stand}",
        }


def resultat_metier(interet, lang):
    interet_global = []
    categ_global = []
    metier = []

    for k in range(len(interet)):
        interet_global.append(
            translate(interet[k], lang)
        )
        categ_global.append(
            translate(interet[k] + "_4", lang)
        )
        metier.append(
            translate(f"{interet[k]}_3", lang)
        )

    categ = "\n\n".join(categ_global)
    met = "\n".join(metier)

    if lang == "fr":
        reponse1 = f"D'apres ce long test que vous avez réaliser, Voici donc vos resultats:\n Nous avons le plaisir de vous annoncer vos intérêts globaux.\
Vous êtes une personne {' et '.join(interet_global) if len(interet_global)<3  else ' , '.join(interet_global[0:-1])+' et '+interet_global[-1]}"
        reponse2 = f'ALORS, CI-DESSOUS UNE PETITE DESCRIPTION POUR CELA:\n\n{categ}'
        reponse3 = f"\n\nVOICI DONC LES METIERS QUI TE CORRESPONDENT\n\n{met}"
        return reponse1, reponse2, reponse3

    elif lang == "en":
        reponse1 = f"According to this long test that you have carried out, here are your results:\nWe are pleased to announce your global interests. \
You are a person {' and '.join(interet_global) if len(interet_global)<3  else ' , '.join(interet_global[0:-1])+' and '+interet_global[-1]}"
        reponse2 = f"\n\nSO THAT BELOW A LITTLE DESCRIPTION FOR THIS:\n\n{categ}"
        reponse3 = f"\n\nSO HERE ARE THE PROFESSIONS THAT MATCH YOU:\n\n{met}"
        return reponse1, reponse2, reponse3

    else:
        reponse1 = f"Rehefa nodinidinihaana sy nalalinina ary ny andrana izay nataona dia azo lazaina ary fa \
{' sy '.join(interet_global) if len(interet_global)<3  else ' , '.join(interet_global[0:-1])+' ary '+interet_global[-1]} ny sehatra metimety aminao kokoa"
        reponse2 = f"KA TOY IZAO ARY IZANY:\n\n{' '.join(categ)}"
        reponse3 = f"KA NOHO IZANY ARY DIA IRETO AVY NY ASA MIFANARAKA AMINAO:\n\n{' '.join(met)}"
        return reponse1, reponse2, reponse3


def voir_liste_des_fiches_metiers(domaine="", lang="fr"):
    if lang and lang == "en":
        return f"Here are the lists of job descriptions available for the domain of {domaine}"

    elif lang and lang == "mg":
        return f"Ireto ary ny lisitry ny filazalazana asa azo alaina ho an'ny sehatry ny {domaine}"

    return f"Voici donc les listes des fiches métiers disponibles pour le domainde de {domaine}"


def informations_stands(info):
    return f"DESCRITIONS: \n{info[4]}\n\nNOS CONTACTS:\nTel: {info[0]}\nEmail: {info[1]} \
        \n\nADRESSE: {info[3]}"


def description_emploi(description):
    return f"DESCRIPTIONS:\n\n{description}"
