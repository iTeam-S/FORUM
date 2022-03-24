import { Route,Redirect } from 'react-router-dom'
import { LoginService } from 'utils/service/LoginService';

//header, footer, navbar
import AdminNavbar from "components/Navbars/AdminNavbar.js";
import Sidebar from "components/Sidebar/Sidebar.js";
import HeaderStats from "components/Headers/HeaderStats.js";
import FooterAdmin from "components/Footers/FooterAdmin.js";

export default function EntrepriseRoute({children, ...rest}){
    return(
        <>   
            <Sidebar />
            <div className="relative md:ml-64 bg-blueGray-100">
            <AdminNavbar />
            {/* Header */}
            <HeaderStats />
            <div className="px-4 md:px-10 mx-auto w-full -m-24">
                <Route {...rest} render = {() => {
                    return LoginService.getCurrentCompte().token !== null
                    ? children
                    : <Redirect to='/error' />
            }} />
            <FooterAdmin />
            </div>
        </div>
       </>
    )
}