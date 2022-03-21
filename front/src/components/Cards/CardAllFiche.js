import React, {useContext, useState } from "react";
import { useHistory } from "react-router";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

import { CompteContext } from "utils/contexte/CompteContext";
import CompteService from "utils/service/CompteService";
import { LoginService } from "utils/service/LoginService";

//styles css
import '../../assets/styles/cardStyle.css';

function DomaineName({domaine_id}){
    let nomDomaine = "";
    const domaineId = parseInt(domaine_id);
    switch (domaineId) {
      case 1 :
        nomDomaine = "Santé";
        break;
      case 2 :
        nomDomaine = "Informatique";
        break;
      case 3 :
        nomDomaine = "Commerce et Admnistration";
        break;
      case 4 :
        nomDomaine = "Agronomie";
        break;
      case 5 :
        nomDomaine = "Science Humaine et Communication";
        break;
      case 6 :
        nomDomaine = "Tourisme";
        break;
      case 7 :
        nomDomaine = "Industrie et BT";
        break;
      case 8 :
        nomDomaine = "Justice et Force de l'ordre";
        break;
      default :
        nomDomaine = "Vide";
        break;
    }
    return (
      <p className="border-t-0 align-top  border-l-0 border-r-0 text-xs whitespace-nowrap ">{nomDomaine}</p>
    )
  }

export default function CardAllFiche({color}) {
  const {fiche} = useContext(CompteContext); //fiche still array
  console.log(fiche)
  const [domaine, setDomaine] = useState(0);
  const ficheParDomaine = LoginService.getFichePerDomaine(fiche, domaine);
  const [termSearch, setTermSearch] = useState("");

  const choixDomaine = (e) => {
    let domCheck = parseInt(e.target.value);
     return setDomaine(domCheck);
  }

  const history = useHistory();

  async function deleteFiche(id_fiche){
    await CompteService.DeleteFicheMetier(id_fiche);
      history.push("/admin/AllFicheMetier");
      window.location.reload();
  }
  
  const recherche = (e) => {
    let valeur = e.target.value;
    setTermSearch(valeur);
}

  return (
    <>
        <div
            className={
            "relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded " +
            (color === "light" ? "bg-white" : "bg-lightBlue-900 text-white")
            }
        >
        <div className="rounded-t mb-0 px-4 py-3 border-0">
          <div className="flex flex-wrap items-center">
            <div className="relative w-full px-4 max-w-full flex-grow flex-1">
              <h3
                className={
                  "font-semibold text-lg " +
                  (color === "light" ? "text-blueGray-700" : "text-white")
                }
              >
                Listes des fiches métiers
              </h3>
            </div>
            <div className="w-full lg:w-4/12 px-4 mx-4 sm:mb-3">
                  <div className="relative w-full">
                    <input
                      type="text"
                      name="searchBar"
                      id="searchBar"
                      className="bg-lightBlue-900 border-0 px-3 py-3 placeholder-blueGray-300 text-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      placeholder="Entrer le titre à recherché..."
                      onChange={(e) => recherche(e)}
                   />
                </div>
            </div>
            <select
                name="type"
                className="bg-lightBlue-900 border-0 px-3 py-3 placeholder-blueGray-300 text-white bg-white rounded text-sm shadow focus:outline-none focus:ring w-3/12 ease-linear transition-all duration-150"
                onChange={(e) => choixDomaine(e)}
            >
                  <option  hidden>Trier par domaine</option>
                  <option key="1" value="1">Santé</option>
                  <option key="2" value="2">Informatique</option>
                  <option key="3" value="3">Commerce et Admnistration</option>
                  <option key="4" value="4">Agronomie</option>
                  <option key="5" value="5">Science Humaine et Communication</option>
                  <option key="6" value="6">Tourisme</option>
                  <option key="7" value="7">Industrie et BT</option>
                  <option key="8" value="8">Justice et Force de l'ordre</option>
            </select>
          </div>
        </div>
        <div className="block w-full overflow-x-auto">
          {/* Stand, entreprise table */}
          <table className="items-center w-full bg-transparent border-collapse">
            <thead>
              <tr>
                <th
                  className={
                    "px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left " +
                    (color === "light"
                      ? "bg-blueGray-50 text-blueGray-500 border-blueGray-100"
                      : "bg-lightBlue-800 text-lightBlue-300 border-lightBlue-700")
                  }
                >
                  Titre
                </th>
                <th
                  className={
                    "px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left " +
                    (color === "light"
                      ? "bg-blueGray-50 text-blueGray-500 border-blueGray-100"
                      : "bg-lightBlue-800 text-lightBlue-300 border-lightBlue-700")
                  }
                >
                  Domaine
                </th>
                <th
                  className={
                    "px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center " +
                    (color === "light"
                      ? "bg-blueGray-50 text-blueGray-500 border-blueGray-100"
                      : "bg-lightBlue-800 text-lightBlue-300 border-lightBlue-700")
                  }
                >
                  Statistique de visite
                </th>
                <th
                  className={
                    "px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left " +
                    (color === "light"
                      ? "bg-blueGray-50 text-blueGray-500 border-blueGray-100"
                      : "bg-lightBlue-800 text-lightBlue-300 border-lightBlue-700")
                  }
                ></th>
              </tr>
            </thead>
            <tbody>
                 { ficheParDomaine.filter((fiche) => {
                      return fiche.titre.toLowerCase().includes(termSearch.toLocaleLowerCase());
                    }).map((fiche) => (
                    <tr key={fiche.id}>
                      <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center">
                        <img
                          src={require("assets/img/fiche.jpeg").default}
                          className="h-12 w-12 bg-white rounded-full border"
                          alt="..."
                        ></img>{" "}
                        <span
                          className={
                            "ml-3 font-bold " +
                            +(color === "light" ? "text-blueGray-600" : "text-white")
                          }
                        >
                          {fiche.titre}
                        </span>
                      </th>
                      <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                        <div className="flex">
                          <span className="mr-2">
                              <DomaineName domaine_id={fiche.domaine_id} />
                          </span>
                        </div>
                      </td>
                      <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                        <div className="flex justify-center">
                          <span className="mr-2">100</span>
                        </div>
                      </td>
                      <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left">
                        <Link to={`/admin/CardEditFiche/${fiche.id}`}>
                          <button
                          className="bg-teal-500  text-white active:bg-lightBlue-800  font-bold  text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                            type="button"
                          >
                            Edit
                          </button>
                        </Link>
                        <button
                          className="bg-red-500  text-white active:bg-red-500 font-bold  text-xs px-2 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                          type="button"
                          onClick={() => deleteFiche(fiche.id)}
                        >
                          Delete
                        </button>
                      </td>
                    </tr>
                 ))
                 }
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}

CardAllFiche.defaultProps = {
  color: "light",
};

CardAllFiche.propTypes = {
  color: PropTypes.oneOf(["light", "dark"]),
};
