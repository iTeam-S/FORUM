import React, {useContext, useState} from "react";
import { Link } from "react-router-dom"
import { createPopper } from "@popperjs/core";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as Yup from 'yup';

//style css
import '../../assets/styles/cardStyle.css';


//components
import { LoginService } from "utils/service/LoginService";
import { CompteContext } from "utils/contexte/CompteContext";
import CompteService from "utils/service/CompteService";
import {uRI} from "utils/urlAxios/UrlAxios";


export default function CardProfile() {
  const {compte} = useContext(CompteContext);
  const compteCurrent = LoginService.getOneCompteContexte(compte);
  const [erreur, setErreur] = useState(false);
  const [errorMesssage,setErrorMessage]=useState("");

  console.log(compte)  
  

  //get one item from comptecurrent
  const idCompte = compteCurrent.map((compte) => {
    return compte.id;
  })
  const linkVideo = compteCurrent.map((compte) => {
    return compte.video;
  })
  //regex video facebook
  const regexVideoFb = /^(https?:\/\/){0,1}(www\.){0,1}facebook\.com\/(.){5,}\/videos\/[0-9]{15}/;
  const ComponentVideo = () => {
    if (regexVideoFb.test(linkVideo[0])){
      return (
          <div>
            <iframe src = {`https://www.facebook.com/plugins/video.php?href=${linkVideo[0]}/&width=500&show_text=false&appId=823777418309594&height=280`} style={{ border:'none', overflow: 'hidden'}} 
                  className="w-full flex justify-center relative"
                  frameBorder="0" 
                  title="Video facebook"
                  allowFullScreen={true} 
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          />
          <Link
                  to={`/adminEntreprise/CardAddVideo/${idCompte}`}
                  className="bg-teal-500 active:bg-lightBlue-600 uppercase px-4 py-2 text-white font-bold hover:shadow-md shadow rounded outline-none focus:outline-none sm:mr-2 mb-1 ease-linear transition-all duration-150"
          >
            <button
                  className="text-sm font-bold px-4 py-"
                  type="button"
                  style={{margin: '20px 0px'}}
            >
                  Remplacer
            </button>
          </Link>
          </div>
    )
    } else{
      if(linkVideo[0] !== null){
          return(
              <div>
                  <video src={`${uRI}/get_attachement/${idCompte}/${linkVideo[0]}#t=90000,100000`} controls="controls" autoPlay={true} />
                  <Link
                  to={`/adminEntreprise/CardAddVideo/${idCompte}`}
                  className="bg-teal-500 active:bg-lightBlue-600 uppercase px-4 py-2 text-white font-bold hover:shadow-md shadow rounded outline-none focus:outline-none sm:mr-2 mb-1 ease-linear transition-all duration-150"
                    >
                      <button
                            className="text-sm font-bold px-4 py-"
                            type="button"
                            style={{margin: '20px 0px'}}
                      >
                            Remplacer
                      </button>
                  </Link>
              </div>
          )
      } else {
          return(
              <div>
                <p className="text-xs font-semibold leading-normal mb-2 text-blueGray-700 mb-2">Il n'a pas encore de vidéo de présentation</p>
                <Link
                      to={`/adminEntreprise/CardAddVideo/${idCompte}`}
                      className="bg-teal-500 active:bg-lightBlue-600 uppercase px-4 py-2 text-white font-bold hover:shadow-md shadow rounded outline-none focus:outline-none sm:mr-2 mb-1 ease-linear transition-all duration-150"
                    >
                      <button
                      className="text-xl font-bold px-5 py-1"
                      type="button"
                  >
                      +
                  </button>
                  </Link>
              </div>
            )
      }
    }
  }

  // dropdown props
  const [dropdownPopoverShow, setDropdownPopoverShow] = useState(false);
  const btnDropdownRef = React.createRef();
  const popoverDropdownRef = React.createRef();
  const openDropdownPopover = () => {
    createPopper(btnDropdownRef.current, popoverDropdownRef.current, {
      placement: "bottom-start",
    });
    setDropdownPopoverShow(true);
  };
  const closeDropdownPopover = () => {
    setDropdownPopoverShow(false);
  };
  const validationSchema = Yup.object().shape({
        logo: Yup.mixed()
          .test('required', "N'oubliez pas votre image, c'est important", (value) => {
            return value && value.length;
          })
          .test('fileSize', "Le logo est trop gros", (value) => {
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


  const  handleEditLogo = async(data) => {
        try {
            if(compte !== null){
                  await CompteService.UpdateLogo(data.logo[0]);
                  window.location.reload();
            }else{
                setErreur(true);
                setErrorMessage("Echec à la modification du logo");
            }
        } catch (error) {
            setErreur(true)
            setErrorMessage(error.response.data.message)
        }
      }

  return (
    <>
      { compteCurrent.map((account) => (
        <div className="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg mt-16" key={account.id}>
          <div className="px-6">
            <div className="flex flex-wrap justify-center">
              <div className="w-full px-4 flex justify-center">
                <div className="relative photo">
                  <a
                    className="text-blueGray-500 block"
                    href="#pablo"
                    ref={btnDropdownRef}
                    onClick={(e) => {
                      e.preventDefault();
                      dropdownPopoverShow ? closeDropdownPopover() : openDropdownPopover();
                    }}
                  >
                    <img
                      alt="..."
                      src={account.logo ? `${uRI}/get_attachement/${idCompte}/${account.logo}` : require("assets/img/logodefaut.png").default}
                      className="shadow-xl rounded-full image-size align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px"
                    />
                  </a>
                  <form onSubmit={handleSubmit(handleEditLogo)}>
                      <div
                          ref={popoverDropdownRef}
                          className={
                            (dropdownPopoverShow ? "block " : "hidden ") +
                            "bg-blueGray-200 text-base z-50 float-left py-4 px-4 list-none text-left rounded shadow-lg min-w-48"
                          }
                        >
                            <input
                              id="imageprofil"
                              type="file"
                              {...register('logo')}
                            />
                            <p className="text-red-500 italic">{errors.logo?.message}</p>
                            <input 
                               className="bg-teal-500 sauvegarde text-white active:bg-lightBlue-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                                type="submit"              
                                value="Sauvegarder" 
                            />
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
              </div>
              <div className="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                <div className="py-6 px-3 mt-32 sm:mt-0">
                  <Link
                      to="/adminEntreprise/CardEditProfile"
                      className="bg-teal-500 active:bg-lightBlue-600 uppercase px-4 py-2 text-white font-bold hover:shadow-md shadow rounded outline-none focus:outline-none sm:mr-2 mb-1 ease-linear transition-all duration-150"
                    >
                      <button
                      className="text-sm font-bold px-4 py-"
                      type="button"
                  >
                      Modifier
                  </button>
                  </Link>
                </div>
              </div>
              <div className="w-6/12 px-4 text-center mt-0">
                <div className="flex justify-center py-4 lg:pt-4 pt-8">
                  <div className="mr-4 p-3 text-center">
                    <span className="text-xl font-bold block uppercase tracking-wide text-blueGray-600">
                    </span>
                  </div>
                </div>
              </div>
            </div>
            <div className="text-center mt-12">
              <h3 className="text-xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2">
                {account.nom}
              </h3>
              <div className="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase">
                <i className="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"></i>{" "}
                {account.adresse}
              </div>
              <div className="mb-2 text-blueGray-600">
                <i className="fas fa-envelope mr-2 text-lg text-blueGray-400"></i>
                  {account.email}
              </div>
              <div className="mb-2 text-blueGray-600">
                <i className="fas fa-address-card mr-2 text-lg text-blueGray-400"></i>
                  {account.tel}
              </div>
              { account.lien !== "" ? (
                    <div className="mb-2 text-blueGray-600">
                      <i className="fas fa-university mr-2 text-lg text-blueGray-400"></i>
                        <a href={account.lien} target="_blank" rel="noreferrer" >Site web</a>
                    </div>
                ) : (
                    <div className="mb-2 text-blueGray-600">
                        <p style={{margin:'0px 0px 30px 0px'}} >Lien site web pas encore disponible.</p>
                    </div>
                )
              }
            </div>
            <div className="mt-10 py-10 border-t border-blueGray-200 text-center" style={{margin: '0px 0px 100px 0px'}}>
              <div className="flex flex-wrap justify-center">
                <div className="w-full lg:w-9/12 px-4">
                  <p className="mb-4 text-lg leading-relaxed text-blueGray-700">
                    {account.description}
                  </p>
                  <div className="w-full flex video" >
                    <ComponentVideo />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      ))
      }
    </>
  );
}