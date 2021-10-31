import axios from "axios";
import React, { useEffect, useState } from "react";
import { Card, Col, Container, Form, Modal, Row } from "react-bootstrap";
import "./Profile.css";
import { useForm } from "react-hook-form";
import { CardBody } from "reactstrap";
import Button from "@restart/ui/esm/Button";

function Profile() {
  const { register, handleSubmit, reset } = useForm();
  const [image, setImage] = useState(null);
  const [newImage, setNewImage] = useState(null);
  const [userID, setUserID] = useState("");
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

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
        handleClose()
      })
      .catch((err) => console.log(err));
  };

  async function updateProfile(data) {
    console.log(data, " user id");
    // feedsubs/pk which whole feeds user is subscribed to
    await axios
      .patch("http://localhost:8000/edituser/" + userID, data)
      .then((res) => {
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
      <Row>
        <Col md={4}>
          <Card >
            <CardBody>
              <Card.Img variant="top" img idi="profileImage" src={image} alt="ima" />
              
            </CardBody>
          </Card>
        </Col>
      </Row>
      <Modal show={show} autoFocus="true" onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Modal heading</Modal.Title>
        </Modal.Header>
        <Modal.Body>
        <Form.Group className="mb-3">
                <form onSubmit={Submit}>
                  <p>
                    <input
                      type="file"
                      id="image"
                      accept="image/png, image/jpeg"
                      onChange={ImageChange}
                      required
                    />
                  </p>
                </form>
                  {/* <Button
                    value="Upload Photo"
                    className="btn btn-primary"
                    type="submit"
                    onChange={(e) => setNewImage( e.target.value)}
                  /> */}
              </Form.Group>


        </Modal.Body>
        <Modal.Footer>
       
          <Button className="btn btn-primary" variant="primary" onClick={Submit}>
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>
      <Form.Group className="mb-3" controlId="formBasicEmail">
      <Button variant="primary" onClick={handleShow}>
        Launch demo modal
      </Button>
        <form onSubmit={handleSubmit(updateProfile)}>
          <label>Email: </label>
          <input {...register("email")} />
          <label>Username: </label>
          <input {...register("username")} />
          <label>First name: </label>
          <input {...register("first_name")} />
          <label>Last name: </label>
          <input placeholder="last name" {...register("last_name")} />
          <input value="Update" className="btn btn-primary" type="submit" />
        </form>
      </Form.Group>
    </Container>
  );
}

export default Profile;
