import React, {useContext} from "react";
import { useHistory } from "react-router";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

import { CompteContext } from "utils/contexte/CompteContext";
import CompteService from "utils/service/CompteService";

//styles css
import '../../assets/styles/cardStyle.css';


export default function CardAllFiche({color}) {
  const {fiche} = useContext(CompteContext); //fiche still obj
  const history = useHistory();

  const deleteFiche = (id_fiche) => {
    CompteService.DeleteFicheMetier(id_fiche);
    history.push("/adminEntreprise/Statistiques");
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
                Listes des fiches métiers
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
              </tr>
            </thead>
            <tbody>
                 { Object.keys(fiche).map((cle) => (
                    <tr key={fiche[cle].id}>
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
                          {fiche[cle].titre}
                        </span>
                      </th>
                      <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                        <div className="flex justify-center">
                          <span className="mr-2">
                            {fiche[cle].domaine}
                          </span>
                        </div>
                      </td>
                      <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                        <div className="flex justify-center">
                          <span className="mr-2">100</span>
                        </div>
                      </td>
                      <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left">
                        <Link to="/admin/CardEditFiche">
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
                          onClick={() => deleteFiche(fiche[cle].id)}
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
