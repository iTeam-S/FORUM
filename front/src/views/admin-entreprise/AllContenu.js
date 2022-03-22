import React, {useState, useContext} from "react";
import CardAllContenu from "components/Cards/CardAllContenu";
import { LoginService } from "utils/service/LoginService";
import { CompteContext } from "utils/contexte/CompteContext";


export default function AllContenu() {
  const {contenus} = useContext(CompteContext);
  const [type, setType] = useState("");
  const contenuParDomaine = LoginService.getContenuPerDomaine(contenus, type);

  const [termSearch, setTermSearch] = useState("");

  const choixType = (e) => {
    let choix = e.target.value;
    return setType(choix);
  }

  const recherche = (e) => {
  let valeur = e.target.value;
  setTermSearch(valeur);
}

  return (
    <>
      <div className="flex flex-col flex-wrap bg-blueGray-400 w-full relative mt-20">
        <div className="flex justify-center flex-wrap">
            <h2 className="text-3xl font-bold text-center w-full mt-8 text-blueGray-800">Tous les contenus </h2>
            <div className="w-full lg:w-6/12 px-4 mx-4 sm:mb-3">
                  <div className="relative w-full">
                    <input
                      type="text"
                      name="searchBar"
                      id="searchBar"
                      className="border-1 px-3 py-3 placeholder-blueGray-500 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      placeholder="Entrer la clé de la recherche..."
                      onChange={(e) => recherche(e)}
                   />
                </div>
              </div>
            <select
                name="type"
                className="border-1 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-4/12 ease-linear transition-all duration-150"
                onChange={(e) => choixType(e)}
            >
                  <option  hidden>Trier par domaine</option>
                  <option key="1" value="galerie">Galerie</option>
                  <option key="2" value="emploi">Offre d'emploi</option>
                  <option key="3" value="information">Informations</option>
             </select>
        </div>
        <div className="flex flex-wrap">
            <CardAllContenu contenu={contenus} allContenu={contenuParDomaine} termSearch={termSearch}/>
        </div>
      </div>
    </>
  );
}
