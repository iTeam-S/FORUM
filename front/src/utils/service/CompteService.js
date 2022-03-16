import { RouteAxios } from "utils/urlAxios/UrlAxios";
import {LoginService} from "utils/service/LoginService";

class CompteService{
                /*ADD SERVICE*/
    AddAccount(nom, email, tel, domaine, lien, type, password, adresse){
        return RouteAxios.post('/add_account', {
            nom, 
            email, 
            tel, 
            domaine, 
            lien, 
            type, 
            password, 
            adresse
        }, {
            headers: {
                'Authorization': `Bearer ${LoginService.getCurrentCompte().token}`,
                'Content-Type': 'application/json'
            }
        }
        )
    }
    AddContenu(titre, description, type, file){
        var content = new FormData();

        content.append("titre", titre);
        content.append("description", description);
        content.append("type", type);
        content.append("file", file);

        return RouteAxios.post('/add_content', content,{
            headers: {
                'Authorization': `Bearer ${LoginService.getCurrentCompte().token}`
            }
        })
    }
    AddFicheMetier(titre, domaine_id, file){
        var content = new FormData();

        content.append("titre", titre);
        content.append("domaine_id", domaine_id);
        content.append("file", file);

        return RouteAxios.post('/add_fiche_metier', content,{
            headers: {
                'Authorization': `Bearer ${LoginService.getCurrentCompte().token}`
            }
        })
    }

                /*GET SERVICE*/
    getAllCompte(){
        return RouteAxios.get("/list_accounts",  {
                headers: {
                    'Authorization': `Bearer ${LoginService.getCurrentCompte().token}`
                }
        }).then(response =>{
            return response;
        })
    }

    getAllContenu(){
        return RouteAxios.get("/list_contents",  {
                headers: {
                    'Authorization': `Bearer ${LoginService.getCurrentCompte().token}`
                }
        }).then(response =>{
            return response;
        })
    }

    getAllFiche(){
        return RouteAxios.get("/list_fiche_metier", {
            headers: {
                    'Authorization': `Bearer ${LoginService.getCurrentCompte().token}`
            }
        }).then(response => {
            return response;
        })
    }


                /*DELETE SERVICE*/
    DeleteOneCompte(compte_id){
        return RouteAxios.delete("/delete_account", 
            {
            headers: {
                'Authorization': `Bearer ${LoginService.getCurrentCompte().token}`
            },
            data: {
                compte_id: compte_id
            }
        },
        ) 
    }

    DeleteOneContent(content_id){
        return RouteAxios.delete("/delete_content", 
            {
            headers: {
                'Authorization': `Bearer ${LoginService.getCurrentCompte().token}`
            },
            data: {
                content_id: content_id
            }
        }
        ) 
    }

    DeleteFicheMetier(fiche_metier_id){
        return RouteAxios.delete("/delete_fiche_metier", 
            {
            headers: {
                'Authorization': `Bearer ${LoginService.getCurrentCompte().token}`
            },
            data: {
                fiche_metier_id: fiche_metier_id
            }
        }
        ) 
    }

    UpdateCompte(nom, email, tel, domaine, lien, type, password, adresse, description){
        return RouteAxios.patch('/update_account', {
            nom, 
            email, 
            tel, 
            domaine, 
            lien, 
            type, 
            password, 
            adresse,
            description
        }, {
            headers: {
                'Authorization': `Bearer ${LoginService.getCurrentCompte().token}`,
                'Content-Type': 'application/json'
            }
        }
        )
    }
        
}

export default new CompteService();
