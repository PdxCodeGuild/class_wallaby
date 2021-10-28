import React from 'react';
import axios from "axios";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import Home from "./pages/Home";
import Login from "./authorization/Login";
import FederalRegister from "./pages/FederalRegister";
import Register from './authorization/Register';




export default function Router() {
  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/federalregister" component={FederalRegister} />
        <Route exact path="/register" component={Register} />
      </Switch>
    </BrowserRouter>
  );
}