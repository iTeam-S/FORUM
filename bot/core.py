import const
import requetes
import json
import messenger
from options import Options
from utils import translate
from conf import ACCESS_TOKEN, URL_SERVER, ID_DEV


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

    def salutation(self, sender_id, user_lang):
        """
            Saluer et presenter qui nous sommes
            avant tout à l'utulisateurs
        """
        self.bot.send_message(
            sender_id,
            translate("salutation", user_lang)
        )
        self.bot.send_media(
            sender_id,
            "https://www.facebook.com/iTeam.Community/photos/a.102143328508332/102143775174954/",
            "image")
        self.bot.send_quick_reply(sender_id, user_lang, "choix_langues")

    def divers(self, user_id, user_lang, commande):
        self.bot.send_quick_reply(user_id, user_lang, "bienvenue")
        return True

    def traitement_cmd(self, user_id, user_lang, commande):
        """
            METHODES QUI ANALYSES ET TRAITE LES
            PAYLOADS DE QUICK_REPLY ENVOYER PAR
            FACEBOOK
        """
        cmd = commande.split()
        _cmd = commande.split("_")

        if commande == "__MENU":
            self.bot.send_quick_reply(user_id, user_lang, "bienvenue")
            return True

        elif commande == "get_started":
            self.salutation(user_id, user_lang)
            return True

        elif cmd[0] == '__SET_LANG' and cmd[-1] in ('fr', 'mg'):
            self.req.update_lang(user_id, cmd[-1])
            self.bot.send_message(
                user_id,
                translate('langue_mis_a_jour', cmd[-1]) + ' ✔'
            )
            self.bot.persistent_menu(
                user_id,
                const.persistent_menu('PRINCIPALE', cmd[-1])
            )
            self.bot.send_quick_reply(user_id, cmd[-1], "bienvenue")
            return True

        elif commande == "__FICHE_METIER":
            self.bot.send_quick_reply(
                user_id,
                user_lang,
                "recherche_ou_voir_fiche_metier"
            )
            return True

        elif commande == "__VOIR_LISTE_FICHE_METIER":
            self.bot.send_quick_reply(
                user_id,
                user_lang,
                "domaine_de_fiche_metier"
            )
            return True

        elif cmd[0] == "__SANTE":
            self.fiche_metier_par_domaine(
                user_id,
                translate("sante", user_lang).upper(),
                "Santé",
                cmd[-1],
                payload_plus_de_dix="__SANTE",
                lang=user_lang
            )
            return True

        elif cmd[0] == "__INFORMATIQUE":
            self.fiche_metier_par_domaine(
                user_id,
                translate("informatique", user_lang).upper(),
                "Informatique",
                cmd[-1],
                payload_plus_de_dix="__INFORMATIQUE",
                lang=user_lang
            )
            return True

        elif cmd[0] == "__COMMERCE":
            self.fiche_metier_par_domaine(
                user_id,
                translate("comm_et_admin", user_lang).upper(),
                "Commerce et Admnistration",
                cmd[-1],
                payload_plus_de_dix="__COMMERCE",
                lang=user_lang
            )
            return True

        elif cmd[0] == "__AGRONOMIE":
            self.fiche_metier_par_domaine(
                user_id,
                translate("agronomie", user_lang).upper(),
                "Agronomie",
                cmd[-1],
                payload_plus_de_dix="__AGRONOMIE",
                lang=user_lang
            )
            return True

        elif cmd[0] == "__SCIENCE_HUMAINE":
            self.fiche_metier_par_domaine(
                user_id,
                translate("science_humaine", user_lang).upper(),
                "Science Humaine et Communication",
                cmd[-1],
                payload_plus_de_dix="__SCIENCE_HUMAINE",
                lang=user_lang
            )
            return True

        elif cmd[0] == "__INDISTRUE":
            self.fiche_metier_par_domaine(
                user_id,
                translate("industrie", user_lang).upper(),
                "Industrie et BT",
                cmd[-1],
                payload_plus_de_dix="__INDISTRUE",
                lang=user_lang
            )
            return True

        elif cmd[0] == "__JUSTICE":
            self.fiche_metier_par_domaine(
                user_id,
                translate("justice", user_lang).upper(),
                "Justice et Force de l'ordre",
                cmd[-1],
                payload_plus_de_dix="__JUSTICE",
                lang=user_lang
            )
            return True

        elif cmd[0] == "__TOURISME":
            self.fiche_metier_par_domaine(
                user_id,
                translate("tourisme", user_lang).upper(),
                "Tourisme",
                cmd[-1],
                payload_plus_de_dix="__TOURISME",
                lang=user_lang
            )
            return True

        elif commande == "__RECHERCHE_FICHE_METIER":
            self.bot.send_message(
                user_id,
                translate("nom_de_domaine_rechercher", user_lang)
            )
            self.req.set_action(user_id, "CHERCHER_FICHE_METIER")
            return True

        elif commande == "__OUI_AUTRE_DOMAINE":
            self.bot.send_quick_reply(
                user_id, user_lang, "domaine_de_fiche_metier")
            return True

        elif commande == "__NON_AUTRE_DOMAINE":
            self.bot.send_message(user_id, "😔😔")
            return True

        elif commande == "__VISITE_STAND":
            self.bot.send_quick_reply(
                user_id,
                user_lang,
                "rechercher_ou_visiter_stands"
            )
            return True

        elif commande == "__RECHERCHE_STAND":
            self.bot.send_message(
                user_id,
                translate("recherche_stand", user_lang)
            )
            self.req.set_action(user_id, "CHERCHER_STAND")
            return True

        elif cmd[0] == "__VOIR_LISTE_DU_STAND":
            if not cmd[-1].isdigit():
                self.bot.send_message(
                    user_id,
                    translate("listes_stands", user_lang)
                )
            else:
                pass

            self.gestion_de_stands_par_dix(
                user_id,
                user_lang,
                self.liste_de_tout_les_stands(
                    self.req.tous_les_stands(),
                    user_lang
                ),
                page=int(cmd[-1]) if cmd[-1].isdigit() else 1
            )
            return True

        elif cmd[0] == "__VOIR_LISTE_FICHE_METIER_RECHERCHE":
            self.gestion_de_liste_des_fiches_metier_par_dix(
                user_id,
                user_lang,
                self.listes_de_tout_fiches_metiers(
                    self.req.rechercher_fiche_metier(
                        json.loads(self.req.get_temp(user_id)).get("recherche_fiche_metier")
                    ), user_lang
                ),
                page=int(cmd[-1]) if cmd[-1].isdigit() else 1,
                types="recherche",
                payload_plus_de_dix="__VOIR_LISTE_FICHE_METIER_RECHERCHE"
            )
            return True

        elif cmd[0] == "__GALERIE":
            galery = self.req.galerie_de_chaque_stand(cmd[-1])
            if galery:
                self.bot.send_message(
                    user_id,
                    translate("galery", user_lang)
                )
                self.bot.send_template(
                    user_id,
                    self.liste_galerie_de_chaque_stand(
                        cmd[-1],
                        user_lang,
                        galery
                    ), next=[const.retoure("STAND_EMPLOI", user_lang, cmd[-1])]
                )
                return True

            else:
                self.bot.send_message(
                    user_id, translate(
                        "pas_galery", user_lang))
                self.bot.send_quick_reply(
                    user_id,
                    user_lang,
                    "retourne_stand_emploi",
                    cmd[-1]
                )
                return True

        elif cmd[0] == "__EMPLOI":
            data = self.req.emploi_de_chaque_stands(cmd[-2])
            if data:
                if not cmd[-1].isdigit():
                    self.bot.send_message(
                        user_id,
                        translate("emploi", user_lang)
                    )

                else:
                    pass

                self.gestion_de_liste_demploi_par_dix(
                    user_id,
                    user_lang,
                    cmd[-2],
                    self.liste_emploi_de_chaque_stand(
                        data,
                        user_lang,
                        cmd[-2]
                    ),
                    page=int(cmd[-1]) if cmd[-1].isdigit() else 1
                )
                return True

            else:
                self.bot.send_message(
                    user_id,
                    translate("pas_emploi", user_lang)
                )
                self.bot.send_quick_reply(
                    user_id,
                    user_lang,
                    "retourne_stand_emploi",
                    cmd[1]
                )
                return True

        elif cmd[0] == "__EVENEMENTS":

            data = self.req.evenement_chaque_stand(cmd[-2])
            if data:
                if not cmd[-1].isdigit():
                    self.bot.send_message(
                        user_id,
                        translate("events", user_lang)
                    )
                    self.gestion_evenement_par_dix(
                        user_id,
                        cmd[-2],
                        user_lang,
                        self.liste_evenement_de_chaque_stand(cmd[-2], user_lang, data),
                        page=int(cmd[-1]) if cmd[-1].isdigit() else 1
                    )
                    return True

                else:
                    self.gestion_evenement_par_dix(
                        user_id,
                        cmd[-2],
                        user_lang,
                        self.liste_evenement_de_chaque_stand(cmd[-2], user_lang, data),
                        page=int(cmd[-1]) if cmd[-1].isdigit() else 1
                    )
                    return True

            else:
                self.bot.send_message(
                    user_id,
                    translate("pas_events", user_lang)
                )
                self.bot.send_quick_reply(
                    user_id,
                    user_lang,
                    "retourne_stand_emploi",
                    cmd[1]
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
                    f"{translate('lien',user_lang)}\n{info[2]}"
                )
                self.bot.send_quick_reply(
                    user_id,
                    user_lang,
                    "retourne_stand_emploi",
                    cmd[-1]
                )
                return True

            else:
                self.bot.send_quick_reply(
                    user_id,
                    user_lang,
                    "retourne_stand_emploi",
                    cmd[-1]
                )
                return True

        elif cmd[0] == "__PRESENTATION":
            presentation = self.req.presentation_stand(cmd[-1])
            if presentation:

                if presentation.startswith("http"):
                    self.bot.send_message(
                        user_id, translate(
                            "present_video", user_lang))
                    self.bot.send_media(user_id, presentation, "video")
                    self.bot.send_quick_reply(
                        user_id,
                        user_lang,
                        "retourne_stand_emploi",
                        cmd[-1]
                    )
                    return True

                else:
                    self.bot.send_message(
                        user_id, translate(
                            "present_video", user_lang))
                    self.bot.send_file_url(
                        user_id,
                        f"{URL_SERVER}{cmd[-1]}/{presentation}",
                        filetype="video"
                    )
                    self.bot.send_quick_reply(
                        user_id,
                        user_lang,
                        "retourne_stand_emploi",
                        cmd[-1]
                    )
                    return True

            else:
                self.bot.send_message(
                    user_id, translate(
                        "pas_video", user_lang))
                self.bot.send_quick_reply(
                    user_id,
                    user_lang,
                    "retourne_stand_emploi",
                    cmd[-1]
                )
                return True

        elif commande == "__TEST_KAVIO":
            verification = int(self.req.verif_test_kavio(user_id))
            if verification and verification >= 72:
                self.bot.send_message(
                    user_id,
                    translate("fini_test_kavio", user_lang)
                )
                self.bot.send_quick_reply(
                    user_id, user_lang, "fini_test_kavio")
                return True

            elif verification and verification < 72:
                self.bot.send_message(
                    user_id,
                    translate("test_non_fini", user_lang)
                )
                self.bot.send_quick_reply(
                    user_id, user_lang, "refaire_test_kavio")
                return True

            else:
                self.bot.send_message(
                    user_id, translate(
                        "bienvenu_kavio", user_lang))
                self.bot.send_quick_reply(user_id, user_lang, "tester_kavio")
                return True

        elif commande == "__ABANDON_KAVIO":
            self.bot.send_message(
                user_id, translate(
                    "remercier_abandon", user_lang))
            self.bot.send_quick_reply(user_id, user_lang, "bienvenue")
            return True

        elif commande == "__NON_REFAIRE":
            self.bot.send_message(
                user_id,
                translate("non_refaire", user_lang)
            )
            self.bot.send_quick_reply(
                user_id,
                user_lang,
                "bienvenue"
            )
            return True

        elif commande == "__OUI_REFAIRE":
            self.req.suppression_test_kavio(user_id)
            self.bot.send_message(
                user_id, translate(
                    "bienvenu_kavio", user_lang))
            self.bot.send_message(
                user_id, translate(
                    "consignes_part_1", "fr"))
            self.bot.send_message(
                user_id, f"{translate('serie','fr').upper()} 1\n{const.get_serie('1','1')}")
            self.bot.send_quick_kavio(
                user_id,
                types=0,
                kavio=const.get_quick_kavio("A_1_1_1")
            )
            return True

        elif commande == "__FAIRE_KAVIO":
            self.bot.send_message(
                user_id, translate(
                    "consignes_part_1", "fr"))
            self.bot.send_message(
                user_id, f"{translate('serie','fr').upper()} 1\n{const.get_serie('1','1')}")
            self.bot.send_quick_kavio(
                user_id,
                types=0,
                kavio=const.get_quick_kavio("A_1_1_1")
            )
            return True

        elif _cmd[0] == "--**KAVIO":
            categ = ["A", "I", "R", "S", "C", "E"]
            """
                _cmd[-1]:point,
                _cmd[1]:categ
                _cmd[2]:num_question,
                _cmd[3]:partie,
                _cmd[4]:serie
            """

            self.req.insert_kavio(user_id, int(_cmd[2]), int(
                _cmd[3]), int(_cmd[4]), _cmd[1], int(_cmd[-1]))
            if int(_cmd[2]) < 6:
                num_question = int(_cmd[2])
                verif_trois_vrai = int(self.req.verif_trois_vrai(
                    int(_cmd[3]),
                    int(_cmd[4]),
                    user_id
                ))

                if verif_trois_vrai < 3:
                    self.bot.send_quick_kavio(
                        user_id,
                        types=0,
                        kavio=const.get_quick_kavio(
                            f"{categ[num_question]}_{num_question+1}_{_cmd[3]}_{_cmd[4]}")
                    )
                    return True

                else:
                    self.bot.send_quick_kavio(
                        user_id,
                        types=1,
                        kavio=const.get_quick_kavio(
                            f"{categ[num_question]}_{num_question+1}_{_cmd[3]}_{_cmd[4]}",)
                    )
                    return True

            else:
                serie = int(_cmd[4])
                if serie < 4:
                    self.bot.send_message(
                        user_id,
                        f"{translate('serie','fr').upper()} {serie+1}\n{const.get_serie(_cmd[3],serie+1)}"
                    )
                    self.bot.send_quick_kavio(
                        user_id, types=0, kavio=const.get_quick_kavio(
                            f"A_1_{_cmd[3]}_{serie+1}"))
                    return True

                else:
                    partie = int(_cmd[3])
                    if partie < 3:
                        self.bot.send_message(user_id, translate(
                            f"consignes_part_{partie+1}", "fr"))
                        self.bot.send_message(
                            user_id,
                            f"{translate('serie','fr').upper()} 1\n{const.get_serie(f'{partie+1}','1')}")
                        self.bot.send_quick_kavio(
                            user_id, types=0, kavio=const.get_quick_kavio(
                                f"A_1_{partie+1}_1"))
                        return True
                    else:
                        self.resultat_generale(user_id, "fr")
                        self.bot.send_quick_reply(
                            user_id, user_lang, "fin_kavio")
                        return True

        elif commande == "__VOIR_RESULTAT":
            self.resultat_generale(user_id, "fr")
            self.bot.send_quick_reply(user_id, user_lang, "fin_kavio")
            return True

        elif commande == "__RETOURE_FICHEMETIER":
            self.bot.send_quick_reply(
                user_id, user_lang, "domaine_de_fiche_metier")
            return True

        elif commande == "__RETOURE_FICHEMETIER_RECHERCHE":
            self.bot.send_quick_reply(
                user_id, user_lang, "recherche_ou_voir_fiche_metier")
            return True

        elif cmd[0] == "__RETOURNE_STAND_EMPLOI":
            self.__execution(user_id, f"__VISITER {cmd[-1]}")
            return True

        elif commande == "__RETOURNE_STAND_DEBUT":
            self.bot.send_quick_reply(
                user_id, user_lang, "rechercher_ou_visiter_stands")
            return True

    def traitement_pstPayload(self, user_id, user_lang, commande):
        postback_payload = commande.split(' ')

        if postback_payload[0] == "__VOIR":
            self.bot.send_file_url(user_id, postback_payload[-2], 'image')
            self.req.inserer_consultation(
                user_id,
                postback_payload[-3],
                types=postback_payload[-1]
            )
            self.bot.send_quick_reply(user_id,
                                      user_lang,
                                      "retoure_a_la_domaine") if postback_payload[-1] == "FICHE_METIER" else self.bot.send_quick_reply(user_id,
                                                                                                                                       user_lang,
                                                                                                                                       "retourne_stand_emploi",
                                                                                                                                       postback_payload[-2].split("/")[-2])
            return True

        elif postback_payload[0] == "__VOIR_EMPLOI":
            description = self.req.description_de_chaque_contenu(
                postback_payload[1])[0]
            
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
                    self.bot.send_quick_reply(
                        user_id,
                        user_lang,
                        "retourne_stand_emploi",
                        postback_payload[-2].split("/")[-2]
                    )

                else:
                    self.bot.send_file_url(
                        user_id,
                        postback_payload[-2],
                        filetype='file'
                    )

                    self.bot.send_quick_reply(
                        user_id,
                        user_lang,
                        "retourne_stand_emploi",
                        postback_payload[-2].split("/")[-2]
                    )

            else:
                if description:
                    print("ato")
                    self.bot.send_message(
                        user_id,
                        const.description_emploi(description[0])
                    )
                    self.bot.send_file_url(
                        user_id,
                        postback_payload[-2],
                        filetype="image"
                    )

                    self.bot.send_quick_reply(
                        user_id,
                        user_lang,
                        "retourne_stand_emploi",
                        postback_payload[-2].split("/")[-2]
                    )

                else:
                    self.bot.send_file_url(
                        user_id,
                        postback_payload[-2],
                        filetype="image"
                    )
                    self.bot.send_quick_reply(
                        user_id,
                        user_lang,
                        "retourne_stand_emploi",
                        postback_payload[-2].split("/")[-2]
                    )

            self.req.inserer_consultation(
                user_id,
                postback_payload[1],
                postback_payload[-1]
            )
            return True

        elif postback_payload[0] == "__VOIR_EVENEMENT":
            description = self.req.description_de_chaque_contenu(
                postback_payload[1])[0]

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

                    self.bot.send_quick_reply(
                        user_id,
                        user_lang,
                        "retourne_stand_emploi",
                        postback_payload[-2].split("/")[-2]
                    )

                else:
                    self.bot.send_file_url(
                        user_id,
                        postback_payload[-2],
                        filetype='file'
                    )
                    self.bot.send_quick_reply(
                        user_id,
                        user_lang,
                        "retourne_stand_emploi",
                        postback_payload[-2].split("/")[-2]
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

                    self.bot.send_quick_reply(
                        user_id,
                        user_lang,
                        "retourne_stand_emploi",
                        postback_payload[-2].split("/")[-2]
                    )

                else:
                    self.bot.send_file_url(
                        user_id,
                        postback_payload[-2],
                        filetype='video'
                    )

                    self.bot.send_quick_reply(
                        user_id,
                        user_lang,
                        "retourne_stand_emploi",
                        postback_payload[-2].split("/")[-2]
                    )

            elif postback_payload[-1] == "CONTENU_URL":
                description_url = self.req.description_de_chaque_contenu(
                    postback_payload[1])[0]
                if description_url:
                    self.bot.send_message(
                        user_id,
                        const.description_emploi(description_url[0])
                    ) 
                    self.bot.send_message(
                        user_id,
                        f"{translate('lien_actu', user_lang)}\n\n{postback_payload[-2]}",
                    )
                    self.bot.send_quick_reply(
                        user_id,
                        user_lang,
                        "retourne_stand_emploi",
                        postback_payload[-3]
                    )

                else:
                    self.bot.send_message(
                        user_id,
                        postback_payload[-2]
                    )
                    self.bot.send_quick_reply(
                        user_id,
                        user_lang,
                        "retourne_stand_emploi",
                        postback_payload[-3]
                    )

                self.req.inserer_consultation(
                    user_id,
                    postback_payload[1],
                    postback_payload[-1].split("_")[0]
                )
                return True

            else:
                try:

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

                        self.bot.send_quick_reply(
                            user_id,
                            user_lang,
                            "retourne_stand_emploi",
                            postback_payload[-2].split("/")[-2]
                        )

                    else:
                        self.bot.send_file_url(
                            user_id,
                            postback_payload[-2],
                            filetype="image"
                        )
                        
                        self.bot.send_quick_reply(
                            user_id,
                            user_lang,
                            "retourne_stand_emploi",
                            postback_payload[-2].split("/")[-2]
                        )

                except BaseException as err:
                    self.bot.send_message(ID_DEV,str(err))
                    return True

            self.req.inserer_consultation(
                user_id,
                postback_payload[1],
                postback_payload[-1]
            )
            return True

        elif postback_payload[0] == "__VISITER":
            description = self.req.description_de_chaque_stand(
                postback_payload[-1]
            )

            if description:
                self.bot.send_message(user_id, "DESCRIPTION:\n" + description)

            id_stand = postback_payload[-1]
            quick_rep =  []

            # verification video presentation
            if self.req.presentation_stand(id_stand):
                quick_rep.append(
                   {
                        "content_type": "text",
                        "title": "🏢" + translate("presentation", user_lang).upper(),
                        "payload": f"__PRESENTATION {id_stand}"
                    },
                )

            # verification de galerie
            if self.req.galerie_de_chaque_stand(id_stand):
                quick_rep.append(
                    {
                        "content_type": "text",
                        "title": "🖼️" + translate("galerie",user_lang).upper(),
                        "payload": f"__GALERIE {id_stand}"
                    },
                )
            
            # verification emploi
            if self.req.emploi_de_chaque_stands(id_stand):
                quick_rep.append(
                    {
                        "content_type": "text",
                        "title": "💱" + translate("offre", user_lang).upper(),
                        "payload": f"__EMPLOI {id_stand} page"
                    },
                )
            
            # verification evenement
            if self.req.evenement_chaque_stand(id_stand):
                 quick_rep.append(
                     {
                        "content_type": "text",
                        "title": "📜" + translate("info",user_lang).upper(),
                        "payload": f"__EVENEMENTS {id_stand} page"
                    },
                )
            
            quick_rep.append(              
                {  
                    "content_type": "text",
                    "title": "📠" + translate("plus_info", user_lang).upper(),
                    "payload": f"__INFO {id_stand}"
                }
            )
            self.bot.send_quick_reply(
                user_id,
                user_lang,
                "visiter_stand",
                postback_payload[-1],
                quick_rep=quick_rep
            )
            return True

        elif postback_payload[0] == "stand":
            stand = self.req.stand_par_id(postback_payload[-1])
            if stand:
                self.bot.send_template(
                    user_id,
                    self.liste_de_tout_les_stands(
                        stand,
                        user_lang
                    )
                )
                return True
            else:
                self.bot.send_message(
                    user_id,
                    translate("pas_fiche_stand_id", user_lang)
                )
                return True

    def traitement_action(self, user_id, user_lang, commande, statut):
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
                    translate("resultat_de_recherche", user_lang)
                )
                self.gestion_de_liste_des_fiches_metier_par_dix(
                    user_id,
                    user_lang,
                    self.listes_de_tout_fiches_metiers(data, user_lang),
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
                    self.req.set_temp(user_id, json.dumps(
                        {"recherche_fiche_metier": commande.strip()}))
                else:
                    pass

                self.req.set_action(user_id, None)
                return True

            else:
                self.bot.send_message(
                    user_id,
                    translate("resultat_de_recherche_vide", user_lang)
                )
                self.bot.send_quick_reply(
                    user_id,
                    user_lang,
                    "recherche_ou_voir_fiche_metier"
                )
                self.req.set_action(user_id, None)
                return True

        elif statut == "CHERCHER_STAND":
            data = self.req.rechercher_fiche_stands(commande)
            if data:
                self.bot.send_message(
                    user_id,
                    translate("resultat_de_recherche", user_lang)
                )
                self.bot.send_template(
                    user_id,
                    self.liste_de_tout_les_stands(data, user_lang),
                    next=[const.retoure("STAND_DEBUT", user_lang)]
                )
                self.req.set_action(user_id, None)
                return True

            else:
                self.bot.send_message(
                    user_id,
                    translate("resultat_de_recherche_stand_vide", user_lang)
                )
                self.bot.send_quick_reply(
                    user_id,
                    user_lang,
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

        user_lang = self.req.get_user_lang(user_id)

        if self.traitement_action(user_id, user_lang, commande, statut):
            return

        if self.traitement_pstPayload(user_id, user_lang, commande):
            return

        if self.traitement_cmd(user_id, user_lang, commande):
            return

        if self.divers(user_id, user_lang, commande):
            return
