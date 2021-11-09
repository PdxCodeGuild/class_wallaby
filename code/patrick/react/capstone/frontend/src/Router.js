import React, { useContext, useState } from 'react';
import { BrowserRouter, Switch, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import Home from "./pages/Home";
import Login from "./authorization/Login";
import FederalRegister from "./pages/FederalRegister";
import Register from './authorization/Register';
import AuthContext from './API/context/AuthContext';
import Profile from './pages/Profile';
import SearchResults from './pages/SearchResults';


export default function Router() {
  const {loggedIn} = useContext(AuthContext);
  const [searchData, setSearchData] = useState([])

  return (
    <BrowserRouter>
     <NavBar setSearchData={setSearchData}/>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/federalregister" component={FederalRegister} />
        <Route  exact path="/searchresults" >
          <SearchResults searchData={searchData} />
        </Route>
        {! loggedIn ? (
          <Route>
          <Route exact path="/login" component={Login} />
          <Route exact path="/register" component={Register} />
          </Route>
          ) : (
            <Route>
          <Route exact path="/profile" component={Profile} />
          </Route>
        )}
      </Switch>
    </BrowserRouter>
  );
}

