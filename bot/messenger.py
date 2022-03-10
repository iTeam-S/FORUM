import requests
from  retry import retry
from utils import translate


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
    def send_quick_reply(self, dest_id, lang, types, *args):
        self.send_action(dest_id, 'typing_on')
        '''
            Envoie des quick reply messenger
        '''
        if types == "bienvenue":
            text = translate("bienvenu",lang)
            quick_rep = [
                {
                    "content_type": "text",
                    "title": "📑" + translate("fiches_metiers",lang).upper(),
                    "payload": "__FICHE_METIER"
                },
                {
                    "content_type": "text",
                    "title": "🏠" + translate("visiter_stands",lang).upper(),
                    "payload": "__VISITE_STAND"
                },
                {
                    "content_type": "text",
                    "title": "🔶" + translate("kavio",lang).upper(),
                    "payload": "__TEST_KAVIO"
                }
            ]
        
        elif types == "choix_langues":
            text = translate('choisir_votre_langue', lang)
            quick_rep = [
                {
                    "content_type": "text",
                    "title": 'FR 🇫🇷',
                    "payload": "__SET_LANG fr",
                },
                {
                    "content_type": "text",
                    "title": 'EN 🇬🇧',
                    "payload": "__SET_LANG en",
                },
                {
                    "content_type": "text",
                    "title": 'MG 🇲🇬',
                    "payload": "__SET_LANG mg",
                }
            ]
        
        elif types == "tester_kavio":
            text = translate("idee_commencer_kavio",lang)
            quick_rep = [
                {
                    "content_type": "text",
                    "title":"😍" + translate("faire_test_kavio",lang).upper(),
                    "payload": "__FAIRE_KAVIO",
                },
                {
                    "content_type": "text",
                    "title":"😉" + translate("abandomner_test_kavio",lang).upper(),
                    "payload": "__ABANDON_KAVIO",
                }
            ]

        elif types == "recherche_ou_voir_fiche_metier":
            text = translate("recherche_ou_voir_fiche_metier",lang)
            quick_rep = [
                {
                    "content_type": "text",
                    "title": "🔍" + translate("rechercher",lang).upper(),
                    "payload": "__RECHERCHE_FICHE_METIER"
                },
                {
                    "content_type": "text",
                    "title": "📑" + translate("voir_les_listes",lang).upper(),
                    "payload": "__VOIR_LISTE_FICHE_METIER"
                }
            ]

        elif types == "domaine_de_fiche_metier":
            text = translate("domaine_de_fiche_metier",lang)
            quick_rep = [
                {
                    "content_type": "text",
                    "title": translate("sante",lang).upper(),
                    "image_url":"https://e7.pngegg.com/pngimages/291/741/png-clipart-blue-wikipedia-wikimedia-commons-blue-dots-miscellaneous-blue.png",
                    "payload": "__SANTE"
                },
                {
                    "content_type": "text",
                    "title": translate("informatique",lang).upper(),
                    "image_url":"https://e7.pngegg.com/pngimages/291/741/png-clipart-blue-wikipedia-wikimedia-commons-blue-dots-miscellaneous-blue.png",
                    "payload": "__INFORMATIQUE"
                },
                {
                    "content_type": "text",
                    "title":translate("comm_et_admin",lang).upper(),
                    "image_url":"https://e7.pngegg.com/pngimages/291/741/png-clipart-blue-wikipedia-wikimedia-commons-blue-dots-miscellaneous-blue.png",
                    "payload": "__COMMERCE"
                },
                {
                    "content_type": "text",
                    "title": "🟢" + translate("agronomie",lang).upper(),
                    "payload": "__AGRONOMIE"
                },
                {
                    "content_type": "text",
                    "title": "🔴" + translate("science_humaine",lang).upper(),
                    "payload": "__SCIENCE_HUMAINE"
                },
                {
                    "content_type": "text",
                    "title": "🟠" + translate("tourisme",lang).upper(),
                    "payload": "__TOURISME"
                },
                {
                    "content_type": "text",
                    "title": "🟣" + translate("industrie",lang).upper(),
                    "payload": "__INDISTRUE"
                },
                {
                    "content_type": "text",
                    "title": "🟡" + translate("justice",lang).upper(),
                    "payload": "__JUSTICE"
                }   
            ]
            
        elif types == "rechercher_ou_visiter_stands":
            text = translate("rechercher_ou_visiter_stands",lang)
            quick_rep = [
                {
                    "content_type": "text",
                    "title": "🔍" + translate("rechercher",lang).upper(),
                    "payload": "__RECHERCHE_STAND"
                },
                {
                    "content_type": "text",
                    "title": "📜" + translate("voir_les_listes",lang).upper(),
                    "payload": "__VOIR_LISTE_DU_STAND"
                }
            ]
        
        elif types == "visiter_stand":
            for argument in args:
                id_stand = argument
                
            text = translate("visiter_stand",lang)
            quick_rep = [
                {
                    "content_type": "text",
                    "title": "" + translate("offre",lang).upper(),
                    "image_url":"https://png.pngtree.com/png-clipart/20210617/ourlarge/pngtree-job-vacancy-logo-with-finding-glass-png-image_3469306.jpg",
                    "payload": f"__EMPLOI {id_stand} page"
                },
                {
                    "content_type": "text",
                    "title": "📜" + translate("info",lang).upper(),
                    "payload": f"__EVENEMENTS {id_stand} page"
                },
                {
                    "content_type": "text",
                    "title": "🖼️" + translate("galerie",lang).upper(),
                    "payload": f"__GALERIE {id_stand}" 
                },
                {
                    "content_type": "text",
                    "title": "🏢" + translate("presentation",lang).upper(),
                    "payload": f"__PRESENTATION {id_stand}" 
                },
                {
                    "content_type": "text",
                    "title": "📠" + translate("plus_info",lang).upper(),
                    "payload": f"__INFO {id_stand}" 
                }   
            ]
        elif types == "fini_test_kavio":
            text = translate("fini_test_kavio_question",lang)
            quick_rep = [
                {
                    "content_type": "text",
                    "title": "😍" + translate("voir_resultat",lang).upper(),
                    "payload": "__VOIR_RESULTAT"
                },
                {
                    "content_type": "text",
                    "title": "➕" + translate("recommencer",lang).upper(),
                    "payload": "__FAIRE_KAVIO"
                }
            ]
            
        else:
            return
            
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

        return requests.post(
            self.url + '/messages',
            json=dataJSON,
            headers=header,
            params=params
        )

    @retry(requests.exceptions.ConnectionError, tries=3, delay=3)
    def send_media(self,destId,url_facebook,types):
        """
            Methode qui envoye des fichiers
            media comme image et video 
            par lien facebook
        """
        self.send_action(destId, 'typing_on')
        dataJSON = {
            "recipient":{
                "id": destId
            },
            "message":{
                "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "media",
                    "elements": [
                        {
                        "media_type": types,
                        "url": url_facebook
                        }
                    ]
                }
            }    
            }
        }

        header = {'content-type': 'application/json; charset=utf-8'}
        params = {"access_token": self.token}
        self.send_action(destId, 'typing_off')

        return requests.post(
            'https://graph.facebook.com/v2.6/me/messages',
            json=dataJSON,
            headers=header,
            params=params
        )

    
    @retry(requests.exceptions.ConnectionError, tries=3, delay=3)
    def send_quick_kavio(self, dest_id, types, **kwargs):

        self.send_action(dest_id, 'typing_on')
        data_json = {
            'messaging_type': "RESPONSE",
            'recipient': {
                "id": dest_id
            },

            'message': {
                'text': kwargs.get("kavio").get("text"),
                'quick_replies': f"[{kwargs.get('kavio').get('quick_rep')[1]}]" if types==1 \
                else kwargs.get("kavio").get("quick_rep")
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