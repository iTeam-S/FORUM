import {createContext, useEffect, useState} from 'react';
import CompteService from 'utils/service/CompteService';
import { LoginService } from 'utils/service/LoginService';


export const CompteContext = createContext();

export const CompteContextProvider = (props) =>{
    let [contenus, setContenu] = useState([]);
    const [compte, setCompte] = useState([]);

    async function fetchContenu(){
           await CompteService.getAllContenu().then((response) => {
            setContenu(response.data);
        });
    }

    useEffect(() => {
        if(LoginService.getCurrentCompte() != null){
            async function fetchCompte(){
                await CompteService.getAllCompte().then((response) => {
                setCompte(response.data);
                fetchContenu();
                })
            }
            fetchCompte();
    }
    }, [])
   

    return(
        <CompteContext.Provider value={{ setCompte, setContenu,  compte, contenus }}>
            {props.children}
        </CompteContext.Provider>
    )
}