from pathlib import Path
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
import time
import os
# ---------------------------------------
from conf import database
# ---------------------------------------

app = Flask(__name__)
CORS(app)

# ------------UPLOAD FOLDER CONF---------------
path = os.getcwd()
if not os.path.isdir('data'):
    os.makedirs('data/')

UPLOAD_FOLDER = os.path.join(path, 'data/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# ---------------------------------------------

# ----------------TOKEN CONFIG-----------------
app.config["JWT_SECRET_KEY"] = "LUCIFER-MORNINGSTAR"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)
jwt = JWTManager(app)
# ---------------------------------------------

# --------------DATABASE CONNECT---------------
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
# ---------------------------------------------


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

        if access == "ADMIN":
            if nom and email and type and lien and password:
                CURSOR.execute("SELECT * FROM Compte WHERE email=%s", (email,))
                if CURSOR.rowcount < 1:
                    password = str(generate_password_hash(password).decode())
                    CURSOR.execute(
                        """
                        INSERT INTO
                            Compte(
                                nom, tel, email, type, lien,
                                domaine, password, adresse
                            )
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        (
                            nom, tel, email, type, lien,
                            domaine, password, adresse
                        )
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
        compte_id = get_jwt_identity().split("+")[0]

        filename = None
        titre = request.form.get("titre")
        description = request.form.get("description")
        type = request.form.get("type")

        if request.files:
            fichier = request.files['file']
            compte_folder = os.path.join(
                app.config['UPLOAD_FOLDER'], str(compte_id)
            )
            Path(compte_folder).mkdir(parents=True, exist_ok=True)

            filename = str(time.time()) + '_' + secure_filename(
                fichier.filename)

            fichier.save(
                os.path.join(compte_folder, filename)
            )

        if titre and type and compte_id:
            CURSOR.execute("""
                INSERT INTO
                    Contenu(titre, description, type, fichier, compte_id)
                    VALUES (%s, %s, %s, %s, %s)
                """, (titre, description, type, filename or None, compte_id)
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

        filename = None
        titre = request.form.get("titre")
        domaine_id = request.form.get("domaine_id")

        if request.files:
            fichier = request.files['file']

            compte_folder = os.path.join(
                app.config['UPLOAD_FOLDER'], str(compte_id)
            )
            Path(compte_folder).mkdir(parents=True, exist_ok=True)

            filename = str(time.time()) + '_' + secure_filename(
                fichier.filename)
            fichier.save(
                os.path.join(compte_folder, filename)
            )

        if access == "ADMIN":
            if titre and domaine_id:
                CURSOR.execute("""
                    INSERT INTO
                        Fiche_metier(titre, fichier, domaine_id, compte_id)
                        VALUES (%s, %s, %s, %s)
                    """, (titre, filename, domaine_id, compte_id)
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


# -------------------- GET LIST API ----------------
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
        access = get_jwt_identity().split("+")[1]

        if access == "ADMIN":
            CURSOR.execute("""
                SELECT
                   id, nom, tel, email, type, lien, logo , domaine, adresse
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


@verif_db
@app.route("/api/v1/list_contents", methods=['GET'])
@jwt_required()
def list_contents():
    """
        DESC : Fonction permettant d'obtenir la liste
        des contenus d'un stands
    """
    try:
        compte_id = get_jwt_identity().split("+")[0]

        if compte_id:
            CURSOR.execute("""
                SELECT
                    id, titre, description, type, fichier
                FROM
                    Contenu
                WHERE
                    compte_id=%s;
            """, (compte_id,))
            contents = CURSOR.fetchall()
            if contents:
                return {
                    contents.index(content):
                        dict(
                            zip(CURSOR.column_names, content)
                        ) for content in contents
                }, 200
            else:
                return {
                    "error": False,
                    "message": "No content finded!"
                }, 200
        return {
            "error": True,
            "message": "Pas d'access"
        }, 403

    except Exception as err:
        print(err)
        abort(500, description="Something went wrong !")


# ---------------------------------------------------
@verif_db
@app.route("/api/v1/list_fiche_metier", methods=['GET'])
@jwt_required()
def list_fiche_metier():
    """
        DESC : Fonction permettant d'obtenir la liste
        listes des fiches metiers
    """
    try:
        access = get_jwt_identity().split("+")[1]

        if access == "ADMIN":
            CURSOR.execute("""
                SELECT
                    id, titre, fichier
                FROM
                    Fiche_metier;
            """)
            fiche_metiers = CURSOR.fetchall()

            if fiche_metiers:
                return {
                    fiche_metiers.index(fiche_metier):
                        dict(
                            zip(CURSOR.column_names, fiche_metier)
                        ) for fiche_metier in fiche_metiers
                }, 200
            else:
                return {
                    "error": False,
                    "message": "No Fiche Metier finded!"
                }, 200
        return {
            "error": True,
            "message": "Pas d'access admin"
        }, 403

    except Exception as err:
        print(err)
        abort(500, description="Something went wrong !")


@verif_db
@app.route("/api/v1/delete_content", methods=['DELETE'])
@jwt_required()
def delete_content():
    """
        DESC : Fonction permettant de supprimer un contenu
    """
    try:
        compte_id, access = get_jwt_identity().split("+")
        content_id = request.get_json().get("content_id")

        if compte_id:
            try:
                CURSOR.execute("""
                    DELETE FROM
                        Contenu
                    WHERE
                        id=%s AND compte_id=%s;
                """, (content_id, compte_id))

                DB.commit()

                return {
                    "error": False,
                    "message": "Content Deleted!"
                }, 200
            except Exception as err:
                print(err)
                DB.close()
                return {
                    "error": True,
                    "message": "le contenu est encore utilisé !"
                }, 400

        return {
            "error": True,
            "message": "Pas d'access admin"
        }, 403

    except Exception as err:
        print(err)
        abort(500, description="Something went wrong !")


@verif_db
@app.route("/api/v1/delete_account", methods=['DELETE'])
@jwt_required()
def delete_account():
    """
        DESC : Fonction permettant de supprimer
        un compte de stand
    """
    try:
        access = get_jwt_identity().split("+")[1]
        data = request.get_json()
        print(data)
        if data:
            account_id = data.get("compte_id")
        else:
            return {
                "error": True,
                "message": "Pas de compte à suprimmé"
            }, 400

        if access == "ADMIN" and account_id:
            try:
                CURSOR.execute("""
                    DELETE FROM
                        Compte
                    WHERE
                        id=%s;
                """, (account_id,))

                DB.commit()

                return {
                    "error": False,
                    "message": "Account Deleted!"
                }, 200
            except Exception as err:
                print(err)
                return {
                    "error": True,
                    "message": "le compte est encore utilisé !"
                }, 400

        return {
            "error": True,
            "message": "Pas d'access admin"
        }, 403

    except Exception as err:
        print(err)
        abort(500, description="Something went wrong !")


@verif_db
@app.route("/api/v1/delete_fiche_metier", methods=['DELETE'])
@jwt_required()
def delete_fiche_metier():
    """
        DESC : Fonction permettant de supprimer un
        Fiche Metier
    """
    try:
        access = get_jwt_identity().split("+")[1]
        fiche_metier_id = request.get_json().get("fiche_metier_id")

        if access == "ADMIN":
            try:
                CURSOR.execute("""
                    DELETE FROM
                        Fiche_metier
                    WHERE
                        id=%s;
                """, (fiche_metier_id))

                DB.commit()

                return {
                    "error": False,
                    "message": "Fiche Metier Deleted!"
                }, 200
            except Exception as err:
                print(err)
                DB.close()
                return {
                    "error": True,
                    "message": "le fiche metier est encore utilisé !"
                }, 400

        return {
            "error": True,
            "message": "Pas d'access admin"
        }, 403

    except Exception as err:
        print(err)
        abort(500, description="Something went wrong !")


@verif_db
@app.route("/api/v1/update_account/", methods=['PATCH'])
@jwt_required()
def update_account():
    """
        DESC : Fonction permettant de mettre à jour
        les données du compte
    """
    try:
        compte_id = get_jwt_identity().split("+")[0]
        data = request.get_json()

        if compte_id:
            account = (
                data.get("nom"),
                data.get("email"),
                data.get("tel"),
                data.get("domaine"),
                str(
                    generate_password_hash(
                        str(data.get("password"))).decode()),
                data.get("adresse"),
                data.get("type"),
                data.get("lien"),
                compte_id
            )
            try:
                CURSOR.execute("""
                    UPDATE
                        Compte
                    SET
                        nom = %s,
                        email = %s,
                        tel = %s,
                        domaine = %s,
                        password = %s,
                        adresse = %s,
                        type = %s,
                        lien = %s,

                    WHERE
                        id=%s;
                """, account)

                DB.commit()

                return {
                    "error": False,
                    "message": "Account Updated!"
                }, 200
            except Exception as err:
                print(err)
                DB.close()
                return {
                    "error": True,
                    "message": "le Compte est encore utilisé !"
                }, 400

        return {
            "error": True,
            "message": "Pas d'access"
        }, 403

    except Exception as err:
        print(err)
        abort(500, description="Something went wrong !")


@verif_db
@app.route("/api/v1/update_content/", methods=['PATCH'])
@jwt_required()
def update_content():
    """
        DESC : Fonction permettant de mettre à jour
        les infos sur un contenus
    """
    try:
        compte_id = get_jwt_identity().split("+")[0]
        data = request.get_json()

        if compte_id:
            content = (
                data.get("titre"),
                data.get("description"),
                data.get("type"),
                data.get("content_id"),
                compte_id
            )

            if request.files:
                fichier = request.files['file']

                compte_folder = os.path.join(
                    app.config['UPLOAD_FOLDER'], str(compte_id)
                )
                Path(compte_folder).mkdir(parents=True, exist_ok=True)

                filename = str(time.time()) + '_' + secure_filename(
                    fichier.filename)
                fichier.save(compte_folder, filename)

            try:
                CURSOR.execute("""
                    UPDATE
                        Content
                    SET
                        titre = %s,
                        description = %s,
                        type = %s
                """ + (filename or '') + """
                    WHERE
                        id=%s AND compte_id=%s;
                """, content)

                DB.commit()

                return {
                    "error": False,
                    "message": "Account Updated!"
                }, 200
            except Exception as err:
                print(err)
                DB.close()
                return {
                    "error": True,
                    "message": "le Contenu est encore utilisé !"
                }, 400

        return {
            "error": True,
            "message": "Pas d'access"
        }, 403

    except Exception as err:
        print(err)
        abort(500, description="Something went wrong !")


@verif_db
@app.route("/api/v1/update_fiche_metier/", methods=['PATCH'])
@jwt_required()
def update_fiche_metier():
    """
        DESC : Fonction permettant de mettre à jour
        les infos sur un contenus
    """
    try:
        compte_id = get_jwt_identity().split("+")[0]
        data = request.get_json()

        if compte_id:
            content = (
                data.get("titre"),
                data.get("description"),
                data.get("type"),
                data.get("content_id"),
                compte_id
            )

            if request.files:
                fichier = request.files['file']

                compte_folder = os.path.join(
                    app.config['UPLOAD_FOLDER'], str(compte_id)
                )
                Path(compte_folder).mkdir(parents=True, exist_ok=True)

                filename = str(time.time()) + '_' + secure_filename(
                    fichier.filename)
                fichier.save(compte_folder, filename)

            try:
                CURSOR.execute("""
                    UPDATE
                        Content
                    SET
                        titre = %s,
                        description = %s,
                        type = %s
                """ + (filename or '') + """
                    WHERE
                        id=%s AND compte_id=%s;
                """, content)

                DB.commit()

                return {
                    "error": False,
                    "message": "Account Updated!"
                }, 200
            except Exception as err:
                print(err)
                DB.close()
                return {
                    "error": True,
                    "message": "le Compte est encore utilisé !"
                }, 400

        return {
            "error": True,
            "message": "Pas d'access"
        }, 403

    except Exception as err:
        print(err)
        abort(500, description="Something went wrong !")


if __name__ == "__main__":
    app.run(debug=True)
