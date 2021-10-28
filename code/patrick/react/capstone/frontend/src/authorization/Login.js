import Requests from "../API/Calls";
import React, { useState, useEffect } from "react";
import { Container, Col, } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";




export default function Login() {
  const {register, handleSubmit, formState: { errors } } = useForm(); 
  const [token, setToken] = useState([]);
  const onSubmit = (data) => {
  let creds = data
  axios.post("http://localhost:8000/dj-rest-auth/login/", creds,).then((res) => {
      // let cookie = res.data["key"]
      // document.cookie = `token: ${cookie}` 
      // console.log(res)
      console.log('loged in')
    setToken(res)
    ;})}
  
  
  
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
