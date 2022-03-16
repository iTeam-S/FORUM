import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";

import "@fortawesome/fontawesome-free/css/all.min.css";
import "assets/styles/tailwind.css";

//contexte
import { CompteContextProvider } from "utils/contexte/CompteContext";

// private
import AdminRoute from "views/private/AdminRoute";
import EntrepriseRoute from "views/private/EntrepriseRoute";

// layouts
import CardEditProfile from "components/Cards/CardEditProfile";
import TablesEntreprises from "views/admin/TablesEntreprises.js";


// views without 
import Index from "views/Index.js";
import Erreur from "views/Erreur.js";

//views admin
import AddEntreprise from "views/admin/AddEntreprise.js";
import AddFicheMetier from "views/admin/AddFicheMetier";

//views entreprise
import ProfilEntreprise from "views/admin-entreprise/ProfilEntreprise.js";
import OtherProfilEntreprise from 'views/admin/OtherProfilEntreprise.js'
import Statistiques from "views/admin-entreprise/Statistiques.js"
import AllContenu from "views/admin-entreprise/AllContenu.js";
import AddContenu from "views/admin-entreprise/AddContenu.js";
import AllFicheMetier from "views/admin/AllFicheMetier";
import CardEditContenu from "components/Cards/CardEditContenu";
import CardEditFiche from "components/Cards/CardEditFiche";


ReactDOM.render(
      <CompteContextProvider>
        <BrowserRouter>
          <Switch>
            <Route path="/" exact component={Index} />
            <Route path="/error" exact component={Erreur} />
            
            {/* add routes with layouts */}
            {/*entreprise route */}
            <EntrepriseRoute path="/adminEntreprise/Statistiques" exact>
              <Statistiques />
            </EntrepriseRoute>
            <EntrepriseRoute path="/adminEntreprise/AllContenu" exact >
              <AllContenu />
            </EntrepriseRoute>
            <EntrepriseRoute path="/adminEntreprise/AddContenu" exact >
              <AddContenu />
            </EntrepriseRoute>
            <EntrepriseRoute path="/adminEntreprise/ProfilEntreprise" exact>
              <ProfilEntreprise />
            </EntrepriseRoute>
            <EntrepriseRoute path="/adminEntreprise/CardEditProfile" exact >
              <CardEditProfile />
            </EntrepriseRoute>
            <EntrepriseRoute path="/adminEntreprise/CardEditContenu/:id" exact >
              <CardEditContenu />
            </EntrepriseRoute>

            {/*admin route */}
              <AdminRoute exact path="/admin/TablesEntreprises">
                <TablesEntreprises /> 
              </AdminRoute>
              <AdminRoute exact path="/admin/AllFicheMetier">
                <AllFicheMetier />
              </AdminRoute>
              <AdminRoute exact path="/adminEntreprise/ProfilEntreprise">
                <ProfilEntreprise /> 
              </AdminRoute>
              <AdminRoute exact path="/admin/profilDe/:id">
                <OtherProfilEntreprise />
              </AdminRoute>
              <AdminRoute exact path="/admin/CardEditFiche/:id">
                <CardEditFiche />
              </AdminRoute>
              <AdminRoute exact path="/admin/AddEntreprise">
                <AddEntreprise /> 
              </AdminRoute>
              <AdminRoute exact path="/admin/AddFicheMetier">
                <AddFicheMetier /> 
              </AdminRoute>
            
            {/* add redirect for first page */}
            <Redirect from="*" to="/error" />
          </Switch>
        </BrowserRouter>
      </CompteContextProvider>,
  document.getElementById("root")
);
