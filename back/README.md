## Deployement 
Dev : python main.py
Prod : gunicorn wsgi:app

## Login request
```
POST http://<host>:5000/api/v1/login
content-type: application/json

{
    "email": "<account_email>",
    "password": "<account_pass>"
}
```
=> RETOUR:
```
{
  "description": <description>,
  "id": <id>,
  "lien": <lien_vers_site>,
  "logo": <logo_entreprise>,
  "nom": <nom_entreprise>,
  "tel": <tel>,
  "token": <token_expire_12h>,
  "type": <role_compte>,
  "video": <video_presentation>,
  "vu": <nombre_visiteur>
}
```

## Add company(stand) account request
```
  POST http://<host>:5000/api/v1/add_account
  content-type: application/json
  Authorization: Bearer <Token>

  {
    "nom": <stand_name>,
    "email": <email>,
    "tel": <phone_number>,
    "domaine": <stand_domaine>,
    "lien": <site_link>,
    "type": <account_type>,
    "password": <account_password>,
    "adresse": "<addresse_of_company>"
  }
```
=> RETOUR:
```
  {
    "error": false,
    "message": "Account created"
  }
```