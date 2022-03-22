import Axios from 'axios';

const uRI = "https://forum-api.iteam-s.mg/api/v1"

const RouteAxios = Axios.create({
    baseURL: uRI /*route v1 with endpoin '/login' && 'add_account' */
})

export {
    RouteAxios, uRI
}
