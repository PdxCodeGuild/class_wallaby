import React, { useContext } from "react";
import { Container, Col, } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import AuthContext from "../API/context/AuthContext";
import { useHistory } from "react-router";



export default function Login() {
  const {register, handleSubmit, formState: { errors } } = useForm(); 
  let history = useHistory()
  const { getLoggedIn } = useContext(AuthContext);
  
 async function onSubmit(data) {
  let creds = data
  await axios.post("http://localhost:8000/dj-rest-auth/login/", creds,).then((res) => {
      console.log(res, 'loged in')
      ;})
      await getLoggedIn()
      history.push("/")
    
    }
  
  return (
    <Container>
      <Col>
        <form onSubmit={handleSubmit(onSubmit)}>
          <input  {...register("username")} />
          <input  {...register("email")} />
          <input {...register("password", { required: true })} />
          {errors.exampleRequired && <span>This field is required</span>}
          <input type="submit" />
        </form>
      </Col>
    </Container>
  );
}
