import React, {useContext} from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

import { CompteContext } from "utils/contexte/CompteContext";
import CompteService from "utils/service/CompteService";

export default function CardTable({ color}) {
  const {compte} = useContext(CompteContext);

  async function deleteOneCompte(id){
    await CompteService.DeleteOneCompte(id);
      window.location.reload();
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
                    Object.keys(compte).map((cle) => (
                          <tr key={compte[cle].id}>
                              <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center">
                                  <img
                                      src={compte[cle].logo ? compte[cle].logo : require("assets/img/logodefaut.png").default}
                                      className="h-12 w-12 bg-white rounded-full border"
                                      alt="..."
                                  ></img>{" "}
                                  <span
                                      className={
                                          "ml-3 font-bold " +
                                          +(color === "light" ? "text-blueGray-600" : "text-white")
                                        }
                                  >
                                        {compte[cle].nom}
                                  </span>
                                </th>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                                  <div className="flex justify-center">
                                    <span className="mr-2">{compte[cle].visiteurs}</span>
                                  </div>
                                </td>
                                <td className="border-t-0 px-3 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap text-left">
                                  <Link to={`/admin/profilDe/${compte[cle].id}`}>
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
                                      onClick={() => deleteOneCompte(compte[cle].id)}
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
