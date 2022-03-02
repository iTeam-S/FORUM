#-------------------------------------------------------------------------------------------#
#                             VARIABLES CONSTANTS                                           #
#-------------------------------------------------------------------------------------------#
salutation = "Bonjour, Bienvenue au FORUM 2022 du programme SESAME"

nom_de_domaine_rechercher = "Tapez alors le nom de metier que vous souhaitez obtenir de \
    fiche metier\n\nExemple : Developer"

nom_de_domaine_rechercher_pour_les_stands = "Tapez alors le nom de domaine que vous souhaitez \
    obtenir des stands\n\nExemple : Informatique, Multimedia, Medicine, Ressources Humaines"
    
donner_des_listes_du_stand = "Voici donc les listes du stand disponibles"

resultat_de_recherche = "Voici donc les fruits de votre recherche"

resultat_de_recherche_vide = "Pour le moments, il n'y a pas du fiche metier correspondant à votre \
recherche\n\nOr vous pouvez maintenant même choisir encore les deux propositions ci-dessous en cherchant \
à nouveau"

resultat_de_recherche_stand_vide = "Pour le moments, il n'y a pas de stand correspondant à votre \
    recherche\n\nOr vous pouvez maintenant même choisir encore les deux propositions ci-dessous en cherchant \
à nouveau"

exemple_de_nom_de_stand_a_cherchher = "Entrer le nom du stand que vous voulez rechercher \
    \n\nExemple: Bfv,..."
    
pas_video = "Pour le moment, Ce stand n'a pas de video de présentation"
    
presentation_video = "Voici donc notre video de presentation\
    Veuillez patienter un peu pour le chargement ⏳⏳⏳\n\n"

site_web = "Voici notre lien de site web:"

galerie = "Voici donc nos differents galeries:"

pas_emploi = "Pour le moment, il n'y a pas d'offre d'emploi pour ce stand"

emploi = "Voici donc les offres d'emploi disponibles auprès de nous"

evenement = "Voici donc nos evements disponibles"

pas_evenement = "Pour le moment, il n'y a pas d'evenement disponible aupres de nous"

#-------------------------------------------------------------------------------------------#
#                             FONCTIONS CONSTANTS                                           #
#-------------------------------------------------------------------------------------------#
def voir_liste_des_fiches_metiers(domaine=""):
    return f"Voici donc les listes des fiches métiers disponibles pour le domainde de {domaine}"

def informations_stands(info):
    return f"DESCRITIONS: \n{info[4]}\n\nNOS CONTACTS:\nTel: {info[0]}\nEmail: {info[1]} \
        \n\nADRESSE: {info[3]}"

def description_emploi(description):
    return f"DESCRIPTIONS:\n\n{description}"