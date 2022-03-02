from messenger import Messenger
from requetes import Requete
from  conf import URL_SERVER
import const


class Options:
    
    def __init__(self, bot: Messenger, req: Requete):
        if not isinstance(bot, Messenger):
            raise Exception('bot doit être de type Messenger')
        self.bot = bot
        if not isinstance(req, Requete):
            raise Exception('req doit être de type Requete')
        self.req = req

    def listes_de_tout_fiches_metiers(self, data):
        """
            Methodes qui fetche tout les fiches
            metiers disponibles 
        """
        liste_des_fiches_metiers = []
        for i in range(len(data)):
            liste_des_fiches_metiers.append({
                    "title": f"{i+1} - {data[i][1].upper()}",
                    "image_url": URL_SERVER + data[i][2],
                    "buttons": [
                        {
                            "type": "postback",
                            "title":"VOIR",
                            "payload": f"__VOIR {data[i][0]} {URL_SERVER + data[i][2]} FICHE_METIER"
                        }
                    ]
                }              
            )
        return liste_des_fiches_metiers
    
    def gestion_de_liste_des_fiches_metier_par_dix(self, dest_id,
        liste_des_fiches_metiers, page, types, payload_plus_de_dix):
        '''
            methode gere à afficher les fiches metiers
            sous formes de templates par 10 affiches
        '''
        
        res = liste_des_fiches_metiers
        if res:
            deb_indice = (page - 1) * 10
            
            if types == "recherche":
                if len(res) > deb_indice + 10:
                    self.bot.send_template(
                        dest_id, res[deb_indice:deb_indice + 10],
                        next=[
                            {
                                "content_type": "text",
                                "title": "⏭️PAGE SUIVANTE",
                                "payload": f"{payload_plus_de_dix} {page+1}",
                            }
                        ]
                    )
                else:
                    self.bot.send_template(dest_id, res[deb_indice:deb_indice + 10])
        
            else:
                if len(res) > deb_indice + 10:
                    self.bot.send_template(
                        dest_id, res[deb_indice:deb_indice + 10],
                        next=[
                            {
                                "content_type": "text",
                                "title": "⏭️PAGE SUIVANTE",
                                "payload": f"{payload_plus_de_dix} {page+1}",
                            }
                        ]
                    )
                else:
                    self.bot.send_template(dest_id, res[deb_indice:deb_indice + 10])
        else:
            self.bot.send_message(dest_id, "Pas de fiche metier pour le moment ")
            
    def fiche_metier_par_domaine(self, user_id, domaine, page, payload_plus_de_dix=""):
        if not page.isdigit():
            self.bot.send_message(
                    user_id,
                    const.voir_liste_des_fiches_metiers(domaine.upper(),)
                ) 
        else:
            pass
        
        self.gestion_de_liste_des_fiches_metier_par_dix(
            user_id,
            self.listes_de_tout_fiches_metiers(
                self.req.fiche_metier_chaque_domaine(domaine=domaine)
            ),
            page=int(page) if page.isdigit() else 1,
            types="listage",
            payload_plus_de_dix=payload_plus_de_dix
        )
        
    def liste_de_tout_les_stands(self, data):
        liste_des_stands = []
        for i in range(len(data)):
            liste_des_stands.append({
                    "title": f"{data[i][2].upper()}",
                    "image_url": f"{URL_SERVER}{data[i][0]}/{data[i][1]}",
                    "buttons": [
                        {
                            "type": "postback",
                            "title":"VISITER",
                            "payload": f"__VISITER {data[i][0]}"
                        }
                    ]
                }
            )
            
        return liste_des_stands
    
    def gestion_de_stands_par_dix(self, dest_id, liste_des_stands, page):
        res = liste_des_stands
        if res:
            deb_indice = (page - 1) * 10

            if len(res) > deb_indice + 10:
                self.bot.send_template(
                    dest_id, res[deb_indice:deb_indice + 10],
                    next=[
                        {
                            "content_type": "text",
                            "title": "⏭️PAGE SUIVANTE",
                            "payload": f"__VOIR_LISTE_DU_STAND {page+1}",
                        }
                    ]
                )
            else:
                self.bot.send_template(dest_id, res[deb_indice:deb_indice + 10])
                
    def liste_galerie_de_chaque_stand(self, id_stand, data):
        liste_galerie = []
        for i in range(len(data)):
            liste_galerie.append({
                    "title": f"{i+1} - {data[i][1].upper()}",
                    "image_url": f"{URL_SERVER}{id_stand}/{data[i][2]}",
                    "buttons": [
                        {
                            "type": "postback",
                            "title":"VOIR L'IMAGE",
                            "payload": f"__VOIR {data[i][0]} {URL_SERVER}{id_stand}/{data[i][2]} CONTENU"
                        }
                    ]
                }
            )
            
        return liste_galerie
        
    def liste_emploi_de_chaque_stand(self, data, id_stand):
        liste_emploi = []
        for i in range(len(data)):
            liste_emploi.append({
                    "title": f"{i+1} - {data[i][1].upper()}",
                    "image_url": f"{URL_SERVER}{id_stand}/{data[i][2]}" if not data[i][2].endswith(".pdf") \
                        else "https://www.iconpacks.net/icons/2/free-pdf-download-icon-2617-thumb.png",
                    "buttons": [
                        {
                            "type": "postback",
                            "title":"VOIR" if not data[i][2].endswith(".pdf") else "TELECHARGER",
                            "payload": f"__VOIR_EMPLOI {data[i][0]} {URL_SERVER}{id_stand}/{data[i][2]} CONTENU"
                        }
                    ]
                }              
            )
        return liste_emploi

    def gestion_de_liste_demploi_par_dix(self, dest_id, id_stand, liste_emploi, page):
        res = liste_emploi
        deb_indice = (page - 1) * 10
        
        if len(res) > deb_indice + 10:
            self.bot.send_template(
                dest_id, res[deb_indice:deb_indice + 10],
                next=[
                    {
                        "content_type": "text",
                        "title": "⏭️PAGE SUIVANTE",
                        "payload": f"__EMPLOI {id_stand} {page+1}",
                    }
                ]
            )
        else:
            self.bot.send_template(dest_id, res[deb_indice:deb_indice + 10])

    def gestion_extension_de_fichier(self,fichier):
        if fichier.endswith(".pdf"):
            return "https://www.iconpacks.net/icons/2/free-pdf-download-icon-2617-thumb.png","TELECHARGER"
        elif fichier.endswith(".mp4"):
            return "https://icon-library.com/images/play-video-icon-png-transparent/play-video-icon-png-transparent-14.jpg","REGARDER"
        elif fichier.startswith("http"):
            return "https://www.kindpng.com/picc/m/256-2564683_transparent-link-website-transparent-website-link-logo-hd.png","VOIR"
        else:
            return "https://www.kindpng.com/picc/m/244-2446073_icons8-flat-gallery-icon-logo-gallery-png-transparent.png","VOIR"
        
    def liste_evenement_de_chaque_stand(self,id_stand,data):
        list_evenement = []
        for i in range(len(data)):            
            list_evenement.append({
                    "title": f"{i+1} - {data[i][1].upper()}",
                    "image_url": f"{list(map(self.gestion_extension_de_fichier,list(data[i][2].split())))[0][0]}",
                    "buttons": [
                        {
                            "type": "postback",
                            "title":f"{list(map(self.gestion_extension_de_fichier,list(data[i][2].split())))[0][1]}",
                            "payload":f"__VOIR_EVENEMENT {data[i][0]} {data[i][2]} CONTENU_URL" if data[i][2].startswith("http") \
                                else f"__VOIR_EVENEMENT {data[i][0]} {URL_SERVER}{id_stand}/{data[i][2]} CONTENU"
                        }
                    ]
                } 
            )
        return list_evenement
        
    def gestion_evenement_par_dix(self, dest_id, id_stand, liste_evenement, page):
        res = liste_evenement
        deb_indice = (page - 1) * 10
        
        if len(res) > deb_indice + 10:
            self.bot.send_template(
                dest_id, res[deb_indice:deb_indice + 10],
                next=[
                    {
                        "content_type": "text",
                        "title": "⏭️PAGE SUIVANTE",
                        "payload": f"__EVENEMENTS {id_stand} {page+1}",
                    }
                ]
            )
        else:
            self.bot.send_template(dest_id, res[deb_indice:deb_indice + 10])