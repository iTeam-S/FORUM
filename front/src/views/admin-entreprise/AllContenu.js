import React, {useState, useContext} from "react";
import CardAllContenu from "components/Cards/CardAllContenu";
import { LoginService } from "utils/service/LoginService";
import { CompteContext } from "utils/contexte/CompteContext";


export default function AllContenu() {
   const {contenus} = useContext(CompteContext);
   const [type, setType] = useState("");
   const allContenus = LoginService.convertItemToArray(contenus);
  const contenuParDomaine = LoginService.getContenuPerDomaine(allContenus, type);

  const choixType = (e) => {
    let choix = e.target.value;
    return setType(choix);
  }
  return (
    <>
      <div className="flex flex-col flex-wrap bg-blueGray-400 w-full relative mt-20">
        <div className="flex justify-center flex-wrap">
            <h2 className="text-3xl font-bold text-center w-full mt-8 text-blueGray-800">Tous les contenus </h2>
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
            <CardAllContenu allContenu={contenuParDomaine} />
        </div>
      </div>
    </>
  );
}
