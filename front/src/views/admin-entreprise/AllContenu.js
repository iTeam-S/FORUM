import React from "react";
import CardAllContenu from "components/Cards/CardAllContenu";


export default function AllContenu() {
  return (
    <>
      <div className="flex flex-wrap bg-blueGray-400 w-full relative mt-20">
        <h2 className="text-3xl font-bold text-center w-full mt-8 text-blueGray-800">Tous les contenus </h2>
        <CardAllContenu />
      </div>
    </>
  );
}
