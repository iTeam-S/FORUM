import React, {useState, useContext } from "react";
import { useForm } from "react-hook-form";
import { useParams } from "react-router";
import { yupResolver } from "@hookform/resolvers/yup";
import * as Yup from 'yup';
import {useHistory} from "react-router";

// components
import CompteService from "utils/service/CompteService";
import { LoginService } from "utils/service/LoginService";
import { CompteContext } from "utils/contexte/CompteContext";


export default function CardAddVideo() {
  const {compte} = useContext(CompteContext);
  const compteCurrent = LoginService.getOneCompteContexte(compte);

  const [erreur,setErreur]=useState(false);
  const [errorMesssage,setErrorMessage]=useState("");

  const [hiddenLien, setHiddenLien] = useState(false);
  const [hiddenFile, setHiddenFile] = useState(false);

  //fonction pour controller le choix de l'user
  function HiddenFile(e){
    let valeur = e.target.value;
    if(valeur.length > 0){
      setHiddenFile(true);
    } else {
      setHiddenFile(false)
    }
  }
  function HiddenLien(e){
    let valeur = e.target.value;
    if(valeur.length > 0){
      setHiddenLien(true);
    } else{
      setHiddenLien(false);
    }
  }

  let history = useHistory();

  const validationPassword = Yup.object().shape({
      lien: Yup.string()
        .nullable(true)
        .notRequired(),
      video: Yup.mixed()
        .nullable()
        .notRequired(),
   });

  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    resolver: yupResolver(validationPassword)
  });

  const  handleAddVideo = async(data) => {
        try {
            if(compte !== null){
               /* await CompteService.AddVideo(data.lien, data.video)
                history.push('/adminEntreprise/ProfilEntreprise');
                window.location.reload();*/
            }else{
                setErreur(true);
                setErrorMessage("Echec à l'ajout de la vidéo");
            }
        } catch (error) {
            setErreur(true);
        }
    }


  return (
    <>
      <div className="relative mt-4 flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
        <form onSubmit={handleSubmit(handleAddVideo)}>
          <div className="rounded-t bg-white mb-0 px-6 py-6">
            <div className="text-center flex justify-between">
              <h6 className="text-blueGray-700 text-xl font-bold">Ajouter votre vidéo de présentation</h6>
              <input 
                className="bg-teal-500 text-white active:bg-lightBlue-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                type="submit"              
                value="Ajouter"
              />
            </div>
          </div>


                <h6 className="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
                  Vidéo de presentation  (*Vous pouvez insérer soit par fichier soit via lien facebook*)
                </h6>
                <div className="flex flex-wrap">
                  <div className="w-full lg:w-6/12 px-4" hidden={hiddenLien}>
                    <div className="relative w-full mb-3">
                      <label
                        className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                      >
                        Video via lien facebook
                      </label>
                      <input
                        type="url"
                        name="lien"
                        className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                        {...register('lien')}
                        placeholder="Lien vers le video sur facebook..."
                        onChange={(e) => HiddenFile(e)}
                      />
                    </div>
                  </div>

                   <div className="w-full lg:w-6/12 px-4" hidden={hiddenFile}>
                    <div className="relative w-full mb-3">
                      <label
                        className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                      >
                        Video via fichier (*.mp4 et inférieur à 25 Mb*)
                      </label>
                      <input
                        type="file"
                        name="fileVideo"
                        accept="video/mp4"
                        className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                        {...register('video')}
                        onChange={(e) => HiddenLien(e)}
                      />
                      <p className="text-red-500 italic">{errors.lienf?.message}</p>
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
