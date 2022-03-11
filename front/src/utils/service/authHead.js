export default function authHead(){
    const compte = JSON.parse(localStorage.getItem('compte'));

    if(compte && compte.token){
        return { 'x-acces-token' : compte.token }
    } else{
        return {}
    }
}