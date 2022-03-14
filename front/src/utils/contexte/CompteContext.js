import {createContext, useLayoutEffect, useState} from 'react';
import CompteService from 'utils/service/CompteService';
import { LoginService } from 'utils/service/LoginService';


export const CompteContext = createContext();

export const CompteContextProvider = (props) =>{
    const [contenus, setContenu] = useState([]);
    const [compte, setCompte] = useState([]);
    const [fiche, setFiche] = useState([]);

    async function fetchFicheMetier(){
        await CompteService.getAllFiche().then((response) => {
            setFiche(response.data);
        });
    }
    
    async function fetchCompte(){
            await CompteService.getAllCompte().then((response) => {
                setCompte(response.data);
                fetchFicheMetier();
            });
    }
    

    useLayoutEffect(() => {
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
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])
   

    return(
        <CompteContext.Provider value={{ compte, contenus, fiche }}>
            {props.children}
        </CompteContext.Provider>
    )
}