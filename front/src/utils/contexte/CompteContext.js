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
            let reponseFiche = LoginService.convertItemToArray(response.data)
            setFiche(reponseFiche);
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
                let reponseCompte = LoginService.convertItemToArray(response.data)
                setCompte(reponseCompte);
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
   
    const addFiche = (newFiche)=> {
        setFiche([...fiche,newFiche]);
    }
    const addCompte = (newCompte)=> {
        setCompte([...compte,newCompte]);
    }

    return(
        <CompteContext.Provider 
            value= {{ compte, setCompte, addCompte,
                      contenus, 
                      fiche, setFiche, addFiche,
                      stat 
        }}>
            {props.children}
        </CompteContext.Provider>
    )
}