import axios from "axios";
import React, { createContext, useEffect, useState } from "react";

const AuthContext = createContext();

function AuthContextProvider(props) {
  const [loggedIn, setLoggedIn] = useState(undefined);
  

  console.log('auth function')

  
  async function getLoggedIn() {
    
     await axios.get(
      "http://localhost:8000/dj-rest-auth/user/"
    ).then(res =>{
      console.log(res.data.pk)
      if (res.status===200){
        localStorage.setItem("UserID", res.data.pk)
        setLoggedIn(true);
      }
    })
    .catch(error =>{
        console.log('Not Authorized')
        console.log(error)
      setLoggedIn(undefined);
      })
  }
  useEffect(() => {
    getLoggedIn();
    
  }, []);

  return (
    <AuthContext.Provider value={{ loggedIn, getLoggedIn }}>
      {props.children}
    </AuthContext.Provider>
  );
}

export default AuthContext;
export { AuthContextProvider };