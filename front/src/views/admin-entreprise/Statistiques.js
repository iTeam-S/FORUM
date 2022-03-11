import React from "react";

// components

import CardLineChart from "components/Cards/CardLineChart.js";

export default function Statistiques() {
  return (
    <>
      <div className="flex flex-wrap">
        <div className="w-full h-full mb-12 xl:mb-0 px-4">
          <CardLineChart />
        </div>
      </div>
    </>
  );
}
