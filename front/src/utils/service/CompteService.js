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
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${LoginService.getCurrentCompte().token}`
            }
        }
        )
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

    AddContenu(titre, description, type, file){
        return RouteAxios.post('/add_content', {
            titre,
            description,
            type,
            file
        },{
            headers: {
                'Authorization': `Bearer ${LoginService.getCurrentCompte().token}`,
                'Content-Type': "multipart/form-data",

            }
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

}

export default new CompteService();