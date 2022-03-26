import React, {useContext} from "react";

// components

import CardStats from "components/Cards/CardStats.js";
import { CompteContext } from "utils/contexte/CompteContext";
import { LoginService } from "utils/service/LoginService";


export default function HeaderStats() {
  let totalCompte, totalContenu, totalVisiteur = 0;
  let id = LoginService.getCurrentCompte().id;
  const {contenus} = useContext(CompteContext);
  const {compte} = useContext(CompteContext);
  const type = JSON.parse(localStorage.getItem('compte')).type;

  let visiteurEntreprise = compte
                          .filter((item) => {
                            return item.id === id;
                          })
                          .map((item) => {
                            return item.visiteurs;
                          })
  

  totalCompte = compte.length;
  totalContenu = contenus.length;

  //total visiteur
  let visiteur = compte.map((account) => {
    return account.visiteurs;
  })

  totalVisiteur = visiteur.reduce((a, b) => a + b, 0);
  


  return (
    <>
      {/* Header */}
      <div className="relative bg-teal-500 md:pt-6 pb-32 pt-20">
        <div className="px-4 md:px-10 mx-auto w-full">
          <div>
            {/* Card stats */}
            <div className="flex flex-wrap justify-center">
              { type === "ADMIN" &&
                  <div className="w-full lg:w-6/12 xl:w-3/12 px-4">
                    <CardStats
                      statSubtitle="Entreprise"
                      statTitle={totalCompte.toString()}
                      statIconName="far fa-chart-bar"
                      statIconColor="bg-red-500"
                    />
                  </div>}
              { type === "ADMIN" ? (
                  <div className="w-full lg:w-6/12 xl:w-4/12 px-4">
                    <CardStats
                      statSubtitle="Tous les visiteurs"
                      statTitle={totalVisiteur.toString()}
                      statIconName="fas fa-users"
                      statIconColor="bg-pink-500"
                    />
                  </div>
                ) : (
                    <div className="w-full lg:w-6/12 xl:w-4/12 px-4">
                      <CardStats
                        statSubtitle="Visiteurs stands"
                        statTitle={visiteurEntreprise.toString()}
                        statIconName="fas fa-users"
                        statIconColor="bg-pink-500"
                      />
                    </div>
                )

              }
              <div className="w-full lg:w-6/12 xl:w-3/12 px-4">
                <CardStats
                  statSubtitle="Contenus"
                  statTitle={totalContenu.toString()}
                  statIconName="fas fa-chart-pie"
                  statIconColor="bg-orange-500"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
