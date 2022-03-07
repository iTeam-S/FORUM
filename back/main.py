import mysql.connector
from werkzeug.utils import secure_filename
# ---------------------------------------
from flask_cors import CORS
from flask import Flask, request, abort
from flask_bcrypt import check_password_hash, generate_password_hash
# ---------------------------------------
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_access_token
# ---------------------------------------
from datetime import timedelta
from time import time
import os
# ---------------------------------------
from conf import database
# ---------------------------------------


app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = "LUCIFER-MORNINGSTAR"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=12)
jwt = JWTManager(app)

DB = mysql.connector.connect(**database())
CURSOR = DB.cursor(buffered=True)


def verif_db(fonction):
    '''
        Un decorateur de verification de la
        connexion au serveur avant traitement.
    '''
    def trt_verif(*arg, **kwarg):
        if not DB.is_connected():
            DB.reconnect()
        return fonction(*arg, **kwarg)
    return trt_verif


# *************************** ERROR Handler *****************************
@app.errorhandler(404)
def page_not_found(e):
    return "Ressource Not Found", 404


@app.errorhandler(500)
def internal_server_error(e):
    return e, 500
# *************************** ___________ *****************************


@verif_db
@app.route("/api/v1/login", methods=['POST'])
def login():
    """
        DESC : Fonction permettant l'authentification d'un utilisateur
    """
    try:
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        if email and password:
            CURSOR.execute("SELECT * FROM Compte WHERE email=%s", (email,))
            if CURSOR.rowcount > 0:
                account = dict(zip(CURSOR.column_names, CURSOR.fetchone()))
                if check_password_hash(str(account.get("password")), password):
                    account.pop("password")
                    account["token"] = create_access_token(
                        str(str(account.get("id")) + "+" + account.get("type"))
                    )
                    return account, 200
            return {
                "error": True,
                "message": "Email/password incorrect"
            }, 412
        return {
            "error": True,
            "message": "Email/password manquants"
        }, 412

    except Exception as err:
        print(err)
        abort(500, description="Something went wrong !")


@verif_db
@app.route("/api/v1/add_account", methods=['POST'])
@jwt_required()
def add_account():
    """
        DESC : Fonction permettant d'ajouter un compte
        Juste pour les comptes  avec access admin
    """
    try:
        data = request.get_json()

        compte_id, access = get_jwt_identity().split("+")

        nom = data.get("nom")
        email = data.get("email")
        tel = data.get("tel")
        domaine = data.get("domaine")
        password = data.get("password")
        adresse = data.get("adresse")
        type = data.get("type")
        lien = data.get("lien")

        if access == "admin":
            if nom and email and type and lien and password:
                CURSOR.execute("SELECT * FROM Compte WHERE email=%s", (email,))
                if CURSOR.rowcount < 1:
                    password = str(generate_password_hash(password).decode())
                    CURSOR.execute("""
                        INSERT INTO
                            Compte(nom, tel, email, type, lien, domaine, password, adresse)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """, (nom, tel, email, type, lien, domaine, password, adresse)
                    )
                    DB.commit()

                    return {
                        "error": False,
                        "message": "Account created"
                    }, 200

                return {
                        "error": False,
                        "message": "Email already exists."
                }, 409

            return {
                "error": True,
                "message": "Données obligatoires manquants"
            }, 412

        return {
            "error": True,
            "message": "Pas d'access"
        }, 403

    except Exception as err:
        print(err)
        abort(500, description="Something went wrong !")


@verif_db
@app.route("/api/v1/add_content", methods=['POST'])
@jwt_required()
def add_content():
    """
        DESC : Fonction permettant d'ajouter du contenu
    """
    try:
        compte_id, access = get_jwt_identity().split("+")

        titre = request.form.get("titre")
        description = request.form.get("description")
        type = request.form.get("type")

        if 'file' not in request.files:
            fichier = request.files['file']
            filename = str(time.time()) + '_' + secure_filename(fichier.name)
            fichier.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        if titre and type and compte_id:
            CURSOR.execute("""
                INSERT INTO
                    Contenu(titre, description, type, fichier, compte_id)
                    VALUES (%s, %s, %s, %s, %s)
                """, (titre, description, type, filename, compte_id)
            )
            DB.commit()

            return {
                "error": False,
                "message": "Contenu inserted"
            }, 200

        return {
            "error": True,
            "message": "Donnees obligatoires manquants"
        }, 412

    except Exception as err:
        print(err)
        abort(500, description="Something went wrong !")


@verif_db
@app.route("/api/v1/add_fiche_metier", methods=['POST'])
@jwt_required()
def add_fiche_metier():
    """
        DESC : Fonction permettant d'ajouter des fiche metier
        Juste pour les comptes  avec access admin
    """
    try:
        compte_id, access = get_jwt_identity().split("+")

        titre = request.form.get("titre")
        domaine_id = request.form.get("domaine_id")

        if 'file' not in request.files:
            fichier = request.files['file']
            filename = str(time.time()) + '_' + secure_filename(fichier.name)
            fichier.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        if access == "admin":
            if titre and domaine_id and id:
                CURSOR.execute("""
                    INSERT INTO
                        Contenu(titre, fichier, compte_id, domaine_id)
                        VALUES (%s, %s, %s)
                    """, (titre, filename, compte_id, domaine_id)
                )
                DB.commit()

                return {
                    "error": False,
                    "message": "Contenu inserted"
                }, 200

            return {
                "error": True,
                "message": "Donnees obligatoires manquants"
            }, 412

    except Exception as err:
        print(err)
        abort(500, description="Something went wrong !")


@verif_db
@app.route("/api/v1/list_accounts", methods=['GET'])
@jwt_required()
def list_accounts():
    """
        DESC : Fonction permettant d'obtenir la liste
        des comptes entreprises existants
        Juste pour les comptes  avec access admin
    """
    try:
        compte_id, access = get_jwt_identity().split("+")

        if access == "ADMIN":
            CURSOR.execute("""
                SELECT
                    nom, tel, email, type, lien, domaine, adresse
                FROM
                    Compte;
            """)
            accounts = CURSOR.fetchall()

            if accounts:
                return {
                    accounts.index(account):
                        dict(
                            zip(CURSOR.column_names, account)
                        ) for account in accounts
                }, 200
            else:
                return {
                    "error": False,
                    "message": "No account finded!"
                }, 200
        return {
            "error": True,
            "message": "Pas d'access admin"
        }, 403

    except Exception as err:
        print(err)
        abort(500, description="Something went wrong !")


if __name__ == "__main__":
    app.run(debug=True)
