import React from "react";
import { Link } from "react-router-dom";
import CompteService from "utils/service/CompteService";

import '../../assets/styles/cardStyle.css';


export default function CardAllContenu({allContenu, termSearch}) {

  //Fonction delete contenus
  async function deleteContent(id_content){
     await CompteService.DeleteOneContent(id_content);
      window.location.reload();
  }

  return (
    <>
        {/* conver obj to array */}
       { allContenu.filter((content) => {
            return content.titre.toLowerCase().includes(termSearch.toLocaleLowerCase());
          }).map((content) => (
              <div className="w-full  md:w-full lg:w-6/12 xl:w-4/12 px-4 text-center mt-4" key={content.id} >
                <div className="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg">
                  <div className="px-4 py-5 flex-auto">
                      <h6 className="text-xl font-semibold">{content.titre}</h6>
                      <div className="  mt-2 mb-4 text-blueGray-500">
                        <p className="description">
                          {content.description}
                        </p>
                      </div>
                  </div>
                  <div className="flex flex-wrap justify-between mx-4">
                    <p className="text-blueGray-500">{content.Vues} vues</p>
                    <p className="text-teal-500">Publié</p>
                  </div>
                  <div className="mt-8 flex flex-row mx-auto sm:w-full md:flex-wrap md:w-12/12 w-6/12">
                      <Link to={`/adminEntreprise/CardEditContenu/${content.id}`}
                            className="bg-lightBlue-500 w-full text-white active:bg-amber-600 font-bold rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                      >
                        <button className="uppercase text-xs px-4 py-2 font-bold  bg-lightBlue-500 w-full active:bg-amber-600" type="button">
                        Édit
                      </button> 
                      </Link>
                      <button className="bg-emerald-500 w-full text-white active:bg-emerald-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button">
                        Publié
                      </button>
                      <button className="bg-red-500 text-white w-full active:bg-red-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                      type="button"
                      onClick={(e) => {
                        e.preventDefault();
                        deleteContent(content.id);
                      }}
                      >
                        Delete
                      </button>
                  </div>
                </div>
              </div>
       ))}
    </>
  );
}