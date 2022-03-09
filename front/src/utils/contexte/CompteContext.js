import {createContext, useEffect, useState} from 'react';
import CompteService from 'utils/service/CompteService';
import { LoginService } from 'utils/service/LoginService';


export const CompteContext = createContext();

export const CompteContextProvider = (props) =>{
    let [contenu, setContenu] = useState([]);
    const [compte, setCompte] = useState([]);

    function fetchContenu(){
            CompteService.getAllContenu().then((response) => {
            setContenu(response);
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
    const addCompte = (newCompte) => {
        setCompte([...compte, newCompte]);
    }
    const addContenu = (newContenu) => {
        setContenu([...contenu, newContenu]);
    }

    return(
        <CompteContext.Provider value={{addCompte, setCompte, compte, contenu , addContenu, setContenu}}>
            {props.children}
        </CompteContext.Provider>
    )
}