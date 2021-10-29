import axios from 'axios';
import React, { useEffect, useState } from 'react';


function Profile() {
    
    const [username, setUserName] = useState("");
    const [email, setEmail] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [profileImage, setProfileImage] = useState("");
    

    
    
    
    async function profileDetail() {
    
    
// feedsubs/pk which whole feeds user is subscribed to

    await axios.get( "http://localhost:8000/dj-rest-auth/user/").then((res) => {
          setUserName(res.data.username)
          setEmail(res.data.email)
          setFirstName(res.data.first_name)
          setLastName(res.data.last_name)
          setProfileImage(res.data.profile['image'])
    })
}
    useEffect(() => {
        profileDetail();
      }, []);
    
    return (  
        <div>
        <h1>Register a new account</h1>
        <form onSubmit={profileDetail}>
        <img src={profileImage} alt="profile"/>
        <input
            type="password"
            placeholder="Verify your password"
            onChange={(e) => setProfileImage(e.target.value)}
            value={profileImage}
          />
        <input
            type="username"
            placeholder="Username"
            onChange={(e) => setUserName( e.target.value)}
            value={username}
          />
          <input
            type="email"
            placeholder="Email"
            onChange={(e) => setEmail(e.target.value)}
            value={email}
          />
          <input
            type="first_name"
            placeholder="Password"
            onChange={(e) => setFirstName(e.target.value)}
            value={firstName}
          />
          <input
            type="password"
            placeholder="Verify your password"
            onChange={(e) => setLastName(e.target.value)}
            value={lastName}
          />
          <button type="submit">Register</button>
        </form>
      </div>
    );
}

export default Profile;