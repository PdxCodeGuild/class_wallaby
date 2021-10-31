import axios from "axios";
import React, { useEffect, useState } from "react";
import { Container } from "react-bootstrap";
import "./Profile.css";
import { useForm } from "react-hook-form";
import SendIt from "../components/ImageApi";

function Profile() {
  const {  register, handleSubmit, reset } = useForm();
  const [profileImage, setProfileImage] = useState(undefined)

    // async function updateImage(data){
       
        
    //     console.log(data)
    //  await axios.post("http://localhost:8000/dj-rest-auth/user/")
    //     .then((result) => {
    //       console.log("Success:", result);
    //     })
    // }



  async function updateProfile(data) {
    console.log(data)
    // feedsubs/pk which whole feeds user is subscribed to
    await axios
      .patch("http://localhost:8000/dj-rest-auth/user/", data)
      .then((res) => {
        //   setUserName(res.data.username)
        //   setEmail(res.data.email)
        //   setFirstName(res.data.first_name)
        //   setLastName(res.data.last_name)
        console.log(res);
      });
  }
  useEffect(() => {
    axios.get("http://localhost:8000/dj-rest-auth/user/").then((res) => {
      setProfileImage(res.data.profile["image"]);
      console.log(res);
      setTimeout(() => {
        reset({
          first_name: res.data.first_name,
          last_name: res.data.last_name,
        });
      });
    }, 2000);
  }, [reset]);

  return (
    <Container>
        <SendIt />
        <img src={profileImage} alt="ima" />
      <form onSubmit={handleSubmit(updateProfile)}>
        <label>First name: </label>
        
        <input {...register("first_name")} />
        <label>Last name: </label>
        <input {...register("last_name")} />
        <input type="submit" />
      </form>
    </Container>
  );
}

export default Profile;
