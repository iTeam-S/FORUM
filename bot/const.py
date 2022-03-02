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