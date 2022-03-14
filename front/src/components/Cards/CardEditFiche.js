import React, {useState} from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as Yup from 'yup';
import {useHistory} from "react-router";

// components
import CompteService from "utils/service/CompteService";
import { LoginService } from "utils/service/LoginService";

export default function CardEditFiche() {
  const compte = LoginService.getCurrentCompte();
  const [erreur, setErreur] = useState(false);
  const [errorMesssage,setErrorMessage]=useState("");

  let history = useHistory();

  const validationSchema = Yup.object().shape({
        titre: Yup.string()
          .required('Ce champ est obligatoire'),
        domaine_id: Yup.number()
          .required("Ce champ est obligatoire")
          .positive('Nombre positive'),
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

      const  handleEditFiche = async(data) => {
        try {
            if(compte !== null && compte.type === 'ADMIN'){
                if(data.file.length > 0){
                  await CompteService.AddFicheMetier(data.titre, data.domaine_id, data.file[0]);
                  history.push('/admin/AllFicheMetier');
                  window.location.reload();
                }
            }else{
                setErreur(true);
                setErrorMessage("Echec à l'ajout du nouveau fiche métier");
            }
        } catch (error) {
            setErreur(true)
            setErrorMessage(error.response.data.message)
        }
    }

  return (
    <>
      <div className="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
        <form onSubmit={handleSubmit(handleEditFiche)} >
          <div className="rounded-t bg-white mb-0 px-6 py-6">
            <div className="text-center flex justify-between">
              <h6 className="text-blueGray-700 text-xl font-bold">Modifier le fiche métier</h6>
              <input 
                className="bg-teal-500 text-white active:bg-lightBlue-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                type="submit"              
                value="Modifier"
              />
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
                      name="titre"
                      {...register('titre')}
                      id="inpTitreFicheMetier"
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   />
                   <p className="text-red-500 italic">{errors.titre?.message}</p>
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
                    <select
                      name="domaine"
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      {...register('domaine_id')}
                    >
                         <option  value="" hidden>Choisir le domaine</option>
                         <option key="1" value="1">Santé</option>
                         <option key="2" value="2">Informatique</option>
                         <option key="3" value="3">Commerce et Admnistration</option>
                         <option key="4" value="4">Agronomie</option>
                         <option key="5" value="5">Science Humaine et Communication</option>
                         <option key="6" value="6">Tourisme</option>
                         <option key="7" value="7">Industrie et BT</option>
                         <option key="8" value="8">Justice et Force de l'ordre</option>
                    </select>
                    <p className="text-red-500 italic">{errors.domaine_id?.message}</p>
                  </div>
                </div>
                <div className="w-full lg:w-12/12 px-4">
                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="inpAddFicheMetier"
                    >
                      Fichier (*.jpg ou *.png ou *.pdf)
                    </label>
                    <input
                      id="inpAddFicheMetier"
                      name="file"
                      type="file"
                      {...register('file')}
                      accept="image/jpeg, image/jpg, image/png, .pdf, video/*"
                      className="transition ease-in-out
                               bg-white bg-clip-padding border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    />
                    <p className="text-red-500 italic">{errors.file?.message}</p>
                  </div>
                </div>
              </div>
          </div>
        </form>
        {erreur &&(
                  <div className="bg-rose-300 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                      <strong className="font-bold">Erreur!</strong>
                          <span className="block sm:inline">{errorMesssage} </span>
                          <span className="absolute top-0 bottom-0 right-0 px-4 py-3">
                              <svg onClick={()=>{setErreur(false)}} className="fill-current h-5 w-12 text-red-500" role="button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><title>Close</title><path d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"/></svg>
                            </span>
                  </div>
          )}
      </div>
    </>
  );
}
