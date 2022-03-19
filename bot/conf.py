from os import environ as env
from dotenv import load_dotenv

# charger le fichier .env si present
load_dotenv()

# Token de verification serveur par Facebook
VERIFY_TOKEN = 'ametapplication'

# Authentification BDD
DATABASE = {
    'host': env.get("FORUM_DB_HOST"),
    'user': env.get("FORUM_DB_USER"),
    'password': env.get("FORUM_DB_PASS"),
    'database': env.get("FORUM_DB_NAME")
}

# ACCESS_TOKEN d'identification de la page
ACCESS_TOKEN = env.get("FORUM_ACCES_TOKEN")
URL_SERVER = env.get('URL_SERVER')
