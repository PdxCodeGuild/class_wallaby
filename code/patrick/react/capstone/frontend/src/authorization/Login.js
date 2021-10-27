import Requests from "../API/Calls";
import React, { useState, useEffect } from "react";
import { Container, Col, } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import { useCookies } from 'react-cookie';


export default function UserLoginForm() {
  const {register, handleSubmit, formState: { errors } } = useForm(); 
  const [token, setToken] = useState([]);
  const onSubmit = (data) => {
  let creds = data
  axios.post("http://127.0.0.1:8000/api-token/", creds).then((res) => {
    
      let cookie = res.data['token']
      document.cookie = `token: ${cookie}` 
    setToken(res)
    ;})}

  
  console.log(document.cookie)
  return (
    <Container>
      <Col>
        <form onSubmit={handleSubmit(onSubmit)}>
          <input defaultValue="test" {...register("username")} />
          <input {...register("password", { required: true })} />
          {errors.exampleRequired && <span>This field is required</span>}
          <input type="submit" />
        </form>
      </Col>
    </Container>
  );
}
