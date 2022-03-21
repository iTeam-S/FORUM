import React, {useState, useContext } from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as Yup from 'yup';
import {useHistory} from "react-router";

// components
import CompteService from "utils/service/CompteService";
import { LoginService } from "utils/service/LoginService";
import { CompteContext } from "utils/contexte/CompteContext";


export default function CardEditProfile() {
  const {compte} = useContext(CompteContext);
  const compteCurrent = LoginService.getOneCompteContexte(compte);

  const [erreur,setErreur]=useState(false);
  const [errorMesssage,setErrorMessage]=useState("");
  
  let history = useHistory();

  const validationSchema = Yup.object().shape({
        nom: Yup.string()
          .required('Ce champ est obligatoire'),
        email: Yup.string()
          .required('Ce champ est obligatoire')
          .email("Email invalid"),
        tel: Yup.string()
          .required('Ce champ est obligatoire'),
        domaine: Yup.string()
          .required('le choix est obligatoire'),
        description: Yup.string()
          .required('Ce champ est obligatoire')
          .max(600, "Limité à 97 mots"),
        adresse:Yup.string()
        .required("Ce champ est obligatoire"),
        lien: Yup.string()
          .required('Ce champ est obligatoire'), 
  });

  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    resolver: yupResolver(validationSchema)
  });

  const  handleEditAccount = async(data) => {
        try {
            if(compte !== null){
                await CompteService.UpdateCompte(data.nom,data.email,data.tel,data.domaine,data.description, data.adresse, data.lien)
                history.push('/adminEntreprise/ProfilEntreprise');
                window.location.reload();
            }else{
                setErreur(true);
                setErrorMessage("Echec à la Modification");
            }
        } catch (error) {
            setErreur(true);
        }
    }


  return (
    <>
      <div className="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
        <form onSubmit={handleSubmit(handleEditAccount)}   style={{margin: '0px 0px 100px 0px'}}>
          <div className="rounded-t bg-white mb-0 px-6 py-6">
            <div className="text-center flex justify-between">
              <h6 className="text-blueGray-700 text-xl font-bold">Modifier compte</h6>
              <input 
                className="bg-teal-500 text-white active:bg-lightBlue-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                type="submit"              
                value="Sauvegarder"
              />
            </div>
          </div>
          {
            compteCurrent.map((compte) => (
              <div className="flex-auto px-4 lg:px-10 py-10 pt-0" key={compte.id}>
                <h6 className="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
                  Information
                </h6>
                <div className="flex flex-wrap">
                  <div className="w-full lg:w-6/12 px-4">
                    <div className="relative w-full mb-3">
                      <label
                        className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                      >
                        Nom
                      </label>
                      <input
                        type="text"
                        name="nom"
                        className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                        placeholder="Nom de l'entreprise"
                        defaultValue={compte.nom}
                        {...register('nom')}
                    />
                    <p className="text-red-500 italic">{errors.nom?.message}</p>
                    </div>
                  </div>
                  <div className="w-full lg:w-6/12 px-4">
                    <div className="relative w-full mb-3">
                      <label
                        className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                      >
                        Domaine
                      </label>
                      <select
                        name="domaine"
                        className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                        {...register('domaine')}
                      >
                          <option  defaultValue={compte.domaine} hidden>{compte.domaine} </option>
                          <option key="1" value="Santé">Santé</option>
                          <option key="2" value="Informatique">Informatique</option>
                          <option key="3" value="Commerce et Admnistration">Commerce et Admnistration</option>
                          <option key="4" value="Agronomie">Agronomie</option>
                          <option key="5" value="Science Humaine et Communication">Science Humaine et Communication</option>
                          <option key="6" value="Tourisme">Tourisme</option>
                          <option key="7" value="Industrie et BT">Industrie et BT</option>
                          <option key="8" value="Justice et Force de l'ordre">Justice et Force de l'ordre</option>
                      </select>
                      <p className="text-red-500 italic">{errors.domaine?.message}</p>
                    </div>
                  </div>
                  <div className="w-full lg:w-6/12 px-4">
                    <div className="relative w-full mb-3">
                      <label
                        className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                      >
                        Adresse
                      </label>
                      <input
                        type="text"
                        name="adresse"
                        className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                        placeholder="Votre adresse..."
                        defaultValue={compte.adresse}
                        {...register('adresse')}
                      />
                      <p className="text-red-500 italic">{errors.adresse?.message}</p>
                    </div>
                  </div>

                  <div className="w-full lg:w-6/12 px-4">
                    <div className="relative w-full mb-3">
                      <label
                        className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                      >
                        Site web
                      </label>
                      <input
                        type="url"
                        name="lien"
                        className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                        placeholder="Lien vers votre site.."
                        defaultValue={compte.lien}
                        {...register('lien')}
                      />
                      <p className="text-red-500 italic">{errors.lien?.message}</p>
                    </div>
                  </div>

                  <div className="w-full px-4">
                    <div className="relative w-full mb-3">
                      <label
                        className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                      >
                      Petite description de votre entreprise
                      </label>
                      <input
                        type="text"
                        name="description"
                        className="flex flex-wrap border-0 px-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                        placeholder="Description de l'entreprise"
                        style={{minHeight: '70px'}}
                        defaultValue={compte.description}
                        {...register('description')}
                    />
                    <p className="text-red-500 italic">{errors.description?.message}</p>
                    </div>
                  </div>
                </div>

                <hr className="mt-6 border-b-1 border-blueGray-300" />

                <h6 className="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
                  Contacts
                </h6>
                <div className="flex flex-wrap">
                  <div className="w-full lg:w-6/12 px-4">
                    <div className="relative w-full mb-3">
                      <label
                        className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                      >
                        Numéro téléphone
                      </label>
                      <input
                        type="text"
                        name="tel"
                        placeholder="VOtre numéro téléphone..."
                        className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                        defaultValue={compte.tel}
                        {...register('tel')}
                      />
                      <p className="text-red-500 italic">{errors.tel?.message}</p>
                    </div>
                  </div>
                  <div className="w-full lg:w-6/12 px-4">
                    <div className="relative w-full mb-3">
                      <label
                        className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                      >
                        Email
                      </label>
                      <input
                        type="email"
                        name="email"
                        className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                        defaultValue={compte.email}
                        {...register('email')}
                      />
                      <p className="text-red-500 italic">{errors.email?.message}</p>
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
