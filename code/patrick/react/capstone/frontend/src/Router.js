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
  
 
  return (
    <BrowserRouter>
     <NavBar />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/federalregister" component={FederalRegister} />
        <Route exact path="/searchresults" component={SearchResults} />
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


// function Router() {
//   const { loggedIn } = useContext(AuthContext);
//   console.log(loggedIn)
//   return (
//     <BrowserRouter>
//       <NavBar />
//       <Switch>
//         <Route exact path="/">
//           <div>Home</div>
//         </Route>
//         {loggedIn === false && (
//           <>
//             <Route path="/register">
//               <Register />
//             </Route>
//             <Route path="/login">
//               <Login />
//             </Route>
//           </>
//         )}
//         {loggedIn === true && (
//           <>
//             <Route path="/customer">
//               <Profile />
//             </Route>
//           </>
//         )}
//       </Switch>
//     </BrowserRouter>
//   );
// }

// export default Router;