import React, { useContext } from "react";
import { Container, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import AuthContext from "../API/context/AuthContext";
import { useHistory } from "react-router";
import "../css/CssClasses.css";

export default function Login() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  let history = useHistory();
  const { getLoggedIn } = useContext(AuthContext);

  async function onSubmit(data) {
    let creds = data;
    await axios
      .post("http://localhost:8000/dj-rest-auth/login/", creds)
      .then((res) => {
        console.log(res, "loged in");
      });
    await getLoggedIn();
    history.push("/");
  }

  return (
    <Container>
      <h1 className="title">Log in</h1>
      <form onSubmit={handleSubmit(onSubmit)}>
        <Form.Control
          className="mt-2"
          placeholder="username"
          {...register("username")}
        />
        <Form.Control
          className="mt-2"
          placeholder="email"
          {...register("email")}
        />
        <Form.Control
          className="mt-2"
          placeholder="password"
          {...register("password", { required: true })}
        />
        {errors.exampleRequired && <span>This field is required</span>}
        <button class="button btn btn-outline-light mt-2" type="submit">
          Register
        </button>
      </form>
    </Container>
  );
}
