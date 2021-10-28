// import axios from "axios";
// import React, { createContext, useEffect, useState } from "react";

// const AuthContext = createContext();

// function AuthContextProvider(props) {
//   const [loggedIn, setLoggedIn] = useState(undefined);

//   async function getLoggedIn() {
//     // const loggedInRes = await axios.get("http://localhost:5000/auth/loggedIn");
//     const loggedInRes = await axios.get("http://localhost:8000/isauthorized/")
    
//     setLoggedIn(loggedInRes.data);
//   }

//   useEffect(() => {
//     getLoggedIn();
//   }, []);

//   return (
//     <AuthContext.Provider value={{ loggedIn, getLoggedIn }}>
//       {props.children}
//     </AuthContext.Provider>
//   );
// }

// export default AuthContext;
// export { AuthContextProvider };


import axios from "axios";
import React, { createContext, useEffect, useState } from "react";

const AuthContext = createContext();

function AuthContextProvider(props) {
  const [loggedIn, setLoggedIn] = useState(undefined);
  console.log('auth function')
  async function getLoggedIn() {
    
    const loggedInRes = await axios.get(
      "http://localhost:8000/isauthorized/"
    );
    console.log(loggedInRes)
    setLoggedIn(loggedInRes.data);
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