import {createContext, useEffect, useState} from 'react';
import CompteService from 'utils/service/CompteService';
import { LoginService } from 'utils/service/LoginService';


export const CompteContext = createContext();

export const CompteContextProvider = (props) =>{
    const [compte, setCompte] = useState([]);
    const ifLog = LoginService.getCurrentCompte();
    useEffect(() => {
        if(ifLog != null){
            async function fetchCompte(){
                await CompteService.getAllCompte().then((response) => {
                    setCompte(response.data);
                });
        }
        fetchCompte();
    }
    }, [])
    const addCompte = (newCompte) => {
        setCompte([...compte, newCompte]);
    }
    
    return(
        <CompteContext.Provider value={{addCompte, setCompte, compte}}>
            {props.children}
        </CompteContext.Provider>
    )
}