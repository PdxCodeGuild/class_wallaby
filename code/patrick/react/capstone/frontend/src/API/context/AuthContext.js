import axios from "axios";
import React, { createContext, useEffect, useState } from "react";

const AuthContext = createContext(); // set context for conditional routing, logged-in=true.

function AuthContextProvider(props) {
  const [loggedIn, setLoggedIn] = useState(undefined);
  const [avatarImg, setAvatarImage] = useState(undefined);
  const [profileName, setUserName] = useState(undefined);

  async function getLoggedIn() {
    await axios
      .get("http://localhost:8000/dj-rest-auth/user/") // endpoint to retrieve user details
      .then((res) => {
        if (res.status === 200) {
          localStorage.setItem("UserID", res.data.pk); // set user pk to local storage.
          setLoggedIn(true);
          setAvatarImage(res.data.profile["image"])
          setUserName(res.data.username)
        } else if (res.status === 401) {
          axios
            .post("http://localhost:8000/dj-rest-auth/token/refresh/") // request returns new token upon auth
            .then((res) => console.log(res, "refresh request"));
        }
      })
      .catch((error) => {
        axios
          .post("http://localhost:8000/dj-rest-auth/token/refresh/") // ensure refresh will take place
          .then((res) => console.log(res, "refresh request"));
        console.log(error);
        setLoggedIn(undefined);
      });
  }
  useEffect(() => {
    getLoggedIn();
  }, []);

  return (
    <AuthContext.Provider value={{ loggedIn, getLoggedIn, avatarImg, profileName }}>
      {props.children}
    </AuthContext.Provider>
  );
}

export default AuthContext;
export { AuthContextProvider };
