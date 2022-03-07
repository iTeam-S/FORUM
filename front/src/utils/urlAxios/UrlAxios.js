import Axios from 'axios';

const RouteAxios = Axios.create({
    baseURL: "http://localhost:5000/api/v1" /*route v1 with endpoin '/login' && 'add_account' */
})

export {
    RouteAxios
}