import messenger
from conf import ACCESS_TOKEN,URL_SERVER
import const 
import requetes
import json
from options import Options


class Traitement(Options):
    
    bot = messenger.Messenger(ACCESS_TOKEN)
    req = requetes.Requete()
    
    def __init__(self):
        '''
            Appel des constrcuteurs de la class parent.
        '''
        super().__init__(self.bot, self.req)
    
    #-------------------------------------------------------------------------------------------#
    #                          ANALYSES DES MESSAGES POSTÉS PAR                                 #
    #                                   FACEBOOK                                                #              
    #-------------------------------------------------------------------------------------------#

    def _analyse(self, data):
        '''
            Fonction analysant les données reçu de Facebook
            Donnée de type Dictionnaire attendu (JSON parsé)
        '''
        for event in data['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    sender_id = message['sender']['id']
        
                    if message['message'].get('quick_reply'):
                        self.__execution(
                            sender_id, message['message']['quick_reply'].get('payload'))

                    elif message['message'].get('text'):
                        self.__execution(
                            sender_id,
                            message['message'].get('text')
                        )

                if message.get('postback'):
                    recipient_id = message['sender']['id']
                    pst_payload = message['postback']['payload']
                    self.__execution(recipient_id, pst_payload)

    #-------------------------------------------------------------------------------------------#
    #                                   DIFFERENTS TRAITEMENTS                                  #              
    #-------------------------------------------------------------------------------------------#
    
    def salutation(self, sender_id):
        """
            Saluer et presenter qui nous sommes
            avant tout à l'utulisateurs
        """
        self.bot.send_message(
            sender_id,
            const.salutation
        )
        self.bot.send_quick_reply(sender_id, "bienvenue")
        return True

    def traitement_cmd(self, user_id, commande):
        """
            METHODES QUI ANALYSES ET TRAITE LES
            PAYLOADS DE QUICK_REPLY ENVOYER PAR
            FACEBOOK
        """
        
        cmd = commande.split()
        if commande == "__MENU":
            self.bot.send_quick_reply(user_id, "bienvenue")
            return True
        
        elif commande == "__FICHE_METIER":
            
            self.bot.send_quick_reply(
                user_id,
                "recherche_ou_voir_fiche_metier"
            )
            return True
        
        elif commande == "__VOIR_LISTE_FICHE_METIER":
            self.bot.send_quick_reply(
                user_id,
                "domaine_de_fiche_metier"
            )
            return True 
        
        elif cmd[0] == "__SANTE":
            self.fiche_metier_par_domaine(
                user_id,
                "Santé",
                cmd[-1],
                payload_plus_de_dix="__SANTE"
            )
            return True
        
        elif cmd[0] == "__INFORMATIQUE":
            self.fiche_metier_par_domaine(
                user_id,
                "Informatique",
                cmd[-1],
                payload_plus_de_dix="__INFORMATIQUE"
            )
            return True
        
        elif cmd[0] == "__COMMERCE":
            self.fiche_metier_par_domaine(
                user_id,
                "Commerce et Admnistration",
                cmd[-1],
                payload_plus_de_dix="__COMMERCE"
            )
            return True
        
        elif cmd[0] == "__AGRONOMIE":
            self.fiche_metier_par_domaine(
                user_id,
                "Agronomie",
                cmd[-1],
                payload_plus_de_dix="__AGRONOMIE"
            )
            return True
        
        elif cmd[0] == "__SCIENCE_HUMAINE":
            self.fiche_metier_par_domaine(
                user_id,
                "Science Humaine et Communication",
                cmd[-1],
                payload_plus_de_dix="__SCIENCE_HUMAINE"
            )
            return True
        
        elif cmd[0] == "__INDISTRUE":
            self.fiche_metier_par_domaine(
                user_id,
                "Industrie et BT",
                cmd[-1],
                payload_plus_de_dix="__INDISTRUE"
            )
            return True
        
        elif cmd[0] == "__JUSTICE":
            self.fiche_metier_par_domaine(
                user_id,
                "Justice et Force de l'ordre",
                cmd[-1],
                payload_plus_de_dix="__JUSTICE"
            )
            return True
        
        elif cmd[0] == "__TOURISME":
            self.fiche_metier_par_domaine(
                user_id,
                "Tourisme",
                cmd[-1],
                payload_plus_de_dix="__TOURISME"
            )
            return True

        elif commande == "__RECHERCHE_FICHE_METIER":
            self.bot.send_message(
                user_id,
                const.nom_de_domaine_rechercher
            )
            self.req.set_action(user_id, "CHERCHER_FICHE_METIER")
            return True
        
        elif commande == "__VISITE_STAND":
            self.bot.send_quick_reply(
                user_id,
                "rechercher_ou_visiter_stands"
            )
            return True
        
        elif commande == "__RECHERCHE_STAND":
            self.bot.send_message(
                user_id,
                const.exemple_de_nom_de_stand_a_cherchher
            )
            self.req.set_action(user_id, "CHERCHER_STAND")
            return True
        
        elif cmd[0] == "__VOIR_LISTE_DU_STAND":
            if not cmd[-1].isdigit():
                self.bot.send_message(
                    user_id,
                    const.donner_des_listes_du_stand
                )
            else:
                pass
            
            self.gestion_de_stands_par_dix(
                user_id,
                self.liste_de_tout_les_stands(
                    self.req.tous_les_stands()
                ),
                page=int(cmd[-1]) if cmd[-1].isdigit() else 1
            )
            return True
        
        elif cmd[0] == "__VOIR_LISTE_FICHE_METIER_RECHERCHE":
            self.gestion_de_liste_des_fiches_metier_par_dix(
                user_id,
                self.listes_de_tout_fiches_metiers(
                        self.req.rechercher_fiche_metier(
                        json.loads(self.req.get_temp(user_id)).get("recherche_fiche_metier")                     
                    )
                ),
                page=int(cmd[-1]) if cmd[-1].isdigit() else 1,
                types="recherche",
                payload_plus_de_dix="__VOIR_LISTE_FICHE_METIER_RECHERCHE"
            )
            return True
        
        elif cmd[0] == "__GALERIE":
            self.bot.send_message(
                user_id,
                const.galerie
            )
            self.bot.send_template(
                user_id,
                self.liste_galerie_de_chaque_stand(
                    cmd[-1],
                    self.req.galerie_de_chaque_stand(cmd[-1])
                )
            )
            return True
        
        elif cmd[0] == "__EMPLOI":
            data = self.req.emploi_de_chaque_stands(cmd[-2])
            if data:
                if not cmd[-1].isdigit():
                    self.bot.send_message(
                        user_id,
                        const.emploi
                    )
                    
                else:
                    pass
                
                self.gestion_de_liste_demploi_par_dix(
                    user_id,
                    cmd[-2],
                    self.liste_emploi_de_chaque_stand(
                        data,
                        cmd[-2]
                    ),
                    page=int(cmd[-1]) if cmd[-1].isdigit() else 1
                )
                return True
            
            else:
                self.bot.send_message(
                    user_id,
                    const.pas_emploi
                )
                return True
            
        elif cmd[0] == "__EVENEMENTS":
            
            data = self.req.evenement_chaque_stand(cmd[-2])
            if data:
                if not cmd[-1].isdigit():
                    self.bot.send_message(
                        user_id,
                        const.evenement
                    )
                    self.gestion_evenement_par_dix(
                        user_id,
                        cmd[-2],
                        self.liste_evenement_de_chaque_stand(cmd[-2],data),
                        page=int(cmd[-1]) if cmd[-1].isdigit() else 1
                    )
                    return True
                
                else:
                    self.gestion_evenement_par_dix(
                        user_id,
                        cmd[-2],
                        self.liste_evenement_de_chaque_stand(cmd[-2],data),
                        page=int(cmd[-1]) if cmd[-1].isdigit() else 1
                    )
                    return True
            else:
                self.bot.send_message(
                    user_id,
                    const.pas_evenement
                )
                return True

        elif cmd[0] == "__INFO":
            info = self.req.informations_de_chaque_stand(
                cmd[-1]
            )[0]
            self.bot.send_message(
                user_id,
                const.informations_stands(info)
            )
            
            if info[2]:
                self.bot.send_message(
                   user_id,
                   f"{const.site_web}\n\n{info[2]}"
               )
                return True
            
            else:
                return True

        elif cmd[0] == "__PRESENTATION":
            presentation = self.req.presentation_stand(cmd[-1])
            if presentation:
                self.bot.send_message(user_id,const.presentation_video)
                self.bot.send_file_url(
                    user_id,
                    f"{URL_SERVER}{cmd[-1]}/{presentation}",
                    filetype="video"
                )
                return True
            else:
                self.bot.send_message(user_id,const.pas_video)
                return True


    def traitement_pstPayload(self, user_id, commande):
        postback_payload = commande.split(' ')
        
        if postback_payload[0] == "__VOIR":
            self.bot.send_file_url(user_id, postback_payload[-2], 'image')
            
            self.req.inserer_consultation(
                user_id,
                postback_payload[-3],
                types=postback_payload[-1])
            return True
            
        elif postback_payload[0] == "__VOIR_EMPLOI":
            
            description = self.req.description_de_chaque_contenu(postback_payload[1])
            
            if postback_payload[-2].endswith(".pdf"):
                if description:
                    self.bot.send_message(
                        user_id,
                        const.description_emploi(description[0])
                    )
                    self.bot.send_file_url(
                        user_id,
                        postback_payload[-2],
                        filetype='file'
                    )
                    
                else:
                    self.bot.send_file_url(
                        user_id,
                        postback_payload[-2],
                        filetype='file'
                    )
            
            else:
                if description:
                    self.bot.send_message(
                        user_id,
                        const.description_emploi(description[0])
                    )
                    self.bot.send_file_url(
                        user_id,
                        postback_payload[-2],
                        filetype="image"
                    )
                    
                else:
                    self.bot.send_file_url(
                        user_id,
                        postback_payload[-2],
                        filetype="image"
                    )

            self.req.inserer_consultation(
                user_id,
                postback_payload[1],
                postback_payload[-1]
            )
            return True

        elif postback_payload[0] == "__VOIR_EVENEMENT":
            description = self.req.description_de_chaque_contenu(postback_payload[1])
            
            if postback_payload[-2].endswith(".pdf"):
                if description:
                    self.bot.send_message(
                        user_id,
                        const.description_emploi(description[0])
                    )
                    self.bot.send_file_url(
                        user_id,
                        postback_payload[-2],
                        filetype='file'
                    )
                    
                else:
                    self.bot.send_file_url(
                        user_id,
                        postback_payload[-2],
                        filetype='file'
                    )

                    
            elif postback_payload[-2].endswith(".mp4"):
                if description:
                    self.bot.send_message(
                        user_id,
                        const.description_emploi(description[0])
                    )
                    self.bot.send_file_url(
                        user_id,
                        postback_payload[-2],
                        filetype='video'
                    )
                    
                else:
                    self.bot.send_file_url(
                        user_id,
                        postback_payload[-2],
                        filetype='video'
                    )
                
            elif postback_payload[-1] == "CONTENU_URL":
                description_url = self.req.description_de_chaque_contenu(postback_payload[1])
                if description_url:
                    self.bot.send_message(
                        user_id,
                        const.description_emploi(description_url[0])
                    )
                    self.bot.send_message(
                        user_id,
                        postback_payload[-2]
                    )
                    
                else:
                    self.bot.send_message(
                        user_id,
                        postback_payload[-2]
                    )
                self.req.inserer_consultation(
                    user_id,
                    postback_payload[1],
                    postback_payload[-1].split("_")[0]
                )
                return True

            else:
                if description:
                    self.bot.send_message(
                        user_id,
                        const.description_emploi(description[0])
                    )
                    self.bot.send_file_url(
                        user_id,
                        postback_payload[-2],
                        filetype="image"
                    )
                    
                else:
                    self.bot.send_file_url(
                        user_id,
                        postback_payload[-2],
                        filetype="image"
                    )
            
            self.req.inserer_consultation(
                user_id,
                postback_payload[1],
                postback_payload[-1]
            )
            return True
            
        elif postback_payload[0] == "__VISITER":
            self.bot.send_quick_reply(
                user_id,
                "visiter_stand",
                postback_payload[-1]
            )
            return True
            
    def traitement_action(self, user_id, commande, statut):
        """
            IL Y A DES MOMENTS QUE LES UTILISATEUR POSTENT
            DES MESSAGES COMME FAIRE DES RECHERCHES OU REPONDRE
            DES QUESTIONS,.....
            
            DONC IL FAUT LE DONNER UNE STATUT D'ACTION AFIN DE 
            GERER SES POSTS SUR MESSENGER
            
            ET ALORS GERER TOUS ÇA L'INTERER DE CREER CETTE 
            METHODE
        """
        
        if statut == "CHERCHER_FICHE_METIER":
            data = self.req.rechercher_fiche_metier(commande.strip())
            if data:
                self.bot.send_message(
                    user_id,
                    const.resultat_de_recherche
                )
                self.gestion_de_liste_des_fiches_metier_par_dix(
                    user_id,
                    self.listes_de_tout_fiches_metiers(data),
                    page=1,
                    types="recherche",
                    payload_plus_de_dix="__VOIR_LISTE_FICHE_METIER_RECHERCHE"
                )
                
                if len(data) > 10:
                    """
                        On assigne dans le temp de l'utilisateur le mot clé
                        de son recherche si les resultats de recherche depassent
                        le nombre dix pour le but d'obtenir les resultats de la 
                        page suivant
                    """
                    self.req.set_temp(
                        user_id,
                        json.dumps({"recherche_fiche_metier":commande.strip()})
                    )  
                else:
                    pass

                self.req.set_action(user_id, None)
                return True

            else:
                self.bot.send_message(
                    user_id,
                    const.resultat_de_recherche_vide
                )
                self.bot.send_quick_reply(
                    user_id,
                    "recherche_ou_voir_fiche_metier"
                )
                self.req.set_action(user_id, None)
                return True

        elif statut == "CHERCHER_STAND":
            data = self.req.rechercher_fiche_stands(commande)
            if data:
                self.bot.send_message(
                    user_id,
                    const.resultat_de_recherche
                )
                self.bot.send_template(
                    user_id,
                    self.liste_de_tout_les_stands(data)
                )
                self.req.set_action(user_id, None)
                return True
            
            else:
                self.bot.send_message(
                    user_id,
                    const.resultat_de_recherche_stand_vide
                )
                self.bot.send_quick_reply(
                    user_id,
                    "rechercher_ou_visiter_stands"
                )
                self.req.set_action(user_id, None)
                return True

    #-------------------------------------------------------------------------------------------#
    #                       ROUTAGES VERS LES DIFFERENTS TRAITEMENTS                            #              
    #-------------------------------------------------------------------------------------------#
    def __execution(self, user_id, commande):
        """
            Fonction privée qui traite les differentes commandes réçu
            Ary eto dia refa marina ny iray @reo traitement reo dia
            tapaka ny fonction
        """
        self.bot.send_action(user_id, 'mark_seen')
        
        self.req.verif_utilisateur(user_id)
        statut = self.req.get_action(user_id)
        
        if self.traitement_action(user_id, commande, statut):
            return
        
        if self.traitement_pstPayload(user_id, commande):
            return

        if self.traitement_cmd(user_id, commande):
            return

        if self.salutation(user_id):
            return