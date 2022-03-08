import {createContext, useEffect, useState} from 'react';
import CompteService from 'utils/service/CompteService';


export const ContenuContexte = createContext();

export const ContenuContexteProvider = (props) =>{
    const [contenu, setContenu] = useState([]);
    const addContenu = (newContenu) => {
        setContenu([...contenu, newContenu]);
    }

    {/*useEffect(() => {
        async function fetchContenu(){
            const response = await CompteService.getAllCompte();
            setContenu(response.data);
        }

        fetchContenu();
    }, [])*/}

    return(
        <ContenuContexte.Provider value={{contenu, setContenu, addContenu}}>
            {props.children}
        </ContenuContexte.Provider>
    )
}