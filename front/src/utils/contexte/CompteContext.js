import {createContext, useEffect, useState} from 'react';
import CompteService from 'utils/service/CompteService';


export const CompteContext = createContext();

export const CompteContextProvider = (props) =>{
    const [compte, setCompte] = useState([]);
    const addCompte = (newCompte) => {
        setCompte([...compte, newCompte]);
    }

    {/*useEffect(() => {
        async function fetchCompte(){
            const response = await CompteService.getAllCompte();
            setCompte(response.data);
        }

        fetchCompte();
    }, [])*/}

    return(
        <CompteContext.Provider value={{compte, setCompte, addCompte}}>
            {props.children}
        </CompteContext.Provider>
    )
}