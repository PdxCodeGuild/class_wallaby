import axios from "axios";
import React, { useEffect, useState } from "react";
import { Container } from "react-bootstrap";
import "./Profile.css";
import { useForm } from "react-hook-form";

function Profile() {
  const { register, handleSubmit, reset } = useForm();
  const [image, setImage] = useState(null);
  const [newImage, setNewImage] = useState(null);
  const [userID, setUserID] = useState("");
  // const [userName, setUserName] = useState("")

  const ImageChange = (e) => {
    setNewImage(e.target.files[0]);
  };

  const Submit = (e) => {
    e.preventDefault();
    const form_data = new FormData();
    form_data.append("image", newImage);

    axios
      .patch("http://localhost:8000/imageupload/", form_data)
      .then((res) => {
        setImage(res.data.image);
      })
      .catch((err) => console.log(err));
  };

  async function updateProfile(data) {
    console.log(data, ' user id');
    // feedsubs/pk which whole feeds user is subscribed to
    await axios
      .patch("http://localhost:8000/edituser/" + userID, data)
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
      setUserID(res.data.pk);
      setImage(res.data.profile["image"]);
      
     
      setTimeout(() => {
        reset({
          username: res.data.username,
          email: res.data.email,
          first_name: res.data.first_name,
          last_name: res.data.last_name,
        });
      });
    }, 2000);
  }, [reset]);

  return (
    <Container>
      <div>
        <form onSubmit={Submit}>
          {/* <p>
            <input type="text" placeholder='Title' id='title' value={this.state.title} onChange={this.handleChange} required/>
          </p>
          <p>
            <input type="text" placeholder='Content' id='content' value={this.state.content} onChange={this.handleChange} required/>

          </p> */}
          <p>
            <input
              type="file"
              id="image"
              accept="image/png, image/jpeg"
              onChange={ImageChange}
              required
            />
          </p>
          <input type="submit" />
        </form>
      </div>
      <img src={image} alt="ima" />
      <form onSubmit={handleSubmit(updateProfile)}>
        <label>Email: </label>
        <input {...register("email")} />
        <label>Username: </label>
        <input {...register("username")} />
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
