import {createContext, useEffect, useState} from 'react';
import CompteService from 'utils/service/CompteService';
import { LoginService } from 'utils/service/LoginService';


export const CompteContext = createContext();

export const CompteContextProvider = (props) =>{
    let [contenus, setContenu] = useState([]);
    const [compte, setCompte] = useState([]);

    async function fetchCompte(){
               await CompteService.getAllCompte().then((response) => {
                setCompte(response.data);
            });
    }

    useEffect(() => {
        if(LoginService.getCurrentCompte() != null && LoginService.getCurrentCompte().type === 'ADMIN'){
             async function fetchContenu(){
                await CompteService.getAllContenu().then((response) => {
                    setContenu(response.data);
                    fetchCompte();
                })
            }
            fetchContenu();
        } else if(LoginService.getCurrentCompte() != null && LoginService.getCurrentCompte().type === 'ENTREPRISE'){
            async function fetchContenu(){
                await CompteService.getAllContenu().then((response) => {
                    setContenu(response.data);
                })
            }
            fetchContenu();
        }
    }, [])
   

    return(
        <CompteContext.Provider value={{ setCompte, setContenu,  compte, contenus }}>
            {props.children}
        </CompteContext.Provider>
    )
}