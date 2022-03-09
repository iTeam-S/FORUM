import React, {useState, useContext } from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as Yup from 'yup';
import {useHistory} from "react-router";

// components
import CompteService from "utils/service/CompteService";
import { LoginService } from "utils/service/LoginService";
import { CompteContext } from "utils/contexte/CompteContext";

export default function CardAddContenu() {
  const compte = LoginService.getCurrentCompte();
  const [erreur, setErreur] = useState(false);
  const [errorMesssage,setErrorMessage]=useState("");
 
  let history = useHistory();
  const { addContenu } = useContext(CompteContext)

  const validationSchema = Yup.object().shape({
        titre: Yup.string()
          .required('Ce champ est obligatoire'),
        description: Yup.string()
          .required("Ce champ est obligatoire si le type n'est pas galerie"),
        type: Yup.string()
          .required('Ce champ est obligatoire'),
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

  

  const convert2base64 = file => {
    const reader = new FileReader();
    reader.onload = (e) => {
      const lien = e.target.value;
      return lien;
    }
    reader.readAsDataURL(file);
  }


  const  handleAddContenu = async(data, e) => {
    e.preventDefault();
        try {
          const fichier = data.file[0];
          const newContenu = await CompteService.AddContenu(data.titre,data.description,data.type, fichier);
            if(compte !== null && (compte.type === 'ADMIN' || compte.type === 'ENTREPRISE')){
                if(data.file.length > 0){
                  addContenu(newContenu.data);
                  history.push('/adminEntreprise/AllContenu');
                  window.location.reload();
                }
            }else{
                setErreur(true);
                setErrorMessage("Echec à l'ajout du nouveau contenu");
            }
        } catch (error) {
            setErreur(true)
            setErrorMessage(error.response.data.message)
        }
    }

  return (
    <>
      <div className="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
        <form onSubmit={handleSubmit(handleAddContenu)}>
          <div className="rounded-t bg-white mb-0 px-6 py-6">
            <div className="text-center flex justify-between">
              <h6 className="text-blueGray-700 text-xl font-bold">Nouveau contenu pour le forum</h6>
              <input 
                className="bg-teal-500 text-white active:bg-lightBlue-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                type="submit"              
                value="Ajouter"
              />
            </div>
          </div>
          <div className="flex-auto px-4 lg:px-10 py-10 pt-0">
              <h6 className="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
                Information sur le contenu
              </h6>
              <div className="flex flex-wrap">
                <div className="w-full lg:w-6/12 px-4">
                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="grid-password"
                    >
                      Titre
                    </label>
                    <input
                      type="text"
                      name="titre"
                      id="inpTitreContenu"
                      {...register('titre')}
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   />
                   <p className="text-red-500 italic">{errors.titre?.message}</p>
                  </div>
                </div>
                <div className="w-full lg:w-6/12 px-4">
                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="inpCategorie"
                    >
                      Type
                    </label>
                    <select
                      name="type"
                      {...register('type')}
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      
                    >
                         <option  hidden>Choisir le type de contenu</option>
                         <option key="1" value="galerie"> galerie</option>
                         <option key="2" value="emploi">offre d'emploi</option>
                         <option key="3" value="information">information</option>
                    </select>
                    <p className="text-red-500 italic">{errors.type?.message}</p>
                  </div>
                </div>
                <div className="w-full lg:w-12/12 px-4">
                  <div className="relative w-full mb-3">
                    <label
                      className="block  text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="inpDescription"
                    >
                      Description   <span className="lowercase">(*à remplir si le type n'est pas galerie*)</span>
                    </label>
                    <input
                      type="text"
                      name="description"
                      {...register('description')}
                      id="inpDescription"
                      style={{height: '100px'}}
                      className="border-0 px-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    />
                    <p className="text-red-500 italic">{errors.description?.message}</p>
                  </div>
                </div>
              </div>

              <hr className="mt-6 border-b-1 border-blueGray-300" />

              <h6 className="text-blueGray-400 text-center text-sm mt-3 mb-6 font-bold uppercase">
                Média
              </h6>
              <div className="flex flex-wrap">
                <div className="w-full lg:w-12/12 px-4">
                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercaseo text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="inpImageContenu"
                    >
                      Fichier (*.jpeg/jpg ou *.png ou *.pdf ou *.mp4)
                    </label>
                    <input
                      type="file"
                      name="file"
                      onChange={(e) => convert2base64(e)}
                      {...register('file')}
                      id="inpImageContenu"
                      accept="image/jpeg, image/jpg, image/png, .pdf, video/*"
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
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
