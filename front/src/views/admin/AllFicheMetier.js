import React from "react";

// components

import CardAllFiche from "components/Cards/CardAllFiche";

export default function AllFicheMetier() {
  return (
    <>
      <div className="flex flex-wrap mt-4">
        <div className="w-full mb-12 px-4">
          <CardAllFiche color="light" />
        </div>
      </div>
    </>
  );
}
