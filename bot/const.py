from utils import translate

#-------------------------------------------------------------------------------------------#
#                                     QUICK KAVIO                                           #
#-------------------------------------------------------------------------------------------#

#-----------------------------------Quick_activités-----------------------------------------#
def get_quick_kavio(identifiant,lang):
    variables = {
        #serie 1 de la partie 1
        "A_1_1_1":{
            "text":translate("photograhier",lang).upper(),
            "quick_rep":[
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
        "I_2_1_1":{
            "text":translate("trouver",lang).upper(),
            "quick_rep":[
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
        "R_3_1_1":{
            "text":translate("batir",lang).upper(),
            "quick_rep":[
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
        "S_4_1_1":{
            "text":translate("aider",lang).upper(),
            "quick_rep":[
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
        "C_5_1_1":{
            "text":translate("planifier",lang).upper(),
            "quick_rep":[
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
        "E_6_1_1":{
            "text":translate("persuader",lang).upper(),
            "quick_rep":[
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
        #serie 2 de la partie 1
        "A_1_1_2":{
            "text":translate("creer",lang).upper(),
            "quick_rep":[
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
        "I_2_1_2":{
            "text":translate("expliquer",lang).upper(),
            "quick_rep":[
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
        "R_3_1_2":{
            "text":translate("fabriquer",lang).upper(),
            "quick_rep":[
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
        "S_4_1_2":{
            "text":translate("renseigner",lang).upper(),
            "quick_rep":[
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
        "C_5_1_2":{
            "text":translate("financer",lang).upper(),
            "quick_rep":[
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
        "E_6_1_2":{
            "text":translate("marchander",lang).upper(),
            "quick_rep":[
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
        #serie 3 de la partie 1
        "A_1_1_3":{
            "text":translate("illustrer",lang).upper(),
            "quick_rep":[
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
        "I_2_1_3":{
            "text":translate("chercher",lang).upper(),
            "quick_rep":[
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
        "R_3_1_3":{
            "text":translate("ameliorer",lang).upper(),
            "quick_rep":[
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
        "S_4_1_3":{
            "text":translate("conseiller",lang).upper(),
            "quick_rep":[
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
        "C_5_1_3":{
            "text":translate("calculer",lang).upper(),
            "quick_rep":[
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
        "E_6_1_3":{
            "text":translate("acquerir",lang).upper(),
            "quick_rep":[
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
        #serie 4 de la partie 1
        "A_1_1_4":{
            "text":translate("imaginer",lang).upper(),
            "quick_rep":[
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
        "I_2_1_4":{
            "text":translate("iventer",lang).upper(),
            "quick_rep":[
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
        "R_3_1_4":{
            "text":translate("construire",lang).upper(),
            "quick_rep":[
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
        "S_4_1_4":{
            "text":translate("eduquer",lang).upper(),
            "quick_rep":[
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
        "C_5_1_4":{
            "text":translate("gerer",lang).upper(),
            "quick_rep":[
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
        "E_6_1_4":{
            "text":translate("vendre",lang).upper(),
            "quick_rep":[
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
    }

    

    return variables.get(identifiant)


#-------------------------------------------------------------------------------------------#
#                             FONCTIONS CONSTANTS                                           #
#-------------------------------------------------------------------------------------------#
def voir_liste_des_fiches_metiers(domaine="",lang="fr"):
    if lang and lang=="en":
        return f"Here are the lists of job descriptions available for the domain of {domaine}"

    elif lang and lang=="mg":
        return f"Ireto ary ny lisitry ny filazalazana asa azo alaina ho an'ny sehatry ny {domaine}"

    return f"Voici donc les listes des fiches métiers disponibles pour le domainde de {domaine}"

def informations_stands(info):
    return f"DESCRITIONS: \n{info[4]}\n\nNOS CONTACTS:\nTel: {info[0]}\nEmail: {info[1]} \
        \n\nADRESSE: {info[3]}"

def description_emploi(description):
    return f"DESCRIPTIONS:\n\n{description}"