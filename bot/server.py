from flask import Flask, abort, request, send_from_directory
from threading import Thread
from conf import VERIFY_TOKEN
import core

# Instanciation du serveur web
webserver = Flask(__name__)

# Instanciation du principal execution
traitement = core.Traitement()


@webserver.route("/", methods=["GET", "POST"])
def receive_message():
    if request.method == "GET":
        '''
            Ce cas est destiné au verification de l'etat de
            vie du serveur web, utilise par Facebook pour
            justifier que ce serveur reçoit les messages envoyés.
        '''
        token_sent = request.args.get("hub.verify_token")
        if token_sent == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Invalid verification token"

    elif request.method == "POST":
        '''
            Les requetes envoyés en moode 'POST' sont les messages
            envoyé sur la page Facebook et qui sont à traiter.
        '''
        body = request.get_json()
        proc = Thread(target=traitement._analyse, args=[body])
        proc.start()

    return "receive", 200


@webserver.route("/<user_id>/<filename>")
def get_file_for_content(user_id, filename):
    try:
        return send_from_directory(
            './../back/data/' + user_id + '/',
            path=filename,
            as_attachment=True
        )
    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    webserver.run(port=2022)
