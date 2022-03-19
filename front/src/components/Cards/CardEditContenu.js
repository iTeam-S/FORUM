import React, {useState, useContext } from "react";
import { useForm } from "react-hook-form";
import { useParams } from "react-router";
import { yupResolver } from "@hookform/resolvers/yup";
import * as Yup from 'yup';
import {useHistory} from "react-router";

// components
import CompteService from "utils/service/CompteService";
import { CompteContext } from "utils/contexte/CompteContext";
import { LoginService } from "utils/service/LoginService";

export default function CardEditContenu() {
  const compte = LoginService.getCurrentCompte();
  const {contenus} = useContext(CompteContext)
  const {id} = useParams();
  const contenuCurrent = LoginService.getOneItemContexte(contenus, id);
  const [erreur, setErreur] = useState(false);
  const [errorMesssage,setErrorMessage]=useState("");

  //disabling description if galerie
  let [isDisabled, setIsDisabled] = useState(true);
  const onChangeTypeSelect = (e) => {
      let choice = e.target.value;
      if(choice === "galerie"){
        setIsDisabled(true);
      } else {
        setIsDisabled(false)
      }
      
  }

  let history = useHistory();

  const validationSchema = Yup.object().shape({
        titre: Yup.string()
          .required('Ce champ est obligatoire'),
        description: Yup.string()
          .max(2000, "La description doit être inférieur à 2000 caractères")
          .nullable(true),
        type: Yup.string()
          .required('Ce champ est obligatoire'),
        content_id: Yup.number(),
        file: Yup.mixed()
        .nullable()
        .notRequired()
      });
      const {
        register,
        handleSubmit,
        formState: { errors }
      } = useForm({
        resolver: yupResolver(validationSchema)
      });


  const  handleEditContenu = async(data) => {
        try {
            if(compte !== null && (compte.type === 'ADMIN' || compte.type === 'ENTREPRISE')){
                  await CompteService.UpdateOneContent(data.titre,data.description,data.type, data.content_id, data.file);
                  history.push('/adminEntreprise/AllContenu');
                  window.location.reload();
                  console.log(data.file)
            }else{
                setErreur(true);
                setErrorMessage("Echec à la modification du contenu");
            }
        } catch (error) {
            setErreur(true)
            setErrorMessage(error.response.data.message)
        }
    }

  return (
    <>
      <div className="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
        <form onSubmit={handleSubmit(handleEditContenu)}>
          <div className="rounded-t bg-white mb-0 px-6 py-6">
            <div className="text-center flex justify-between">
              <h6 className="text-blueGray-700 text-xl font-bold">Modifier le contenu</h6>
              <input 
                className="bg-teal-500 text-white active:bg-lightBlue-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                type="submit"              
                value="Sauvegarder"
              />
            </div>
          </div>
          { contenuCurrent.map((contenu) => (
            <div className="flex-auto px-4 lg:px-10 py-10 pt-0" key={contenu.id}>
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
                      defaultValue={contenu.titre}
                      {...register('titre')}
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   />
                   <p className="text-red-500 italic">{errors.titre?.message}</p>
                  </div>
                </div>
                <div className="w-full lg:w-6/12 px-4">
                  <div className="relative w-full mb-3">
                    <label
                      className="block  text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="inpCategorie"
                    >
                     <span className="uppercase"> Type </span> <span className="lowercase">     (*N'oubliez pas de choisir le type!*)</span>
                    </label>
                    <select
                      name="type"
                      {...register('type')}
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      onChange={(e) => onChangeTypeSelect(e)}
                    >
                         <option key="1" value={contenu.type}  hidden>{contenu.type}</option>
                         <option key="2" value="galerie"> galerie</option>
                         <option key="3" value="emploi">offre d'emploi</option>
                         <option key="4" value="information">information</option>
                    </select>
                    <p className="text-red-500 italic">{errors.type?.message}</p>
                  </div>
                </div>
                <div className="w-full lg:w-12/12 px-4" hidden={isDisabled}>
                  <div className="relative w-full mb-3">
                    <label
                      className="block  text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="inpDescription"
                    >
                      Description   <span className="lowercase">(*à remplir si le type n'est pas galerie s'il vous plaît*)</span>
                    </label>
                    <input
                      type="text"
                      name="description"
                      defaultValue={contenu.description}
                      {...register('description')}
                      id="inpDescription"
                      style={{height: '100px'}}
                      className="border-0 px-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    />
                  </div>
                </div>
              </div>
              <div>
                  <input type="text" name="content_id" defaultValue={parseInt(id)} {...register('content_id')} hidden/>
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
                      {...register('file')}
                      id="inpImageContenu"
                      accept="image/jpeg, image/jpg, image/png, .pdf, video/*"
                      multiple
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    />
                    <p className="text-red-500 italic">{errors.file?.message}</p>
                  </div>
                </div>
              </div>
            </div>
          ))

          }
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
