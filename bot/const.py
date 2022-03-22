from utils import translate

#-------------------------------------------------------------------------------------------#
#                                     QUICK KAVIO                                           #
#-------------------------------------------------------------------------------------------#

#-----------------------------------Quick_activités-----------------------------------------#


def get_serie(partie, serie):
    variables = {
        #---------------------PARTIE 1----------------------#
        "serie_1_1": f"""
    -Photographier
    -Trouver
    -Bâtir
    -Aider
    -Planifier
    -Persuader""",
        "serie_1_2": f"""
    -Créer
    -Expliquer
    -Fabriquer
    -Renseigner
    -Financer
    -Marchander""",
        "serie_1_3": f"""
    -Illustrer
    -Chercher
    -Améliorer
    -Conseiller
    -Calculer
    -Acquérir""",
        "serie_1_4": f"""
    -Imaginer
    -Inventer
    -Construire
    -Eduquer
    -Gérer
    -Vendre""",

        #---------------------PARTIE 2-------------------------#
        "serie_2_1": f"""
    -Pratique
    -Méthodique
    -Intellectuel (le)
    -Dynamique
    -Imaginatif (ve)
    -Attentionné (e)""",
        "serie_2_2": f"""
    -Solide
    -Organisé (e)
    -Réfléchi (e)
    -Sûr (e)de soi
    -Rêveur (se)
    -Compréhensif (ve)""",
        "serie_2_3": f"""
    -Manuel (le)
    -Sérieux (se)
    -Objectif (ve)
    -Convaincant (e)
    -Créatif (ve)
    -Serviable""",
        "serie_2_4": f"""
    -Bricoleur (se)
    -Honnête
    -Observateur (trice)
    -Combatif(ve)
    -Émotif (ve)
    -Sociable""",

        #---------------PARTIE 3------------------------------#
        "serie_3_1": f"""
    -Médecin
    -Responsable marketing
    -Expert-comptable
    -Cultivateur
    -Développeur web
    -Comédien""",
        "serie_3_2": f"""
    -Dentiste
    -Directeur commercial
    -Secrétaire
    -Ingénieur BTP
    -Journaliste
    -Musicien""",
        "serie_3_3": f"""
    -Sagefemme
    -Directeur des ressources humaines
    -Avocat
    -Ingénieur agronome
    -Ingénieur informatique
    -Photographe""",
        "serie_3_4": f"""
    -Éducateur
    -Guide touristique
    -Inspecteur de police
    -Responsable de maintenance
    -Responsable de communication
    -Graphiste dessinateur"""
    }

    return variables.get(f"serie_{partie}_{serie}")


def get_quick_kavio(identifiant):
    variables = {
        #--------------------------------PARTIE 1---------------------------#
        # serie 1 de la partie 1
        "A_1_1_1": {
            "text": "Photographier",
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
            "text": "Trouver",
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
            "text":"Bâtir",
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
            "text": "Aider",
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
            "text": "Planifier",
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
            "text":"Persuader",
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
            "text": "Créer",
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
            "text": "Expliquer",
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
            "text": "Fabriquer",
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
            "text": "Renseigner",
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
            "text": "Financer",
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
            "text": "Marchander",
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
            "text": "Illustrer",
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
            "text": "Chercher",
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
            "text": "Améliorer",
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
            "text": "Conseiller",
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
            "text": "Calculer",
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
            "text": "Acquérir",
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
            "text": "Imaginer",
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
            "text": "Inventer",
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
            "text":"Construire",
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
            "text": "Eduquer",
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
            "text": "Gérer",
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
            "text": "Vendre",
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
            "text": "Pratique",
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
            "text": "Méthodique",
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
            "text": "Intellectuel (le)",
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
            "text": "Dynamique",
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
            "text": "Imaginatif (ve)",
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
            "text": "Attentionné (e)",
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
            "text": "Solide",
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
            "text": "Organisé (e)",
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
            "text": "Réfléchi (e)",
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
            "text": "Sûr (e)de soi",
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
            "text": "Rêveur (se)",
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
            "text": "Compréhensif (ve)",
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
            "text": "Manuel (le)",
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
            "text": "Sérieux (se)",
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
            "text": "Objectif (ve)",
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
            "text": "Convaincant (e)",
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
            "text": "Créatif (ve)",
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
            "text": "Serviable",
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
            "text": "Bricoleur (se)",
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
            "text": "Honnête",
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
            "text": "Observateur (trice)",
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
            "text": "Combatif(ve)",
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
            "text": "Émotif (ve)",
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
            "text": "Sociable",
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
            "text": "Médecin",
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
            "text": "Responsable marketing",
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
            "text": "Expert-comptable",
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
            "text": "Cultivateur",
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
            "text": "Développeur web",
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
            "text": "Comédien",
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
            "text": "Dentiste",
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
            "text": "Directeur commercial",
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
            "text": "Secrétaire",
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
            "text": "Ingénieur BTP",
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
            "text": "Journaliste",
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
            "text": "Musicien",
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
            "text": "Sagefemme",
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
            "text": "Directeur des ressources humaines",
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
            "text": "Avocat",
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
            "text": "Ingénieur agronome",
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
            "text": "Ingénieur informatique",
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
            "text": "Photographe",
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
            "text": "Éducateur",
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
            "text": "Guide touristique",
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
            "text": "Inspecteur de police",
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
            "text": "Responsable de maintenance",
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
            "text": "Responsable de communication",
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
            "text": "Graphiste dessinateur",
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
                                      "title": "🏠" + translate("visiter_stands",
                                                               lang).upper(),
                                      "payload": "__VISITE_STAND"},
                                     {"type": "postback",
                                     "title": "📑" + translate("fiches_metiers",
                                                              lang).upper(),
                                      "payload": "__FICHE_METIER"},
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
    return f"NOS CONTACTS:\nTel: {info[0]}\nEmail: {info[1]} \
        \n\nADRESSE: {info[3]}"


def description_emploi(description):
    return f"DESCRIPTIONS:\n\n{description}"
