import React from "react";
import { Link } from "react-router-dom";
import { useParams } from "react-router";

//components
import { LoginService } from "utils/service/LoginService";

export default function CardOtherProfil() {
  const {id} = useParams();
  return (
    <>
      <div className="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg mt-16">
        <div className="px-6">
          <div className="flex flex-wrap justify-center">
            <div className="w-full px-4 flex justify-center">
              <div className="relative">
                <img
                  alt="..."
                  src={require("assets/img/team-2-800x800.jpg").default}
                  className="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px"
                />
              </div>
            </div>
            <div className="w-8/12 lg:w-4/12 opx-4 text-right lg:order-3">
              <div className="py-6 px-3 sm:mt-0" style={{marginLeft: '70px'}}>
                <Link
                    to="/adminEntreprise/CardEditProfile/"
                    className="text-blueGray-700 text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase"
                  >
                    <button
                    className="bg-teal-500 active:bg-lightBlue-600 uppercase text-white font-bold hover:shadow-md shadow text-xs px-4 py-2 rounded outline-none focus:outline-none sm:mr-2 mb-1 ease-linear transition-all duration-150"
                    type="button"
                  >
                    Modifier
                  </button>
                </Link>
              </div>
            </div>
            <div className="w-6/12 px-4 text-center mt-0">
              <div className="flex justify-center py-4 lg:pt-4 pt-8">
                <div className="mr-4 p-3 text-center">
                  <span className="text-xl font-bold block uppercase tracking-wide text-blueGray-600">
                  </span>
                </div>
              </div>
            </div>
          </div>
          <div className="text-center mt-12">
            <h3 className="text-xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2">
              Nom
            </h3>
            <div className="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase">
              <i className="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"></i>{" "}
              Adresse
            </div>
            <div className="mb-2 text-blueGray-600">
              <i className="fas fa-envelope mr-2 text-lg text-blueGray-400"></i>
                 Email
            </div>
            <div className="mb-2 text-blueGray-600">
              <i className="fas fa-address-card mr-2 text-lg text-blueGray-400"></i>
                Telephone
            </div>
            <div className="mb-2 text-blueGray-600">
              <i className="fas fa-university mr-2 text-lg text-blueGray-400"></i>
                <a href="lien" target="_blank" rel="noreferrer" >Site web</a>
            </div>
          </div>
          <div className="mt-10 py-10 border-t border-blueGray-200 text-center">
            <div className="flex flex-wrap justify-center">
              <div className="w-full lg:w-9/12 px-4">
                <p className="mb-4 text-lg leading-relaxed text-blueGray-700">
                  Description
                </p>
                <div className="w-full flex">
                  {/*<video src={video} controls="controls" autoPlay={true} />*/}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}