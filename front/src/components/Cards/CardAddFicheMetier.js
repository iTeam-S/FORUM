import React, {useState} from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as Yup from 'yup';
import {useHistory} from "react-router";

// components
import CompteService from "utils/service/CompteService";
import { LoginService } from "utils/service/LoginService";

export default function CardAddFicheMetier() {
  const compte = LoginService.getCurrentCompte();
  const [erreur, setErreur] = useState(false);
  const [errorMesssage,setErrorMessage]=useState("");

  let history = useHistory();

  const validationSchema = Yup.object().shape({
        titre: Yup.string()
          .required('Ce champ est obligatoire'),
        domaine_id: Yup.string()
          .required("Ce champ est obligatoire"),
        file: Yup.mixed()
          .test('required', "N'oubliez pas votre fichier, c'est obligatoire", (value) => {
            return value && value.length;
          })
          .test('fileSize', "Le fichier est trop gros", (value) => {
            return value && value[0] && value[0].size <= 500000000;
          })
      });
      const {
        register,
        handleSubmit,
        formState: { errors }
      } = useForm({
        resolver: yupResolver(validationSchema)
      });

  return (
    <>
      <div className="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
        <form>
          <div className="rounded-t bg-white mb-0 px-6 py-6">
            <div className="text-center flex justify-between">
              <h6 className="text-blueGray-700 text-xl font-bold">Nouveau fiche métier</h6>
              <button
                className="bg-teal-500 text-white active:bg-lightBlue-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                type="button"
              >
              
                Ajouter
              </button>
            </div>
          </div>
          <div className="flex-auto px-4 lg:px-10 py-10 pt-0">
              <h6 className="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
                Information sur le fiche métier
              </h6>
              <div className="flex flex-wrap">
                <div className="w-full lg:w-6/12 px-4">
                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="inpTitreFicheMetier"
                    >
                      Titre
                    </label>
                    <input
                      type="text"
                      id="inpTitreFicheMetier"
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   />
                  </div>
                </div>
                <div className="w-full lg:w-6/12 px-4">
                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="inpDomaine"
                    >
                      Domaine
                    </label>
                    <input
                      type="text"
                      id="inpDomaine"
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    />
                  </div>
                </div>
                <div className="w-full lg:w-12/12 px-4">
                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="inpAddFicheMetier"
                    >
                      Fichier (*.jpg ou *.png)
                    </label>
                    <input
                      id="inpAddFicheMetier"
                      type="file"
                      className="transition ease-in-out
                               bg-white bg-clip-padding border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    />
                  </div>
                </div>
              </div>
          </div>
        </form>
      </div>
    </>
  );
}
