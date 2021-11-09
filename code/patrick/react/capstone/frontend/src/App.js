import React from 'react';
import Router from "./Router";
import axios from "axios";
import { AuthContextProvider } from "./API/context/AuthContext";

axios.defaults.withCredentials = true;

function App() {
  return(
    // Gifting router AuthContext
    <AuthContextProvider>  
      <Router />
    </AuthContextProvider>
  )
}

export default App

