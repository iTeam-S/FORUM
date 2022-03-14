import mysql.connector
from conf import DATABASE


class Requete:

    def __init__(self):
        '''
            Initialisation: Connexion à la base de données
        '''
        self.__connect()

    def __connect(self):
        self.db = mysql.connector.connect(**DATABASE)
        self.cursor = self.db.cursor()

    def verif_db(fonction):
        '''
            Un decorateur de verification de la
            connexion au serveur avant traitement.
        '''

        def trt_verif(*arg, **kwarg):
            if not arg[0].db.is_connected():
                # reconnexion de la base
                try:
                    arg[0].db.reconnect()
                except Exception:
                    arg[0].__connect()
            return fonction(*arg, **kwarg)

        return trt_verif

    @verif_db
    def verif_utilisateur(self, user_id):
        '''
            Fonction d'insertion du nouveau utilisateur
            et/ou mise à jour de la date de dernière utilisation.
        '''
        # Insertion dans la base si non present
        # Mise à jour du last_use si déja présent
        req = '''
            INSERT INTO Public(facebook_id, date_mp) VALUES (%s, NOW())
            ON DUPLICATE KEY UPDATE date_mp = NOW()
        '''
        self.cursor.execute(req, (user_id,))
        self.db.commit()

    @verif_db
    def get_user_lang(self, user_id):
        req = "SELECT lang FROM Public WHERE facebook_id = %s"
        self.cursor.execute(req, (user_id,))
        data = self.cursor.fetchone()[0]
        self.db.commit()
        return data

    @verif_db
    def update_lang(self, user_id, lang):
        req = "UPDATE Public SET lang = %s WHERE facebook_id = %s"
        self.cursor.execute(req, (lang, user_id))
        self.db.commit()

    @verif_db
    def set_action(self, user_id, action):
        '''
            Definir l'action de l'utilisateur
        '''
        req = 'UPDATE Public SET action = %s WHERE facebook_id = %s'
        self.cursor.execute(req, (action, user_id))
        self.db.commit()

    @verif_db
    def set_temp(self, user_id, temp):
        req = 'UPDATE Public SET temp = %s WHERE facebook_id = %s'
        self.cursor.execute(req, (temp, user_id))
        self.db.commit()

    @verif_db
    def get_action(self, user_id):
        '''
            Recuperer l'action de l'utilisateur
        '''
        req = 'SELECT action FROM Public WHERE facebook_id = %s'
        self.cursor.execute(req, (user_id,))
        data = self.cursor.fetchone()[0]
        self.db.commit()
        return data

    @verif_db
    def get_temp(self, user_id):
        '''
            Recuperer le temp de l'utilisateur
        '''
        req = 'SELECT temp FROM Public WHERE facebook_id = %s'
        self.cursor.execute(req, (user_id,))
        data = self.cursor.fetchone()[0]
        self.db.commit()
        return data

    @verif_db
    def fiche_metier_chaque_domaine(self, domaine):
        '''
            Récuperer tous les fiches métier
            pour l'option "VOIR LISTE" pour
            chaque domaine
        '''
        req = """
            SELECT f.id,f.titre,f.fichier
            FROM Fiche_metier f
            JOIN Domaine d ON f.domaine_id = d.id
            WHERE nom = %s
        """
        self.cursor.execute(req, (domaine,))
        data = self.cursor.fetchall()
        self.db.commit()
        return data

    @verif_db
    def inserer_consultation(self, user_id, contenu, types):
        req = """
            INSERT INTO Consultation(id,date,type,dimension)
            VALUES((SELECT id FROM Public WHERE facebook_id = %s)
            ,CURDATE(),%s,%s)
        """
        self.cursor.execute(req, (user_id, types, contenu))
        self.db.commit()

    @verif_db
    def rechercher_fiche_metier(self, query):
        req = """
                SELECT id,titre,fichier
                FROM Fiche_metier
                WHERE LOWER(titre) LIKE %s
                OR SOUNDEX(titre)=SOUNDEX(%s)
        """
        self.cursor.execute(req, (f"%{query.lower()}%", query))
        data = self.cursor.fetchall()
        self.db.commit()
        return data

    @verif_db
    def tous_les_stands(self):
        req = """
            SELECT id,logo,nom,description
            FROM Compte
            WHERE type = "ENTREPRISE"
            ORDER BY classe ASC
        """
        self.cursor.execute(req)
        data = self.cursor.fetchall()
        self.db.commit()
        return data

    @verif_db
    def rechercher_fiche_stands(self, query):
        req = """
                SELECT id,logo,nom,description
                FROM Compte
                WHERE (LOWER(nom) LIKE %s
                OR SOUNDEX(nom)=SOUNDEX(%s))
                AND type = "ENTREPRISE"
                LIMIT 10
        """
        self.cursor.execute(req, (f"%{query.lower()}%", query))
        data = self.cursor.fetchall()
        self.db.commit()
        return data

    @verif_db
    def informations_de_chaque_stand(self, id_stand):
        req = """
                SELECT tel,email,lien,adresse,description
                FROM Compte
                WHERE Id = %s
        """
        self.cursor.execute(req, (id_stand,))
        data = self.cursor.fetchall()
        self.db.commit()
        return data

    @verif_db
    def galerie_de_chaque_stand(self, id_stand):
        req = """
            SELECT id,titre,fichier
            FROM Contenu
            WHERE type = "galerie"
            AND compte_id = %s
        """
        self.cursor.execute(req, (id_stand,))
        data = self.cursor.fetchall()
        self.db.commit()
        return data

    @verif_db
    def presentation_stand(self, id_stand):
        req = """
                SELECT video
                FROM Compte
                WHERE Id = %s
        """
        self.cursor.execute(req, (id_stand,))
        data = self.cursor.fetchone()[0]
        self.db.commit()
        return data

    @verif_db
    def verification_consultation(self, id_user, types, dimension):
        req = """
            SELECT 1 FROM Consultation
            WHERE id = (SELECT id FROM Public WHERE facebook_id = %s)
            AND  type = %s
            AND dimension = %s
            AND date = CURDATE()
        """
        self.cursor.execute(req, (id_user, types, dimension))
        data = self.cursor.fetchone()
        self.db.commit()
        return data

    @verif_db
    def emploi_de_chaque_stands(self, id_stand):
        req = """
            SELECT id, titre, fichier
            FROM Contenu
            WHERE type = "emploi"
            AND compte_id = %s
        """
        self.cursor.execute(req, (id_stand,))
        data = self.cursor.fetchall()
        self.db.commit()
        return data

    @verif_db
    def description_de_chaque_contenu(self, id_contenu):
        req = "SELECT description FROM Contenu WHERE id= %s"
        self.cursor.execute(req, (id_contenu,))
        data = self.cursor.fetchone()
        self.db.commit()
        return data

    @verif_db
    def evenement_chaque_stand(self, id_stand):
        req = """
            SELECT id, titre,fichier
            FROM Contenu
            WHERE type = "evenement"
            AND compte_id = %s
        """
        self.cursor.execute(req, (id_stand,))
        data = self.cursor.fetchall()
        self.db.commit()
        return data

    @verif_db
    def insert_kavio(
        self, id_user, num_question, id_part, serie, categorie, point
    ):
        req = """
            INSERT into Test_KAVIO(
                id_user,
                num_question,
                id_part,
                serie,
                categorie,
                point)
            VALUES(
                (SELECT id FROM Public WHERE facebook_id = %s),%s,%s,%s,%s,%s
            )
        """
        self.cursor.execute(req, (
            id_user, num_question, id_part, serie, categorie, point))
        self.db.commit()

    @verif_db
    def verif_trois_vrai(self, id_part, serie):
        req = """
            SELECT COUNT(point)
            FROM Test_KAVIO
            WHERE id_part=%s
            AND serie=%s
            AND point=1
        """
        self.cursor.execute(req, (id_part, serie))
        data = self.cursor.fetchone()[0]
        self.db.commit()
        return data
