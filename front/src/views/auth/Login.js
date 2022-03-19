import React, {useState} from "react";
import { useHistory } from "react-router";
import {LoginService} from "utils/service/LoginService";
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as Yup from 'yup';

export default function Login() {
  const [erreur,setErreur]=useState(false)
  const [errormessage,setErrorMessage]=useState("");
  const [type, setType] = useState("password");

  const validationSchema = Yup.object().shape({
    email: Yup.string()
      .required('Email is required')
      .email('Email is invalid'),
    password: Yup.string()
      .required('Password is required')
      .min(6, 'Password must be at least 6 characters')
      .max(40, 'Password must not exceed 40 characters')
  });
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    resolver: yupResolver(validationSchema)
  });

  let history = useHistory();
  const onSubmit = (data) => {
        try {
            LoginService.login(data.email, data.password).then(
                (response) => {
                  if(response.type === 'ENTREPRISE'){
                     history.push('/adminEntreprise/ProfilEntreprise');
                     window.location.reload();
                  }
                  else if(response.type === 'ADMIN'){
                    history.push('/admin/TablesEntreprises');
                     window.location.reload();
                  }
                  else if (response.status === 412){
                    setErreur(true);
                    setErrorMessage("Email ou mot de passe incorrecte!");
                  }
                  else {
                    setErreur(true);
                    setErrorMessage("Email ou mot de passe incorrecte!");
                  }
                })
        } catch (error) {
          setErreur(true);
          setErrorMessage("Serveur en maintenance");
        }
  }

  function viewPassword(e){
    let check = e.target.checked;
    check ? setType("text") : setType("password");
  }
  return (
    <>
      <div className="container px-4 h-full">
        <div className="flex justify-center sm:m-0 h-full">
          <div className="w-8/12 xl:w-8/12 px-4">
            <div className="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg  border-0">
              <div className="flex-auto px-4 lg:px-10 py-10 pt-0">
                <div className="text-white text-center text-4xl mb-3 font-bold">
                  <small>SIGN IN</small>
                </div>
                <form onSubmit={handleSubmit(onSubmit)}>
                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercase text-blueGray-100 text-xs font-bold mb-2"
                      htmlFor="grid-password"
                    >
                      Email
                    </label>
                    <input
                      type="email"
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      placeholder="Email"
                      name="email"
                      {...register('email')}
                    />
                    <p className="text-red-500 bold italic">{errors.email?.message}</p>
                  </div>

                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercase text-blueGray-100 text-xs font-bold mb-2"
                      htmlFor="grid-password"
                    >
                      Password
                    </label>
                    <input
                      type={type}
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      placeholder="Password"
                      name="password"
                      {...register('password')}
                    />
                    <p className="text-red-500 bold italic">{errors.password?.message}</p>
                  </div>
                  <div>
                    <label className="inline-flex items-center cursor-pointer">
                      <input
                        id="customCheckLogin"
                        type="checkbox"
                        className="form-checkbox border-0 rounded text-blueGray-700 ml-1 w-5 h-5 ease-linear transition-all duration-150"
                        onChange={(e) => viewPassword(e)}
                      />
                      <span className="ml-2 text-sm font-semibold text-blueGray-600">
                        Afficher mot de passe
                      </span>
                    </label>
                  </div>

                  <div className="text-center mt-6">
                    <input 
                      className="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                      type="submit"
                      value="Connexion"
                    />
                  </div>
                  { erreur &&(
                      <div className="bg-red-500 border border-red-500 text-red-700 px-4 py-3 rounded relative" role="alert">
                        <strong className="font-bold">Erreur!</strong>
                        <span className="block sm:inline">{errormessage} </span>
                        <span className="absolute top-0 bottom-0 right-0 px-4 py-3">
                            <svg onClick={()=>{setErreur(false)}} className="fill-current h-5 w-12 text-red-400" role="button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><title>Close</title><path d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"/></svg>
                        </span>
                      </div>
                  )}
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
