import React, {useState, useContext } from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as Yup from 'yup';
import {useHistory} from "react-router";

// components
import CompteService from "utils/service/CompteService";
import { LoginService } from "utils/service/LoginService";
import { CompteContext } from "utils/contexte/CompteContext";


export default function CardEditPassword() {
  const {compte} = useContext(CompteContext);
  const compteCurrent = LoginService.getOneCompteContexte(compte);

  const [erreur,setErreur]=useState(false);
  const [errorMesssage,setErrorMessage]=useState("");

  const [pass, setPass] = useState("");

  const firstP = (premier) => {
    let valeur = premier.target.value;
    setPass(valeur);
  }
  const secondP = (second) => {
    let valeur = second.target.value;
    if(valeur !== pass){
      setErreur(true);
      setErrorMessage("Confirmation et nouveau mot de passe doit être les mêmes!")
    } else{
      setErreur(false);
    }
  }

  let history = useHistory();

  const validationPassword = Yup.object().shape({
      old_password: Yup.string()
          .required('Ce champ est obligatoire')
          .min(6, 'Password doit être au minimum 6 characters')
          .max(40, 'Password ne doit pas dépasser les 40 characters'),
      new_password: Yup.string()
          .required('Ce champ est obligatoire')
          .min(6, 'Password doit être au minimum 6 characters')
          .max(40, 'Password ne doit pas dépasser les 40 characters'),
   });

  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    resolver: yupResolver(validationPassword)
  });

  const  handleEditPassword = async(data) => {
        try {
            if(compte !== null){
                await CompteService.UpdatePassword(data.old_password, data.new_password)
                history.push('/adminEntreprise/ProfilEntreprise');
                window.location.reload();
            }else{
                setErreur(true);
                setErrorMessage("Echec à la modification");
            }
        } catch (error) {
            setErreur(true);
        }
    }


  return (
    <>
      <div className="relative mt-4 flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
        <form onSubmit={handleSubmit(handleEditPassword)}>
          <div className="rounded-t bg-white mb-0 px-6 py-6">
            <div className="text-center flex justify-between">
              <h6 className="text-blueGray-700 text-xl font-bold">Modifier mot de passe</h6>
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
                </h6>
                <div className="flex flex-wrap">
                  <div className="w-full lg:w-12/12 px-4">
                    <div className="relative w-full mb-3">
                      <label
                        className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                      >
                        Ancien mot de passe
                      </label>
                      <input
                        type="password"
                        name="password"
                        className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                        placeholder="Ancien mot de passe"
                        {...register('old_password')}
                    />
                    <p className="text-red-500 italic">{errors.old_password?.message}</p>
                    </div>
                  </div>
                  <div className="w-full lg:w-6/12 px-4">
                    <div className="relative w-full mb-3">
                      <label
                        className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                      >
                        Nouveau mot de passe
                      </label>
                      <input
                        type="password"
                        name="passwordNouveau"
                        className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                        placeholder="Nouveau mot de passe"
                        onChange={(premier) => firstP(premier)}
                    />
                      <p className="text-red-500 italic">{errors.password?.message}</p>
                    </div>
                  </div>
                  <div className="w-full lg:w-6/12 px-4">
                    <div className="relative w-full mb-3">
                      <label
                        className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                      >
                        Confirm mot de passe
                      </label>
                      <input
                        type="password"
                        name="new_password"
                        className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                        placeholder="Nouveau mot de passe"
                        {...register('new_password')}
                        onChange={(second) => secondP(second)}
                    />
                      <p className="text-red-500 italic">{errors.password?.message}</p>
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
