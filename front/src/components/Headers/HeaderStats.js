import React, {useContext, useState, useEffect} from "react";

// components

import CardStats from "components/Cards/CardStats.js";
import { LoginService } from "utils/service/LoginService";
import { CompteContext } from "utils/contexte/CompteContext";


export default function HeaderStats() {
  let totalCompte, totalContenu = 0;
  const {contenus} = useContext(CompteContext);
  const {compte} = useContext(CompteContext);
  const type = JSON.parse(localStorage.getItem('compte')).type;

  const compteArray = LoginService.convertItemToArray(compte);
  const contenuArray = LoginService.convertItemToArray(contenus);
  totalCompte = compteArray.length;
  totalContenu = contenuArray.length;


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
                      statTitle={totalCompte}
                      statArrow="up"
                      statPercent="2"
                      statPercentColor="text-emerald-500"
                      statDescripiron="Since yesterday"
                      statIconName="far fa-chart-bar"
                      statIconColor="bg-red-500"
                    />
                  </div>}
              <div className="w-full lg:w-6/12 xl:w-3/12 px-4">
                <CardStats
                  statSubtitle="Visiteurs"
                  statTitle="100"
                  statArrow="up"
                  statPercent="5"
                  statPercentColor="text-emerald-500"
                  statDescripiron="Since yesterday"
                  statIconName="fas fa-users"
                  statIconColor="bg-pink-500"
                />
              </div>
              <div className="w-full lg:w-6/12 xl:w-3/12 px-4">
                <CardStats
                  statSubtitle="Contenus"
                  statTitle={totalContenu}
                  statArrow="up"
                  statPercent="1"
                  statPercentColor="text-emerald-500"
                  statDescripiron="Since yesterday"
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
