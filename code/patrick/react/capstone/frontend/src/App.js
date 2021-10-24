import React from "react";
import './App.css';
import NavBar from './components/NavBar'
import Home from './pages/Home'
import FederalRegister from './pages/FederalRegister'
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";


export default function App() {
  return (
    <Router>
      <div>
        <NavBar />      
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route exact path="/federalregister">
            <FederalRegister />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}


// function Federalregister() {
//   return <FederalRegister />;
// }


