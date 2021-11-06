import axios from "axios";
import React, { useContext, useEffect, useState } from "react";
import {
  Card,
  Col,
  Form,
  Modal,
  Row,
  CardGroup,
  Image,
  Container,
} from "react-bootstrap";
import "../css/CssClasses.css";
import { useForm } from "react-hook-form";
import { CardBody } from "reactstrap";
import Button from "@restart/ui/esm/Button";
import SavedSnips from "../components/SavedSnips";
import AuthContext from "../API/context/AuthContext";

function Profile() {
  const { getLoggedIn } = useContext(AuthContext);
  const { register, handleSubmit, reset } = useForm();
  const [image, setImage] = useState(null);
  const [newImage, setNewImage] = useState(null);
  const [userID, setUserID] = useState("");
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  function ImageChange(e) {
    setNewImage(e.target.files[0]);
  }

  function Submit(e) {
    e.preventDefault();
    const form_data = new FormData();
    form_data.append("image", newImage);
    axios
      .patch("http://localhost:8000/imageupload/", form_data)
      .then((res) => {
        setImage(res.data.image);
        handleClose();
        getLoggedIn();
      })
      .catch((err) => console.log(err));
  }

  async function updateProfile(data) {
    console.log(data, " user id");
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
      <CardGroup className="mx-3 pt-3 ">
        <Card>
          <CardBody>
            <Row>
              <Col s={6} md={6}>
                <div className="text-center">
                  <Image
                    variant="top"
                    src={image}
                    alt="ima"
                    className="img-responsive center-block d-block mx-auto"
                    roundedCircle
                  />
                  <Button href="#" onClick={handleShow}>
                    Change Profile Image
                  </Button>
                </div>
              </Col>
              <Col s={6} md={6}>
                <Form.Group className="text-start">
                  <form onSubmit={handleSubmit(updateProfile)}>
                    <label>Email: </label>
                    <Form.Control {...register("email")} />
                    <label className="pt-2">Username: </label>
                    <Form.Control {...register("username")} />
                    <label className="pt-2">First name: </label>
                    <Form.Control {...register("first_name")} />
                    <label className="pt-2">Last name: </label>
                    <Form.Control
                      placeholder="last name"
                      {...register("last_name")}
                    />
                    <div className="pt-2">
                      <Button className="btn btn-primary" type="submit">
                        Update
                      </Button>
                    </div>
                  </form>
                </Form.Group>
              </Col>
            </Row>
          </CardBody>
        </Card>

        <Modal show={show} autoFocus="true" onHide={handleClose}>
          {" "}
          {/* modal to save new profile image */}
          <Modal.Header closeButton>
            <Modal.Title>Update Profile Image</Modal.Title>
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
            </Form.Group>
          </Modal.Body>
          <Modal.Footer>
            <Button
              className="btn btn-primary"
              variant="primary"
              onClick={Submit}
            >
              Save Changes
            </Button>
          </Modal.Footer>
        </Modal>
      </CardGroup>
      <SavedSnips />
    </Container>
  );
}
export default Profile;
