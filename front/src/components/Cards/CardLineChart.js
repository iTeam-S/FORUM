import React, {useContext, useEffect} from 'react';
import Chart from "chart.js";

import { CompteContext } from "utils/contexte/CompteContext";

export default function CardLineChart() {
  const {stat} = useContext(CompteContext);
  let nbreVisiteur = [0];
  let jour = [""];


  useEffect(() => {
    //MANIPULATION DATE

    let dateBrute = stat.map((date) => {
      return date.date;
    })
    for(let i=0; i<dateBrute.length; i++){
      let dateParse = new Date(dateBrute[i]);
      let NumberJourFromDateParse = dateParse.getDay()
      let nomDay = ""
      switch (NumberJourFromDateParse){
        case 1:
          nomDay = "Lundi"
          break;
        case 2:
          nomDay = "Mardi"
          break;
        case 3:
          nomDay = "Mercredi"
          break;
        case 4:
          nomDay = "Jeudi"
          break;
        case 5:
          nomDay = "Vendredi"
          break;
        case 6:
          nomDay = "Samedi"
          break;
        case 7:
          nomDay = "Dimanche"
          break;
        default:
          nomDay = ""
      }
      jour.push(nomDay)
    }

    //FIN DATE 


    //NOMBRE DE VISITE ONLY
    
    //get vue only in array stat
    let vue = stat.map((nbre) => {
      return nbre.Vues;
    })
    //integre vue one by one in nbreVisteur(donné a affiché)
    for(let i = 0; i < vue.length; i++){
      nbreVisiteur.push(vue[i]);
    }
    //FIN NOMBRE DE VISITE 


    function graph(){
      
          var config = {
          type: "line",
          data: {
            labels: jour,
            datasets: [
              {
                label: "Visite contenus",
                backgroundColor: "#02d47c",
                borderColor: "#02d47c",
                data: nbreVisiteur,
                fill: false,
              },
            ],
          },
          options: {
            maintainAspectRatio: false,
            responsive: true,
            title: {
              display: false,
              text: "Stats chart",
              fontColor: "white",
            },
            legend: {
              labels: {
                fontColor: "white",
              },
              align: "end",
              position: "bottom",
            },
            tooltips: {
              mode: "index",
              intersect: false,
            },
            hover: {
              mode: "nearest",
              intersect: true,
            },
            scales: {
              xAxes: [
                {
                  ticks: {
                    fontColor: "rgba(255,255,255,.7)",
                  },
                  display: true,
                  scaleLabel: {
                    display: false,
                    labelString: "Day",
                    fontColor: "white",
                  },
                  gridLines: {
                    display: false,
                    borderDash: [2],
                    borderDashOffset: [2],
                    color: "rgba(33, 37, 41, 0.3)",
                    zeroLineColor: "rgba(0, 0, 0, 0)",
                    zeroLineBorderDash: [2],
                    zeroLineBorderDashOffset: [2],
                  },
                },
              ],
              yAxes: [
                {
                  ticks: {
                    fontColor: "rgba(255,255,255,.7)",
                  },
                  display: true,
                  scaleLabel: {
                    display: false,
                    labelString: "Value",
                    fontColor: "white",
                  },
                  gridLines: {
                    borderDash: [3],
                    borderDashOffset: [3],
                    drawBorder: false,
                    color: "rgba(255, 255, 255, 0.15)",
                    zeroLineColor: "rgba(33, 37, 41, 0)",
                    zeroLineBorderDash: [2],
                    zeroLineBorderDashOffset: [2],
                  },
                },
              ],
            },
          },
        };
        var ctx = document.getElementById("line-chart").getContext("2d");
        window.myLine = new Chart(ctx, config);
    }
    async function LineChart (){
      try{
        graph()
        
      } catch(erreur){
        console.log(erreur);
      }
      
    }
    LineChart();
    // eslint-disable-next-line 
  }, [stat])

    
  return (
    <>
      <div className="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-blueGray-700">
        <div className="rounded-t mb-0 px-4 py-3 bg-transparent">
          <div className="flex flex-wrap items-center">
            <div className="relative w-full max-w-full flex-grow flex-1">
              <h6 className="uppercase text-blueGray-100 mb-1 text-xs font-semibold">
                Statistique
              </h6>
              <h2 className="text-white text-xl font-semibold">Consultation de contenu</h2>
            </div>
          </div>
        </div>
        <div className="p-4 flex-auto">
          {/* Chart */}
          <div className="relative h-350-px">
            <canvas id="line-chart"></canvas>
          </div>
        </div>
      </div>
    </>
  );
}
