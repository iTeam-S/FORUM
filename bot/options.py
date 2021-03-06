from messenger import Messenger
from requetes import Requete
from conf import URL_SERVER
from utils import translate
import const


class Options:

    def __init__(self, bot: Messenger, req: Requete):
        if not isinstance(bot, Messenger):
            raise Exception('bot doit être de type Messenger')
        self.bot = bot
        if not isinstance(req, Requete):
            raise Exception('req doit être de type Requete')
        self.req = req

    def listes_de_tout_fiches_metiers(self, data, lang):
        """
            Methodes qui fetche tout les fiches
            metiers disponibles
        """
        liste_des_fiches_metiers = []
        for i in range(len(data)):
            liste_des_fiches_metiers.append({
                "title": f"{i+1} - {data[i][1].upper()}",
                "image_url": f"{URL_SERVER}{data[i][-1]}/{data[i][2]}",
                "buttons": [
                    {
                        "type": "postback",
                        "title": translate("voir", lang),
                        "payload": f"__VOIR {data[i][0]} {URL_SERVER}{data[i][-1]}/{data[i][2]} FICHE_METIER"
                    }
                ]
            }
            )
        return liste_des_fiches_metiers

    def gestion_de_liste_des_fiches_metier_par_dix(
            self,
            dest_id,
            lang,
            liste_des_fiches_metiers,
            page,
            types,
            payload_plus_de_dix):
        '''
            methode gere à afficher les fiches metiers
            sous formes de templates par 10 affiches
        '''

        res = liste_des_fiches_metiers
        deb_indice = (page - 1) * 10

        if types == "recherche":
            if len(res) > deb_indice + 10:
                self.bot.send_template(
                    dest_id, res[deb_indice:deb_indice + 10],
                    next=[
                        {
                            "content_type": "text",
                            "title": "⏭️" + translate("page_suivant", lang).upper(),
                            "payload": f"{payload_plus_de_dix} {page+1}",
                        }, const.retoure("FICHES_METIERS_RECHERCHE", lang)
                    ]
                )
            else:
                self.bot.send_template(
                    dest_id,
                    res[deb_indice:deb_indice + 10],
                    next=[const.retoure("FICHES_METIERS_RECHERCHE", lang)]
                )

        else:
            if len(res) > deb_indice + 10:
                self.bot.send_template(
                    dest_id, res[deb_indice:deb_indice + 10],
                    next=[
                        {
                            "content_type": "text",
                            "title": "⏭️" + translate("page_suivant", lang).upper(),
                            "payload": f"{payload_plus_de_dix} {page+1}",
                        }, const.retoure("FICHES_METIERS", lang)
                    ]
                )
            else:
                self.bot.send_template(
                    dest_id,
                    res[deb_indice:deb_indice + 10],
                    # next=[const.retoure("FICHES_METIERS", lang)]
                )
                self.bot.send_quick_reply(dest_id, lang, "autre_domaine")

    def fiche_metier_par_domaine(
            self,
            user_id,
            trans_domaine,
            domaine,
            page,
            payload_plus_de_dix="",
            lang="fr"):
        listes = self.req.fiche_metier_chaque_domaine(domaine=domaine)
        if listes:
            if not page.isdigit():
                self.bot.send_message(
                    user_id,
                    const.voir_liste_des_fiches_metiers(trans_domaine, lang)
                )
            else:
                pass

            self.gestion_de_liste_des_fiches_metier_par_dix(
                user_id,
                lang,
                self.listes_de_tout_fiches_metiers(listes, lang),
                page=int(page) if page.isdigit() else 1,
                types="listage",
                payload_plus_de_dix=payload_plus_de_dix
            )

        else:
            self.bot.send_message(user_id, translate("pas_fiche", lang))
            self.bot.send_quick_reply(user_id, lang, "retoure_a_la_domaine")
            return True

    def liste_de_tout_les_stands(self, data, lang):
        liste_des_stands = []
        for i in range(len(data)):
            liste_des_stands.append({
                "title": f"{data[i][2].upper()}",
                "image_url": f"{URL_SERVER}{data[i][0]}/{data[i][1]}" if data[i][1]
                else "https://forum.iteam-s.mg/static/media/logodefaut.6ac1d227.png",
                "buttons": [
                    {
                        "type": "postback",
                        "title": translate("visiter", lang).upper(),
                        "payload": f"__VISITER {data[i][0]}"
                    }
                ]
            }
            )

        return liste_des_stands

    def gestion_de_stands_par_dix(self, dest_id, lang, liste_des_stands, page):
        res = liste_des_stands
        if res:
            deb_indice = (page - 1) * 10

            if len(res) > deb_indice + 10:
                self.bot.send_template(
                    dest_id, res[deb_indice:deb_indice + 10],
                    next=[
                        {
                            "content_type": "text",
                            "title": "⏭️" + translate("page_suivant", lang).upper(),
                            "payload": f"__VOIR_LISTE_DU_STAND {page+1}",
                        }, const.retoure("STAND_DEBUT", lang)
                    ]
                )
            else:
                self.bot.send_template(
                    dest_id,
                    res[deb_indice:deb_indice + 10],
                    next=[const.retoure("STAND_DEBUT", lang)]
                )

    def liste_galerie_de_chaque_stand(self, id_stand, lang, data):
        liste_galerie = []
        for i in range(len(data)):
            liste_galerie.append({
                "title": f"{i+1} - {data[i][1].upper()}",
                "image_url": f"{URL_SERVER}{id_stand}/{data[i][2]}",
                "buttons": [
                    {
                        "type": "postback",
                        "title": translate("voir", lang),
                        "payload": f"__VOIR {data[i][0]} {URL_SERVER}{id_stand}/{data[i][2]} CONTENU"
                    }
                ]
            }
            )

        return liste_galerie

    def liste_emploi_de_chaque_stand(self, data, lang, id_stand):
        liste_emploi = []
        for i in range(len(data)):
            liste_emploi.append({
                "title": f"{i+1} - {data[i][1].upper()}",
                "image_url": f"{URL_SERVER}{id_stand}/{data[i][2]}" if not data[i][2].endswith(".pdf")
                else "https://www.iconpacks.net/icons/2/free-pdf-download-icon-2617-thumb.png",
                "buttons": [
                    {
                        "type": "postback",
                        "title": translate("telecharger", lang).upper() if data[i][2].endswith(".pdf") else translate("voir", lang).upper(),
                        "payload": f"__VOIR_EMPLOI {data[i][0]} {URL_SERVER}{id_stand}/{data[i][2]} CONTENU"
                    }
                ]
            }
            )
        return liste_emploi

    def gestion_de_liste_demploi_par_dix(
            self, dest_id, lang, id_stand, liste_emploi, page):
        res = liste_emploi
        deb_indice = (page - 1) * 10

        if len(res) > deb_indice + 10:
            self.bot.send_template(dest_id,
                                   res[deb_indice:deb_indice + 10],
                                   next=[{"content_type": "text",
                                          "title": "⏭️" + translate("page_suivant",
                                                                    lang).upper(),
                                          "payload": f"__EMPLOI {id_stand} {page+1}",
                                          },
                                         const.retoure("STAND_EMPLOI",
                                                       lang,
                                                       id_stand)])
        else:
            self.bot.send_template(
                dest_id,
                res[deb_indice:deb_indice + 10],
                next=[const.retoure("STAND_EMPLOI", lang, id_stand)]
            )

    def gestion_extension_de_fichier(self, fichier):
        if fichier.endswith(".pdf"):
            return "https://www.iconpacks.net/icons/2/free-pdf-download-icon-2617-thumb.png", "telecharger"  

        elif fichier.startswith("http"):
            verif = fichier.split("/")
            if verif[-1].isdigit() and verif[-2]=="videos":
                return "https://icon-library.com/images/play-video-icon-png-transparent/play-video-icon-png-transparent-14.jpg", "regarder"
            return "https://www.aussitot.fr/wp-content/uploads/2009/10/fb-lien-420.png", "voir"

        elif fichier.endswith(".mp4"):
            return "https://icon-library.com/images/play-video-icon-png-transparent/play-video-icon-png-transparent-14.jpg", "regarder"

        else:
            return "https://www.kindpng.com/picc/m/244-2446073_icons8-flat-gallery-icon-logo-gallery-png-transparent.png", "voir"

    def liste_evenement_de_chaque_stand(self, id_stand, lang, data):
        list_evenement = []
        for i in range(len(data)):
            list_evenement.append({
                "title": f"{i+1} - {data[i][1].upper()}",
                "image_url": f"{list(map(self.gestion_extension_de_fichier,list(data[i][2].split())))[0][0]}",
                "buttons": [
                    {
                        "type": "postback",
                        "title": translate(f"{list(map(self.gestion_extension_de_fichier,list(data[i][2].split())))[0][1]}", lang),
                        "payload": f"__VOIR_EVENEMENT {data[i][0]} {id_stand} {data[i][2]} CONTENU_URL" if data[i][2].startswith("http")
                        else f"__VOIR_EVENEMENT {data[i][0]} {URL_SERVER}{id_stand}/{data[i][2]} CONTENU"
                    }
                ]
            }
            )
        return list_evenement

    def gestion_evenement_par_dix(
            self,
            dest_id,
            id_stand,
            lang,
            liste_evenement,
            page):
        res = liste_evenement
        deb_indice = (page - 1) * 10

        if len(res) > deb_indice + 10:
            self.bot.send_template(dest_id,
                                   res[deb_indice:deb_indice + 10],
                                   next=[{"content_type": "text",
                                          "title": "⏭️" + translate("page_suivant",
                                                                    lang).upper(),
                                          "payload": f"__EVENEMENTS {id_stand} {page+1}",
                                          },
                                         const.retoure("STAND_EMPLOI",
                                                       lang,
                                                       id_stand)])
        else:
            self.bot.send_template(
                dest_id,
                res[deb_indice:deb_indice + 10],
                next=[const.retoure("STAND_EMPLOI", lang, id_stand)]
            )

    def resultat_de_test_kavio(self, data):
        max = 0
        for i in range(len(data)):
            if max < data[i][1]:
                max = data[i][1]
            else:
                max = max

        categ_max = []
        for values in data:
            if values[1] == max:
                categ_max.append(
                    values[0]
                )
            pass
        return categ_max

    def resultat_generale(self, user_id, lang):
        diff_reponse = const.resultat_metier(
            self.resultat_de_test_kavio(
                self.req.interet_global(user_id)), lang)

        for i in range(len(diff_reponse)):
            self.bot.send_message(
                user_id,
                diff_reponse[i]
            )
