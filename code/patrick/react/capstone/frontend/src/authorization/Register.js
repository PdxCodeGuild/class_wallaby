import React, { useState } from 'react';
import { useForm } from "react-hook-form";
import { Container, Col } from "react-bootstrap";
import axios from 'axios'




function Register() {
    const [username, setUserName] = useState("");
    const [email, setEmail] = useState("");
    const [password1, setPassword1] = useState("");
    const [password2, setPassword2] = useState("");
    
  
    // const { getLoggedIn } = useContext(AuthContext);
    // const history = useHistory();
  
  async function register(e) {
      e.preventDefault();
      const data1 = {
          
          username: username,
          email: email, 
          password1: password1,
          password2: password2
      }
        
      await axios.post( "http://localhost:8000/dj-rest-auth/registration/", data1).then((res) => {
          console.log(res)
    })
        

        // await getLoggedIn();
        // history.push("/");
     
    }
  
    return (
      <div>
        <h1>Register a new account</h1>
        <form onSubmit={register}>
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
            type="password"
            placeholder="Password"
            onChange={(e) => setPassword1(e.target.value)}
            value={password1}
          />
          <input
            type="password"
            placeholder="Verify your password"
            onChange={(e) => setPassword2(e.target.value)}
            value={password2}
          />
          <button type="submit">Register</button>
        </form>
      </div>
    );
  }
  
  export default Register;