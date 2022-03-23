import React, {useContext} from "react";
import { useParams } from "react-router";


//contexte
import { CompteContext } from "utils/contexte/CompteContext";
import { LoginService } from "utils/service/LoginService";
import {uRI} from "utils/urlAxios/UrlAxios";

//style
import '../../assets/styles/cardStyle.css';


export default function CardOtherProfil() {
  const {id} = useParams();
  const {compte} = useContext(CompteContext);
  const compteCurrent = LoginService.getOneItemContexte(compte, id);

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
          <iframe src = {`https://www.facebook.com/plugins/video.php?href=${linkVideo[0]}/&width=500&show_text=false&appId=823777418309594&height=280`} style={{ border:'none', overflow: 'hidden'}} 
                  className="w-full flex justify-center relative"
                  frameBorder="0" 
                  title="Video facebook"
                  allowFullScreen={true} 
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          />
    )
    } else{
      if(linkVideo[0] !== null){
          return(
              <video src={`${uRI}/get_attachement/${idCompte}/${linkVideo[0]}`} controls="controls" autoPlay={true} />
          )
      } else {
          return(
              <p className="text-xs font-semibold leading-normal text-blueGray-700 mb-2">Il n'a pas encore de vidéo de présentation</p>
            )
      }
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
                      <img
                        alt="..."
                        src={account.logo ? `${uRI}/get_attachement/${id}/${account.logo}` : require("assets/img/logodefaut.png").default}
                        className="shadow-xl rounded-full image-size align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px"
                      />
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
                  <div className="mb-2 text-blueGray-600">
                    <i className="fas fa-university mr-2 text-lg text-blueGray-400"></i>
                      <a href={account.lien} target="_blank" rel="noreferrer" >Site web</a>
                  </div>
                </div>
                <div className="mt-10 py-10 border-t border-blueGray-200 text-center">
                  <div className="flex flex-wrap justify-center">
                    <div className="w-full lg:w-9/12 px-4">
                      <p className="mb-4 text-lg leading-relaxed text-blueGray-700">
                        {account.description}
                      </p>
                      <div className="w-full flex video">
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