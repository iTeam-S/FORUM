import React, {useContext} from "react";
import { CompteContext } from "utils/contexte/CompteContext";


export default function CardAllContenu() {
  const {contenu} = useContext(CompteContext);

   //convertis le tableau encore en obj en array
  let convertContenu2Tab = Object.keys(contenu).map((cle) => {
    return [contenu[cle]]
  })
  //mapper le tableau convertit et on a nos comptes
  const contenuTab = convertContenu2Tab.map((content) => {
    return content[0];
  });
  console.log(contenuTab)
  return (
    <>
       <div className="w-full sm:w-full md:w-6/12 lg:w-4/12 px-4 text-center mt-4">
          <div className="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg">
            <div className="px-4 py-5 flex-auto">
                <h6 className="text-xl font-semibold">Free Revisions</h6>
                <p className="mt-2 mb-4 text-blueGray-500">
                      Keep you user engaged by providing meaningful information.
                      Remember that by this time, the user is curious.
                </p>
            </div>
            <div className="flex flex-wrap justify-between mx-4">
              <p className="text-blueGray-500">300 vues</p>
              <p className="text-teal-500">Publié</p>
            </div>
            <div className="mt-8 flex flex-row mx-auto sm:w-full md:flex-wrap md:w-12/12 w-6/12">
                <button className="bg-lightBlue-500 w-full text-white active:bg-amber-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button">
                  Édit
                </button>
                <button className="bg-emerald-500 w-full text-white active:bg-emerald-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button">
                  Publié
                </button>
                <button className="bg-red-500 text-white w-full active:bg-red-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button">
                  Delete
                </button>
            </div>
          </div>
        </div>
    </>
  );
}