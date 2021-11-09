import axios from "axios";
import React, { useContext } from "react";
import { useHistory } from "react-router-dom";
import AuthContext from "../API/context/AuthContext";

function LogOutBtn() {
  const {getLoggedIn} = useContext(AuthContext);
  const history = useHistory();

  async function logOut() {
    await axios.post(
      "http://localhost:8000/dj-rest-auth/logout/"
    );
    await getLoggedIn();
    history.push("/");
  }

  return <div  onClick={logOut}>Log out</div>;
}

export default LogOutBtn;