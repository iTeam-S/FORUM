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

## Insert ficher metier (Need ADMIN access)
```
  POST http://<host>:5000/api/v1/add_fiche_metier
  content-type: application/json
  Authorization: Bearer <Token>

  {
    "titre": <titre>,
    "domaine_id": <domaine_id>,
    "file": <file(img/pdf)>
  }
```
=> RETOUR:
```
  {
    "error": false,
    "message": "Fiche Metier inserted"
  }
```


## Get list company
```
  GET http://127.0.0.1:5000/api/v1/list_accounts
  Authorization: Bearer <Token>
```
=> RETOUR:
```
  {
    "0": {
        "nom": <stand_name>,
        "email": <email>,
        "tel": <phone_number>,
        "domaine": <stand_domaine>,
        "lien": <site_link>,
        "type": <account_type>,
        "adresse": "<addresse_of_company>"
      },
      "1": {
        "nom": <stand_name>,
        "email": <email>,
        "tel": <phone_number>,
        "domaine": <stand_domaine>,
        "lien": <site_link>,
        "type": <account_type>,
        "adresse": "<addresse_of_company>"
      },
      ....
  }
```

## Get list contents of a company

```
  GET http://127.0.0.1:5000/api/v1/list_contents
  Authorization: Bearer <Token>
```
=> RETOUR:
```
{
  "0": {
    "description": <description>,
    "fichier": <fichier> ,
    "titre": <titre> ,
    "type": <type>
  },
  "1": {
    "description": <description>,
    "fichier": <fichier> ,
    "titre": <titre> ,
    "type": <type> 
  },
    "2": {
    "description": <description>,
    "fichier": <fichier> ,
    "titre": <titre> ,
    "type": <type> 
  },
  ...
}
```

## Get list of Fiche Metier (Need Admin Access)

```
  GET http://127.0.0.1:5000/api/v1/list_fiche_metier
  Authorization: Bearer <Token>
```
=> RETOUR:
```
{
  "0": {
    "titre": <description>,
    "domaine_id": <fichier> ,
    "file": <titre>
  },
  "1": {
    "titre": <titre>,
    "domaine_id": <domaine_id> ,
    "file": <file>
  },
  ...
}
```

## Delete stand account (Need Admin Access)

```
  DELETE http://127.0.0.1:5000/api/v1/delete_account
  Authorization: Bearer <Token>
  content-type: application/json
    
  {
    "compte_id": <compte_id>
  }
```
=> RETOUR:
```
  {
    "error": False,
    "message": "Account Deleted!"
  }
}
```

## Delete content of an account

```
  DELETE http://127.0.0.1:5000/api/v1/delete_content
  Authorization: Bearer <Token>
  content-type: application/json
    
  {
    content_id": <content_id>
  }
```
=> RETOUR:
```
  {
    "error": False,
    "message": "Content Deleted!"
  }
```

## Delete Fiche metier ( Need admin access )

```
  DELETE http://127.0.0.1:5000/api/v1/delete_fiche_metier
  Authorization: Bearer <Token>
  content-type: application/json
    
  {
    "fiche_metier_id": <fiche_metier_id>
  }
```
=> RETOUR:
```
  {
    "error": False,
    "message": "Fiche Metier Deleted!"
  }
```