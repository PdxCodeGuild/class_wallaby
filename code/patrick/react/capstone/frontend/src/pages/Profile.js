import axios from 'axios';
import React, { createContext, useContext, useEffect, useState } from 'react';
import AuthContext from '../API/context/AuthContext';

const UserCreds = createContext();


function Profile() {
    const [usercreds, setUserCreds] = useState(undefined)
    console.log(usercreds)
    // useEffect(() => {
    //     getLoggedIn();
    //   }, [loggedIn]);
    async function creds() {
    const creds = {
        username: "patrick",
        first_name: "pat",
        last_name: "barry"
    }

    axios.get( "http://localhost:8000/dj-rest-auth/user/", creds).then((res) => {
          setUserCreds(res.data)
    })
}
    useEffect(() => {
        creds();
      }, []);
    
    return (  
        <div>profile</div>
    );
}

export default Profile;