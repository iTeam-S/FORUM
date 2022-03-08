import {createContext, useEffect, useState} from 'react';
import CompteService from 'utils/service/CompteService';


export const CompteContext = createContext();

export const CompteContextProvider = (props) =>{
    const [compte, setCompte] = useState([]);
    useEffect(() => {
        async function fetchCompte(){
                await CompteService.getAllCompte().then((response) => {
                    setCompte(response.data);
                });
               
        }

        fetchCompte();
    }, [])
    const addCompte = (newCompte) => {
        setCompte([...compte, newCompte]);
    }
    
    return(
        <CompteContext.Provider value={{compte, setCompte, addCompte}}>
            {props.children}
        </CompteContext.Provider>
    )
}