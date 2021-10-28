


// function LogOutBtn() {
//     let history = useHistory()
//     const { getLoggedIn } = useContext(AuthContext);

//     async function logOut1() {
//         await axios.post("http://localhost:8000/dj-rest-auth/logout/").then((res) => {
//         console.log(res.data)    
//         getLoggedIn(res.data);
//     })
//         history.push("/")
//     } 
    
//     return (  
//         <button onClick={logOut1}>Log out</button>
//     );
// }

// export default LogOutBtn; 

import axios from "axios";
import React, { useContext } from "react";
import { useHistory } from "react-router-dom";
import AuthContext from "../API/context/AuthContext";

function LogOutBtn() {
  const { getLoggedIn } = useContext(AuthContext);
  const history = useHistory();

  async function logOut() {
    await axios.post(
      "http://localhost:8000/dj-rest-auth/logout/"
    );
    await getLoggedIn();
    history.push("/");
  }

  return <button onClick={logOut}>Log out</button>;
}

export default LogOutBtn;