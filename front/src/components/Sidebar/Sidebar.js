/*eslint-disable*/
import React from "react";
import { Link } from "react-router-dom";

import UserDropdown from "components/Dropdowns/UserDropdown.js";
import { LoginService } from "utils/service/LoginService";

export default function Sidebar() {
  const [collapseShow, setCollapseShow] = React.useState("hidden");
  const compte = LoginService.getCurrentCompte().type;


  return (
    <>
      <nav className="md:left-0 md:block md:fixed md:top-0 md:bottom-0 md:overflow-y-auto md:flex-row md:flex-nowrap md:overflow-hidden shadow-xl bg-white flex flex-wrap items-center justify-between relative md:w-64 z-10 py-4 px-6">
        <div className="md:flex-col md:items-stretch md:min-h-full md:flex-nowrap px-0 flex flex-wrap items-center justify-between w-full mx-auto">
          {/* Toggler */}
          <button
            className="cursor-pointer text-black opacity-50 md:hidden px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent"
            type="button"
            onClick={() => setCollapseShow("bg-white m-2 py-3 px-6")}
          >
            <i className="fas fa-bars"></i>
          </button>
          {/* Brand */}
          <div className="w-6/12 ">Sésame</div>
          {/* User */}
          <ul className="md:hidden items-center flex flex-wrap list-none">
            <li className="inline-block relative">
              <UserDropdown />
            </li>
          </ul>
          {/* Collapse */}
          <div
            className={
              "md:flex md:flex-col md:items-stretch md:opacity-100 md:relative md:mt-4 md:shadow-none shadow absolute top-0 left-0 right-0 z-40 overflow-y-auto overflow-x-hidden h-auto items-center flex-1 rounded " +
              collapseShow
            }
          >
            {/* Collapse header */}
            <div className="md:min-w-full md:hidden block pb-4 mb-4 border-b border-solid border-blueGray-200">
              <div className="flex flex-wrap">
                <div className="w-6/12">
                  Sesame
                </div>
              </div>
            </div>

           

            {/* ADMIN */}
            { compte === 'ADMIN' && (
              <div id="admin">
                <hr className="my-4 md:min-w-full" />
                <h6 className="md:min-w-full text-blueGray-500 text-xs uppercase font-bold block pt-1 pb-4 no-underline">
                Admin 
                </h6>
                {/* Navigation */}

                <ul className="md:flex-col md:min-w-full flex flex-col list-none">
                  <li className="items-center">
                    <Link
                      className={
                        "text-xs uppercase py-3 font-bold block " +
                        (window.location.href.indexOf("/admin/TablesEntreprises") !== -1
                          ? "text-teal-500 hover:text-teal-600"
                          : "text-blueGray-700 hover:text-blueGray-500")
                      }
                      to="/admin/TablesEntreprises"
                    >
                      <i
                        className={
                          "fas fa-building mr-2 text-sm " +
                          (window.location.href.indexOf("/admin/TablesEntreprises") !== -1
                            ? "opacity-75"
                            : "text-blueGray-300")
                        }
                      ></i>{" "}
                      Liste entreprise
                    </Link>
                  </li>
                  <li className="items-center">
                    <Link
                      className={
                        "text-xs uppercase py-3 font-bold block " +
                        (window.location.href.indexOf("/admin/AllFicheMetier") !== -1
                          ? "text-teal-500 hover:text-teal-600"
                          : "text-blueGray-700 hover:text-blueGray-500")
                      }
                      to="/admin/AllFicheMetier"
                    >
                      <i
                        className={
                          "fas fa-file mr-2 text-sm " +
                          (window.location.href.indexOf("/admin/AllFicheMetier") !== -1
                            ? "opacity-75"
                            : "text-blueGray-300")
                        }
                      ></i>{" "}
                      Liste fiche métier
                    </Link>
                  </li>

                  <li className="items-center">
                    <Link
                      className={
                        "text-xs uppercase py-3 font-bold block " +
                        (window.location.href.indexOf("/admin/AddEntreprise") !== -1
                          ? "text-teal-500 hover:text-teal-600"
                          : "text-blueGray-700 hover:text-blueGray-500")
                      }
                      to="/admin/AddEntreprise"
                    >
                      <i
                        className={
                          "fas fa-tools mr-2 text-sm " +
                          (window.location.href.indexOf("/admin/AddEntreprise") !== -1
                            ? "opacity-75"
                            : "text-blueGray-300")
                        }
                      ></i>{" "}
                      Ajouter entreprise
                    </Link>
                  </li>

                  <li className="items-center">
                    <Link
                      className={
                        "text-xs uppercase py-3 font-bold block " +
                        (window.location.href.indexOf("/admin/AddFicheMetier") !== -1
                          ? "text-teal-500 hover:text-teal-600"
                          : "text-blueGray-700 hover:text-blueGray-500")
                      }
                      to="/admin/AddFicheMetier"
                    >
                      <i
                        className={
                          "fas fa-plus mr-2 text-sm " +
                          (window.location.href.indexOf("/admin/AddFicheMetier") !== -1
                            ? "opacity-75"
                            : "text-blueGray-300")
                        }
                      ></i>{" "}
                      Ajouter fiche métier
                    </Link>
                  </li>
                </ul>
              </div>
            )}

            {/* Divider */}
            <hr className="my-4 md:min-w-full" />
            {/* ENTREPRISE */}
              <h6 className="md:min-w-full text-blueGray-500 text-xs uppercase font-bold block pt-1 pb-4 no-underline">
              Entreprise
              </h6>
              {/* Navigation */}

              <ul className="md:flex-col md:min-w-full flex flex-col list-none md:mb-4">
                <li className="items-center">
                  <Link
                    className={
                      "text-xs uppercase py-3 font-bold block " +
                      (window.location.href.indexOf("/adminEntreprise/ProfilEntreprise") !== -1
                        ? "text-teal-500 hover:text-teal-600"
                        : "text-blueGray-700 hover:text-blueGray-500")
                    }
                    to="/adminEntreprise/ProfilEntreprise"
                  >
                    <i className={"fas fa-user-circle mr-2 text-sm" + 
                              (window.location.href.indexOf("/adminEntreprise/ProfilEntreprise") !== -1
                                ? "opacity-75"
                                : "text-blueGray-300")
                        }
                    ></i>{" "}
                    Profile entreprise
                  </Link>
                </li>
                      
                <li className="items-center">
                  <Link
                    className={
                      "text-xs uppercase py-3 font-bold block " +
                      (window.location.href.indexOf("/adminEntreprise/Statistiques") !== -1
                        ? "text-teal-500 hover:text-teal-600"
                        : "text-blueGray-700 hover:text-blueGray-500")
                    }
                    to="/adminEntreprise/Statistiques"
                  >
                    <i
                      className={
                        "fas fa-chart-bar mr-2 text-sm" + 
                          (window.location.href.indexOf("/adminEntreprise/Statistiques") !== -1
                                ? "opacity-75"
                                : "text-blueGray-300")
                      }
                    ></i>{" "}
                    Statistiques
                  </Link>
                </li>

                <li className="items-center">
                  <Link
                    className={
                      "text-xs uppercase py-3 font-bold block " +
                      (window.location.href.indexOf("/adminEntreprise/AllContenu") !== -1
                        ? "text-teal-500 hover:text-teal-600"
                        : "text-blueGray-700 hover:text-blueGray-500")
                    }
                    to="/adminEntreprise/AllContenu"
                  >
                    <i className={"fas fa-newspaper mr-2 text-sm" + 
                                (window.location.href.indexOf("/adminEntreprise/AllContenu") !== -1
                                ? "opacity-75"
                                : "text-blueGray-300")
                        }
                    ></i>{" "}
                    Liste contenus
                  </Link>
                </li>

                <li className="items-center">
                  <Link
                    className={
                      "text-xs uppercase py-3 font-bold block " +
                      (window.location.href.indexOf("/adminEntreprise/AddContenu") !== -1
                        ? "text-teal-500 hover:text-teal-600"
                        : "text-blueGray-700 hover:text-blueGray-500")
                    }
                    to="/adminEntreprise/AddContenu"
                  >
                    <i className={"fas fa-file mr-2 text-sm" + 
                                (window.location.href.indexOf("/adminEntreprise/AddContenu") !== -1
                                ? "opacity-75"
                                : "text-blueGray-300")
                        }
                    ></i>{" "}
                    Ajouter contenu
                  </Link>
                </li>
              </ul>

            {/* iTeam-$ about */}
            <hr className="my-4 md:min-w-full" />
            {/* Heading */}
            <h6 className="md:min-w-full text-blueGray-500 text-xs uppercase font-bold block pt-1 pb-4 no-underline">
              About Us
            </h6>
            {/* Navigation */}
            <ul className="md:flex-col md:min-w-full flex flex-col list-none md:mb-4">
              <li className="inline-flex">
                <a
                  href="https://iteam-s.mg/view/membre.html"
                  target="_blank"
                  className="text-blueGray-700 hover:text-blueGray-500 text-sm block mb-4 no-underline font-semibold"
                >
                  <i className="fas fa-paint-brush mr-2 text-blueGray-300 text-base"></i>
                  About
                </a>
              </li>

              <li className="inline-flex">
                <a
                  href="https://iteam-s.mg/index.html#contact"
                  target="_blank"
                  className="text-blueGray-700 hover:text-blueGray-500 text-sm block mb-4 no-underline font-semibold"
                >
                  <i className="fab fa-css3-alt mr-2 text-blueGray-300 text-base"></i>
                  Contact us
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </>
  );
}
