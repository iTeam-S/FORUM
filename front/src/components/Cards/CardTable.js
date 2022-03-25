import React, {useContext, useState} from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

import { CompteContext } from "utils/contexte/CompteContext";
import CompteService from "utils/service/CompteService";
import { LoginService } from "utils/service/LoginService";
import {uRI} from "utils/urlAxios/UrlAxios";

//style css
import '../../assets/styles/cardStyle.css';

export default function CardTable({ color}) {
  const {compte, setCompte} = useContext(CompteContext);
  const [domaine, setDomaine] = useState("");
  const idCompteCurrent = LoginService.getCurrentCompte().id;
  const compteParDomaine = LoginService.getComptePerDomaine(compte, domaine);

  const [termSearch, setTermSearch] = useState("");
  const [showAlert, setShowAlert] = useState(false);
  const [isActive, setIsActive] = useState("");

  function activate(nombre){
    if(nombre === "1"){
      setIsActive("0")
    }
  }

   function deleteOneCompte(id){
    CompteService.DeleteOneCompte(id);
    setCompte(compte.filter((cmpt) => {
      return cmpt.id !== id;
    }))
    setShowAlert(true)
  }
  
  if(showAlert){
    setTimeout(() => {
      setShowAlert(false)
    }, 5000);
  }
  const choixDomaine = (e) => {
    let domCheck = e.target.value;
    setDomaine(domCheck);
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
        {/**Popup alert */}
        {showAlert ? (
           <div
              className="text-white px-6 py-4 border-0 rounded relative mb-4 bg-red-500 popup"
            >
                <span className="text-xl inline-block mr-5 align-middle mr-2">
                  <i className="fas fa-bell" />
                </span>
                <span className="inline-block align-middle mr-8 ">
                  <b className="capitalize "> </b> Le compte a été supprimé
                </span>
                <button
                  className="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-4 outline-none focus:outline-none"
                  onClick={() => setShowAlert(false)}
                >
                  <span>×</span>
              </button>
            </div> 
      ) : null}
          {/**FIN POPUP */}


        <div className="rounded-t mb-0 px-4 py-3 border-0">
          <div className="flex flex-wrap items-center">
            <div className="relative w-full sm:text-center px-4 max-w-full flex-grow flex-1">
              <h3
                className={
                  "font-semibold text-lg " +
                  (color === "light" ? "text-blueGray-700" : "text-white")
                }
              >
                Listes des entreprises
              </h3>
            </div>
             <div className="w-full lg:w-4/12 px-4 mx-4 sm:mb-3">
                  <div className="relative w-full">
                    <input
                      type="text"
                      name="searchBar"
                      id="searchBar"
                      className="border-0 px-3 py-3 placeholder-blueGray-500 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      placeholder="Entrer la clé de la recherche..."
                      onChange={(e) => recherche(e)}
                   />
                </div>
              </div>
            <select
                name="type"
                className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-3/12 ease-linear transition-all duration-150"
                onChange={(e) => choixDomaine(e)}
            >
                  <option  hidden>Trier par domaine</option>
                  <option key="1" value="Santé">Santé</option>
                  <option key="2" value="Informatique">Informatique</option>
                  <option key="3" value="Commerce et Admnistration">Commerce et Admnistration</option>
                  <option key="4" value="Agronomie">Agronomie</option>
                  <option key="5" value="Science Humaine et Communication">Science Humaine et Communication</option>
                  <option key="6" value="Tourisme">Tourisme</option>
                  <option key="7" value="Industrie et BT">Industrie et BT</option>
                  <option key="8" value="Justice et Force de l'ordre">Justice et Force de l'ordre</option>
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
                  Nom de l'entreprise
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
                 {
                    compteParDomaine.filter((account) => {
                      return account.nom.toLowerCase().includes(termSearch.toLocaleLowerCase());
                    }).map((account) => (
                          <tr key={account.id}>
                              <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center">
                                  <img
                                      src={account.logo ? `${uRI}/get_attachement/${account.id}/${account.logo}`  : require("assets/img/logodefaut.png").default}
                                      className="h-12 w-12 bg-white rounded-full border"
                                      alt="..."
                                  ></img>{" "}
                                  <span
                                      className={
                                          "ml-3 font-bold " +
                                          +(color === "light" ? "text-blueGray-600" : "text-white")
                                        }
                                  >
                                        {account.nom}
                                  </span>
                                </th>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                                  <div className="flex justify-center">
                                    <span className="mr-2">{account.visiteurs}</span>
                                  </div>
                                </td>
                                <td className="border-t-0 px-3 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap text-left">
                                  <Link to={`/admin/profilDe/${account.id}`}>
                                        <button
                                            className="bg-lightBlue-500  text-white active:bg-lightBlue-800 font-bold  text-xs px-2 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                                            type="button"
                                        >
                                          Voir profil
                                        </button>
                                  </Link>
                                  {account.id !== idCompteCurrent && (
                                    <button
                                        className="bg-lightBlue-800  text-white active:bg-teal-500 font-bold  text-xs px-2 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                                        type="button"
                                        onClick={() => deleteOneCompte(account.id)}
                                    >
                                      Delete
                                    </button>
                                  )}
                                  {account.id !== idCompteCurrent && (
                                      account.actif === "1" ? (
                                          <button
                                                className="bg-teal-500  text-white active:bg-lightBlue-800 font-bold  text-xs px-2 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                                                type="button"
                                                onClick={() => activate(account.actif)}
                                          >
                                            Activé
                                          </button>
                                      ) : (
                                        <button
                                            className="bg-red-500  text-white active:bg-lightBlue-800 font-bold  text-xs px-2 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                                            type="button"
                                            onClick={() => activate(account.actif)}
                                        >
                                            Desactivé
                                        </button>
                                      )
                                  )}
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

CardTable.defaultProps = {
  color: "light",
};

CardTable.propTypes = {
  color: PropTypes.oneOf(["light", "dark"]),
};
