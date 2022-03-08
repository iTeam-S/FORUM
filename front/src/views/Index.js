/*eslint-disable*/
import React, {useState} from "react";
import {Link} from "react-router-dom"

import bg from '../assets/img/bg.jpg';

import Login from "./auth/Login";
import { LoginService } from "utils/service/LoginService";

/*Components bouttons dashboard*/
const Boutton = () =>{
  const compte = LoginService.getCurrentCompte().type;
  if(compte === 'ADMIN'){
    return(
      <Link to="/admin/TablesEntreprises">
        <button className="w-6/12 bg-blueGray-800 text-white active:bg-lightBlue-600 font-bold uppercase text-base px-3 py-6 rounded shadow-md hover:shadow-lg outline-none focus:outline-none ml-3 ease-linear transition-all duration-150" type="button" style={{margin: '0px 60px'}}> 
            <i className="far fa-chart-bar px-3"></i>Dashboard
        </button>
      </Link>
    )
  } else if (compte === 'ENTREPRISE'){
    return(
    <Link to="/adminEntreprise/ProfilEntreprise">
      <button className="w-6/12 bg-blueGray-800 text-white active:bg-lightBlue-600 font-bold uppercase text-base px-3 py-6 rounded shadow-md hover:shadow-lg outline-none focus:outline-none ml-3 ease-linear transition-all duration-150" type="button" style={{margin: '0px 60px'}}> 
          <i className="far fa-chart-bar px-3"></i>Dashboard
      </button>
    </Link>
  )
  }
}

const AfficheForm = () => {
  if(localStorage.getItem('compte') !== null){
    return (
      <Boutton />
    )
  } else{
    return(
      <Login />
    )
  }
}

export default function Index() {
  
  return (
    <> 
      <div className="h-screen" style={styles.body}>
        <section className="w-11/12 p-4 flex flex-col flex-wrap items-center sm:flex-row sm:w-full md:flex-row md:w-full justify-between">
            <div className="w-full sm:w-5/12 md:w-5/12">
                <div className="w-8/12">
                  Sesame
                </div>
                <div className="sm:w-4/12 md:w-4/12 flex flex-col" style={styles.content_left}>
                  <h1 className="font-semibold text-4xl text-blueGray-600 mb-4">Forum des métiers</h1>
                  <p>
                    Il s’agit d’une plateforme permettant au public de visiter en ligne le forum de 
                    l’emploi et des entreprises  organisé par l’association SÉSAME du 26 mars au 2 avril. 
                    Deux plateforme seront mis à disposition de SÉSAME dans ce projet : chatBot et plateforme web
                  </p>
                  <div className="mt-12">
                      <a
                        href="https://www.creative-tim.com/learning-lab/tailwind/react/overview/notus?ref=nr-index"
                        target="_blank"
                        className="get-started text-white font-bold px-6 py-4 rounded outline-none focus:outline-none mr-1 mb-1  active:bg-teal-600 uppercase text-sm shadow hover:shadow-lg ease-linear transition-all duration-150"
                        style={{backgroundColor: '#057885'}}
                      >
                        Site web
                      </a>
                      <a
                        href="https://github.com/creativetimofficial/notus-react?ref=nr-index"
                        className="github-star ml-1 text-white font-bold px-6 py-4 rounded outline-none focus:outline-none mr-1 mb-1 bg-blueGray-700 active:bg-blueGray-600 uppercase text-sm shadow hover:shadow-lg ease-linear transition-all duration-150"
                        target="_blank"
                      >
                        Facebook
                      </a>
                  </div>
                </div>
            </div>
            <div className="w-full flex flex-col sm:w-5/12 md:w-5/12" style={styles.right} >
              <AfficheForm />
            </div>
        </section>
      </div>
    </>
  );
}

const styles = {
  body: {
    backgroundImage: `url(${bg})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
  },
  content_left: {
    margin: '146px 0px',
    width: '450px'
  },
  right: {
    margin: '90px 0px 0px 0px',

  }
}