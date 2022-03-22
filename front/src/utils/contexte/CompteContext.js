import {createContext, useEffect, useState} from 'react';
import CompteService from 'utils/service/CompteService';
import { LoginService } from 'utils/service/LoginService';


export const CompteContext = createContext();

export const CompteContextProvider = (props) =>{
    const [contenus, setContenu] = useState([]);
    const [stat, setStat] = useState([]);
    const [compte, setCompte] = useState([]);
    const [fiche, setFiche] = useState([]);

    function fetchFicheMetier(){
        CompteService.getAllFiche()
        .then((response) => {
            let reponseFiche = LoginService.convertItemToArray(response.data)
            setFiche(reponseFiche);
        })
        .catch((error)=>console.log(error))
    }

     function fetchStat(){
        CompteService.getStatGallerie()
        .then((response) => {
                 setStat(response.data);
                 if(LoginService.getCurrentCompte().type === 'ADMIN'){
                    fetchFicheMetier();
                }
            })
        .catch((error)=>console.log(error))
        }
    
     function fetchCompte(){
             CompteService.getAllCompte()
             .then((response) => {
                let reponseCompte = LoginService.convertItemToArray(response.data)
                setCompte(reponseCompte);
                fetchStat();
            })
            .catch((error)=>console.log(error))
    }
    

    useEffect(() => {
        if(LoginService.getCurrentCompte() != null){
              function fetchContenu(){
                  CompteService.getAllContenu()
                  .then((response) => {
                        if(response.data['error'] === undefined){
                            let reponseContent = LoginService.convertItemToArray(response.data);
                            setContenu(reponseContent);
                        } 
                        fetchCompte();
                    })
                  .catch((error)=>console.log(error))
            }
            fetchContenu();
        } else if(LoginService.getCurrentCompte() != null && LoginService.getCurrentCompte().type === 'ENTREPRISE'){
             function fetchContenu(){
                CompteService.getAllContenu()
                .then((response) => {
                        if(response.data['error'] === undefined){
                        setContenu(response.data);
                    } 
                })
                .catch((error)=>console.log(error))
            }
            fetchContenu();
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])
   
    const addFiche = (newFiche)=> {
        setFiche([...fiche,newFiche]);
        window.location.reload();
    }
    const addCompte = (newCompte)=> {
        setCompte([...compte,newCompte]);
        window.location.reload();
    }
    const addContenu = (newContent)=> {
        setContenu([...contenus,newContent]);
        window.location.reload();
    }

    return(
        <CompteContext.Provider 
            value= {{ compte, setCompte, addCompte,
                      contenus, setContenu, addContenu,
                      fiche, setFiche, addFiche,
                      stat 
        }}>
            {props.children}
        </CompteContext.Provider>
    )
}