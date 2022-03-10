import { RouteAxios } from "utils/urlAxios/UrlAxios";
import {LoginService} from "utils/service/LoginService";

class CompteService{
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
        return RouteAxios.get("list_fiche_metier", {
            headers: {
                    'Authorization': `Bearer ${LoginService.getCurrentCompte().token}`
            }
        }).then(response => {
            return response;
        })
    }

}

export default new CompteService();
