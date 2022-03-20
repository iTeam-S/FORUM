import Axios from 'axios';

const RouteAxios = Axios.create({
    baseURL: "https://forum-api.iteam-s.mg/api/v1" /*route v1 with endpoin '/login' && 'add_account' */
})

export {
    RouteAxios
}
