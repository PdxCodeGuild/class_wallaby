import axios from "axios";
import React, { createContext, useEffect, useState } from "react";

const AuthContext = createContext();

function AuthContextProvider(props) {
  const [loggedIn, setLoggedIn] = useState(undefined);
  console.log('auth function')
  async function getLoggedIn() {
    
    const loggedInRes = await axios.get(
      "http://localhost:8000/isauthorized/"
    ).then(res =>{
      console.log(res, 'auth response')
    setLoggedIn(res.data)
      })
      .catch(error =>{
        console.log(error)
      setLoggedIn(undefined);
      })
    
    ;
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