import React, { useContext, useState } from "react";
import axios from "axios";
import AuthContext from "../API/context/AuthContext";
import { useHistory } from "react-router";
import { Container, Form } from "react-bootstrap";
import "../css/CssClasses.css";

function Register() {
  const [username, setUserName] = useState("");
  const [email, setEmail] = useState("");
  const [password1, setPassword1] = useState("");
  const [password2, setPassword2] = useState("");
  const { getLoggedIn } = useContext(AuthContext);
  const history = useHistory();

  async function register(e) {
    e.preventDefault();
    const data1 = {
      username: username,
      email: email,
      password1: password1,
      password2: password2,
    };

    const res = await axios.post(
      "http://localhost:8000/dj-rest-auth/registration/",
      data1
    );
    const creds = {
      email: res.data.user.email,
      username: res.data.user.username,
      password: data1.password1,
    };
    await axios
      .post("http://localhost:8000/dj-rest-auth/login/", creds)
      .then((res) => {
        console.log(res);
      });
    await getLoggedIn();
    history.push("/");
  }
  return (
    <Container>
      <h1 className="title">Register a new account</h1>
      <form onSubmit={register}>
        <Form.Control
          type="username"
          placeholder="Username"
          onChange={(e) => setUserName(e.target.value)}
          value={username}
        />
        <Form.Control
          className="mt-2"
          type="email"
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
          value={email}
        />
        <Form.Control
          className="mt-2"
          type="password"
          placeholder="Password"
          onChange={(e) => setPassword1(e.target.value)}
          value={password1}
        />
        <Form.Control
          className="mt-2"
          type="password"
          placeholder="Verify your password"
          onChange={(e) => setPassword2(e.target.value)}
          value={password2}
        />
        <button class="button btn btn-outline-light mt-2" type="submit">
          Register
        </button>
      </form>
    </Container>
  );
}
export default Register;
