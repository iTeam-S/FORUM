import {createContext, useEffect, useState} from 'react';
import CompteService from 'utils/service/CompteService';


export const ContenuContexte = createContext();

export const ContenuContexteProvider = (props) =>{
    const [contenu, setContenu] = useState([]);
    /*useEffect(() => {
        async function fetchContenu(){
            await CompteService.getAllContenu().then((response) => {
                setContenu(response.data);
            });
        }

        fetchContenu();
    }, [])*/
    const addContenu = (newContenu) => {
        setContenu([...contenu, newContenu]);
    }

    return(
        <ContenuContexte.Provider value={{contenu, setContenu, addContenu}}>
            {props.children}
        </ContenuContexte.Provider>
    )
}