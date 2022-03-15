import { RouteAxios } from "utils/urlAxios/UrlAxios";

function login(email, password){
    return RouteAxios.post("/login",{
        email, password
    })
    .then((response) => {
        if(response.data.token){
            localStorage.setItem("compte", JSON.stringify(response.data));
        }
        return response.data;
    })
    .catch((error) =>{
        return error.message;
    })
}

function logout(){
    return localStorage.removeItem('compte');
}

function getCurrentCompte(){
    return JSON.parse(localStorage.getItem('compte'));
}

function getOneCompteContexte(compteFromContexte){
    const compteFromService = getCurrentCompte();
    const compteConv = Object.keys(compteFromContexte).map((cle) =>{
        return compteFromContexte[cle];
    })
    const compteCurrent = compteConv.filter((compteConvertis) => {
        return compteConvertis.id === compteFromService.id;
    })

    return compteCurrent;
}

export const LoginService={
    login,
    logout,
    getCurrentCompte,
    getOneCompteContexte
}