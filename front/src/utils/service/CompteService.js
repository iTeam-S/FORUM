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
        var content = new FormData();

        content.append("titre", titre);
        content.append("description", description);
        content.append("type", type);
        content.append("file", file);

        return RouteAxios.post('/add_content', content,{
            headers: {
                'Authorization': `Bearer ${LoginService.getCurrentCompte().token}`,
                'Content-Type': 'multipart/form-data; boundary=${form._boundary}'
            }
        })
    }

    getAllContenu(){
        return RouteAxios.get("/list_contents",  {
                headers: {
                    'Authorization': `Bearer ${LoginService.getCurrentCompte().token}`
                }
        }).then(response =>{
            console.log(response.data);
            return response.data;
        })
    }

}

export default new CompteService();
