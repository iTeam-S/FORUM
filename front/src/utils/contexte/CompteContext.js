import {createContext, useEffect, useState} from 'react';
import CompteService from 'utils/service/CompteService';
import { LoginService } from 'utils/service/LoginService';


export const CompteContext = createContext();

export const CompteContextProvider = (props) =>{
    const [contenus, setContenu] = useState([]);
    const [stat, setStat] = useState([]);
    const [compte, setCompte] = useState([]);
    const [fiche, setFiche] = useState([]);

    async function fetchFicheMetier(){
        await CompteService.getAllFiche().then((response) => {
            setFiche(response.data);
        });
    }

    async function fetchStat(){
            await CompteService.getStatGallerie().then((response) => {
                 setStat(response.data);
                 if(LoginService.getCurrentCompte().type === 'ADMIN'){
                    fetchFicheMetier();
                }
            })
        }
    
    async function fetchCompte(){
            await CompteService.getAllCompte().then((response) => {
                setCompte(response.data);
                fetchStat();
            });
    }
    

    useEffect(() => {
        if(LoginService.getCurrentCompte() != null){
             async function fetchContenu(){
                 await CompteService.getAllContenu().then((response) => {
                    if(response.data['error'] === undefined){
                        setContenu(response.data);
                    } 
                    fetchCompte();
                })
            }
            fetchContenu();
        } else if(LoginService.getCurrentCompte() != null && LoginService.getCurrentCompte().type === 'ENTREPRISE'){
            async function fetchContenu(){
                await CompteService.getAllContenu().then((response) => {
                        if(response.data['error'] === undefined){
                        setContenu(response.data);
                    } 
                })
            }
            fetchContenu();
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])
   

    return(
        <CompteContext.Provider value={{ compte, contenus, fiche, stat }}>
            {props.children}
        </CompteContext.Provider>
    )
}