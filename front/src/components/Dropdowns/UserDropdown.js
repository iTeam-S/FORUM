import React, {useContext} from "react";
import { Link } from "react-router-dom"
import { createPopper } from "@popperjs/core";

import {LoginService} from "utils/service/LoginService";
import { CompteContext } from "utils/contexte/CompteContext";
import {uRI} from "utils/urlAxios/UrlAxios";


const UserDropdown = () => {
  const idLocal = LoginService.getCurrentCompte().id;
  const {compte} = useContext(CompteContext);
  const compteCurrent = LoginService.getOneCompteContexte(compte);
  //get one item from comptecurrent
  const logo = compteCurrent.map((compte) => {
    return compte.logo;
  })

  const Deconnexion = () => {
    LoginService.logout();
    window.location.reload(true);
  }

  // dropdown props
  const [dropdownPopoverShow, setDropdownPopoverShow] = React.useState(false);
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
  return (
    <>
      <a
        className="text-blueGray-500 block"
        href="#pablo"
        ref={btnDropdownRef}
        onClick={(e) => {
          e.preventDefault();
          dropdownPopoverShow ? closeDropdownPopover() : openDropdownPopover();
        }}
      >
          <div className="items-center flex">
            <span className="w-12 h-12 text-sm text-white bg-blueGray-200 inline-flex items-center justify-center rounded-full">
              <img
                alt="..."
                className="h-12 w-12 bg-white rounded-full align-middle border-none shadow-lg"
                src={logo[0] ? `${uRI}/get_attachement/${idLocal}/${logo[0]}` : require("assets/img/logodefaut.png").default}
              />
            </span>
          </div>
      </a>
      <div
        ref={popoverDropdownRef}
        className={
          (dropdownPopoverShow ? "block " : "hidden ") +
          "bg-white text-base z-50 float-left py-2 list-none text-left rounded shadow-lg min-w-48"
        }
      > 
        { compteCurrent.map((account) => (
            <div key={account.id}>
                 <Link to={`/adminEntreprise/CardEditPassword/${account.id}`}>
                    <p className="text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-blueGray-700">
                      Modifier mot de passe
                    </p>
                  </Link>
                  <a
                    href="/"
                    className={
                      "text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-blueGray-700"
                    }
                    onClick={Deconnexion}
                  >
                    Deconnexion
                  </a>
            </div>
        ))

        }
      </div>
    </>
  );
};

export default UserDropdown;
