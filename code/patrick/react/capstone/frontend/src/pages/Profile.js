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
        
    }
// feedsubs/pk which whole feeds user is subscribed to

    axios.get( "http://localhost:8000/dj-rest-auth/user/").then((res) => {
          setUserCreds(res.data)
          console.log(res)
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