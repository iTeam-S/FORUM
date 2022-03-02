import requests
from  retry import retry


class Messenger:

    def __init__(self, access_token):
        self.token = access_token
        self.url = "https://graph.facebook.com/v12.0/me"

    @retry(requests.exceptions.ConnectionError, tries=3, delay=3)
    def send_action(self, dest_id, action):
        """
            Cette fonction sert à simuler un action sur les messages.
            exemple: vue, en train d'ecrire.
            Action dispo: ['mark_seen', 'typing_on', 'typing_off']
        """

        data_json = {
            'messaging_type': "RESPONSE",
            'recipient': {
                "id": dest_id
            },
            'sender_action': action
        }

        header = {'content-type': 'application/json; charset=utf-8'}
        params = {"access_token": self.token}

        return requests.post(
            self.url + '/messages',
            json=data_json,
            headers=header,
            params=params
        )
        
    @retry(requests.exceptions.ConnectionError, tries=3, delay=3)
    def send_message(self, dest_id, message):
        self.send_action(dest_id, 'typing_on')
        """
            Cette fonction sert à envoyer une message texte
            à un utilisateur donnée
        """
        data_json = {
            'recipient': {
                "id": dest_id
            },
            'message': {
                "text": message
            }
        }

        header = {'content-type': 'application/json; charset=utf-8'}
        params = {"access_token": self.token}

        res = requests.post(
            self.url + '/messages',
            json=data_json,
            headers=header,
            params=params
        )
        self.send_action(dest_id, 'typing_off')
        return res

    @retry(requests.exceptions.ConnectionError, tries=3, delay=3)
    def send_quick_reply(self, dest_id, types, *args):
        self.send_action(dest_id, 'typing_on')
        '''
            Envoie des quick reply messenger
        '''
        if types == "bienvenue":
            text = "Vous voulez faire qoui maintenant?"
            quick_rep = [
                {
                    "content_type": "text",
                    "title": "📑VOIR FICHES METIERS",
                    "payload": "__FICHE_METIER"
                },
                {
                    "content_type": "text",
                    "title": "📑VISITER DES STANDS",
                    "payload": "__VISITE_STAND"
                }
            ]
        
        elif types == "recherche_ou_voir_fiche_metier":
            text = "Vous voulez rechercher ou voir les listes du fichie metier?"
            quick_rep = [
                {
                    "content_type": "text",
                    "title": "🔍RECHERCHER",
                    "payload": "__RECHERCHE_FICHE_METIER"
                },
                {
                    "content_type": "text",
                    "title": "📑VOIR LES LISTES",
                    "payload": "__VOIR_LISTE_FICHE_METIER"
                }
            ]

        elif types == "domaine_de_fiche_metier":
            text = "Voici donc les domaines ou les filières du fiche metier disponible\n\nVous pouvez choisir ce que vous voulez!!"
            quick_rep = [
                {
                    "content_type": "text",
                    "title": "SANTÉ",
                    "image_url":"https://e7.pngegg.com/pngimages/291/741/png-clipart-blue-wikipedia-wikimedia-commons-blue-dots-miscellaneous-blue.png",
                    "payload": "__SANTE"
                },
                {
                    "content_type": "text",
                    "title": "INFORMATIQUE",
                    "image_url":"https://e7.pngegg.com/pngimages/291/741/png-clipart-blue-wikipedia-wikimedia-commons-blue-dots-miscellaneous-blue.png",
                    "payload": "__INFORMATIQUE"
                },
                {
                    "content_type": "text",
                    "title": "COMMERCE ET\nADMINISTRATION",
                    "image_url":"https://e7.pngegg.com/pngimages/291/741/png-clipart-blue-wikipedia-wikimedia-commons-blue-dots-miscellaneous-blue.png",
                    "payload": "__COMMERCE"
                },
                {
                    "content_type": "text",
                    "title": "🟢AGRONOMIE",
                    "payload": "__AGRONOMIE"
                },
                {
                    "content_type": "text",
                    "title": "🔴SCIENCES HUMAINES ET\nCOMMUNICATION",
                    "payload": "__SCIENCE_HUMAINE"
                },
                {
                    "content_type": "text",
                    "title": "🟠TOURISME",
                    "payload": "__TOURISME"
                },
                {
                    "content_type": "text",
                    "title": "🟣INDUSTRIE ET BT",
                    "payload": "__INDISTRUE"
                },
                {
                    "content_type": "text",
                    "title": "🟡JUSTICE ET FORCE DE L'ORDRE",
                    "payload": "__JUSTICE"
                }   
            ]
            
        elif types == "rechercher_ou_visiter_stands":
            text = "Rechercher ou voir tout les listes du stand?"
            quick_rep = [
                {
                    "content_type": "text",
                    "title": "🔍RECHERCHER",
                    "payload": "__RECHERCHE_STAND"
                },
                {
                    "content_type": "text",
                    "title": "📜VOIR LES LISTES",
                    "payload": "__VOIR_LISTE_DU_STAND"
                }
            ]
        
        elif types == "visiter_stand":
            for argument in args:
                id_stand = argument
                
            text = "Que-ce que vous voulez voir maintenant alors?"
            quick_rep = [
                {
                    "content_type": "text",
                    "title": "OFFRE D'EMPLOI",
                    "image_url":"https://png.pngtree.com/png-clipart/20210617/ourlarge/pngtree-job-vacancy-logo-with-finding-glass-png-image_3469306.jpg",
                    "payload": f"__EMPLOI {id_stand} page"
                },
                {
                    "content_type": "text",
                    "title": "📜INFORMATIONS",
                    "payload": f"__EVENEMENTS {id_stand} page"
                },
                {
                    "content_type": "text",
                    "title": "🖼️GALERIE",
                    "payload": f"__GALERIE {id_stand}" 
                },
                {
                    "content_type": "text",
                    "title": "🏢PRESENTATION",
                    "payload": f"__PRESENTATION {id_stand}" 
                },
                {
                    "content_type": "text",
                    "title": "📠PLUS D'INFO",
                    "payload": f"__INFO {id_stand}" 
                }   
            ]
            
        data_json = {
            'messaging_type': "RESPONSE",
            'recipient': {
                "id": dest_id
            },

            'message': {
                'text': text,
                'quick_replies': quick_rep
            }
        }

        header = {'content-type': 'application/json; charset=utf-8'}
        params = {"access_token": self.token}
        
        self.send_action(dest_id, 'typing_off')
        return requests.post(
            self.url + '/messages',
            json=data_json,
            headers=header,
            params=params
        )

    @retry(requests.exceptions.ConnectionError, tries=3, delay=3)
    def send_template(self, destId, elements, **kwargs):
        self.send_action(destId, 'typing_on')
        '''
            Envoi des produits sous forme templates

        '''
        self.send_action(destId, 'typing_on')
        dataJSON = {
            'messaging_type': "RESPONSE",
            'recipient': {
                "id": destId
            },
            'message': {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": elements,
                    },
                },
            }
        }

        if kwargs.get("next"):
            dataJSON['message']['quick_replies'] = kwargs.get("next")

        header = {'content-type': 'application/json; charset=utf-8'}
        params = {"access_token": self.token}
        self.send_action(destId, 'typing_off')

        return requests.post(
            self.url + '/messages', json=dataJSON,
            headers=header, params=params
        )

    @retry(requests.exceptions.ConnectionError, tries=3, delay=3)
    def send_file_url(self, destId, url, filetype='file'):
        self.send_action(destId, 'typing_on')
        '''
            Envoyé piece jointe par lien.
        '''
        self.send_action(destId, 'typing_on')
        dataJSON = {
            'messaging_type': "RESPONSE",
            'recipient': {
                "id": destId
            },
            'message': {
                'attachment': {
                    'type': filetype,
                    'payload': {
                        "url": url,
                        "is_reusable": True
                    }
                }
            }
        }
        header = {'content-type': 'application/json; charset=utf-8'}
        params = {"access_token": self.token}
        self.send_action(destId, 'typing_off')
        self.send_action(destId, 'typing_off')

        return requests.post(
            self.url + '/messages',
            json=dataJSON,
            headers=header,
            params=params
        )