import React, {useContext, useState} from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

import { CompteContext } from "utils/contexte/CompteContext";
import CompteService from "utils/service/CompteService";
import { LoginService } from "utils/service/LoginService";

export default function CardTable({ color}) {
  const {compte} = useContext(CompteContext);
  const [domaine, setDomaine] = useState("");
  const allCompte = LoginService.convertItemToArray(compte);
  const compteParDomaine = LoginService.getComptePerDomaine(allCompte, domaine);

  async function deleteOneCompte(id){
    await CompteService.DeleteOneCompte(id);
      window.location.reload();
  }
  const choixDomaine = (e) => {
    let domCheck = e.target.value;
    setDomaine(domCheck);
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
                Listes des entreprises
              </h3>
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
                    compteParDomaine.map((account) => (
                          <tr key={account.id}>
                              <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center">
                                  <img
                                      src={account.logo ? account.logo : require("assets/img/logodefaut.png").default}
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
                                            className="bg-emerald-500  text-white active:bg-lightBlue-800 font-bold  text-xs px-2 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                                            type="button"
                                        >
                                          Voir profil
                                        </button>
                                  </Link>
                                  <button
                                      className="bg-lightBlue-800  text-white active:bg-teal-500 font-bold  text-xs px-2 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                                      type="button"
                                      onClick={() => deleteOneCompte(account.id)}
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

CardTable.defaultProps = {
  color: "light",
};

CardTable.propTypes = {
  color: PropTypes.oneOf(["light", "dark"]),
};
