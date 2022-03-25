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
  const {contenus, setContenu, addContenu}=useContext(CompteContext)
  let [isDisabled, setIsDisabled] = useState(true);

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

  const onChangeTypeSelect = (e) => {
      let choice = e.target.value;
      choice !== "galerie" ? setIsDisabled(false) : setIsDisabled(true);
  }

  let history = useHistory();

  const validationSchema = Yup.object().shape({
        titre: Yup.string()
          .required('Ce champ est obligatoire'),
        description: Yup.string()
          .nullable(true),
        type: Yup.string()
          .required('Ce champ est obligatoire'),
        file: Yup.mixed()
          .nullable()
          .notRequired(),
        lien: Yup.string()
          .nullable()
          .notRequired()
      });

  
  const  handleAddContenu = async(data) => {
        try {
            let newContenu = {}
            let res = await CompteService.AddContenu(data.titre,data.description,data.type, data.file, data.lien);
            let formdata = res.config.data;
            formdata.delete('file');
            for(let value of formdata.entries()){
                newContenu[value[0]] = value[1];
            }

            if(compte !== null){
                history.push('/adminEntreprise/AllContenu');
            }else{
                setErreur(true);
                setErrorMessage("Echec à l'ajout du nouveau contenu");
            }

            newContenu['id'] = res.data.id;
            setContenu([...contenus, newContenu]);
            addContenu(newContenu);
        } catch (error) {
            setErreur(true)
            setErrorMessage(error.response.data.message)
        }
    }
    
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
                      onChange={onChangeTypeSelect}
                    >
                         <option  hidden>Choisir le type de contenu</option>
                         <option key="1" value="galerie"> Galerie</option>
                         <option key="2" value="emploi">Offre d'emploi</option>
                         <option key="3" value="actu">Actualité</option>
                         <option key="4" value="formation">Formation</option>
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
              <div className="flex flex-wrap" >
                <div className="w-full lg:w-6/12 px-4" hidden={hiddenFile}>
                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercaseo text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="inpImageContenu"
                    >
                      Fichier (*.jpeg/jpg ou *.png ou *.pdf ou *.mp4 moins de 25Mo)
                    </label>
                    <input
                      type="file"
                      name="file"
                      multiple={isDisabled}
                      {...register('file')}
                      onChange={(e) => HiddenLien(e)}
                      id="inpImageContenu"
                      accept="image/jpeg, image/jpg, image/png, .pdf, video/*"
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    />
                    <p className="text-red-500 italic">{errors.file?.message}</p>
                  </div>
                </div>
                <div className="w-full lg:w-6/12 px-4" hidden={hiddenLien}>
                    <div className="relative w-full mb-3">
                      <label
                        className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                      >
                        Soit lien (facebook, Linkedin)
                      </label>
                      <input
                        type="url"
                        name="lien"
                        className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                        {...register('lien')}
                        onChange={(e) => HiddenFile(e)}
                      />
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
