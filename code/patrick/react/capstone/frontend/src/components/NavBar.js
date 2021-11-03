import { Navbar } from "react-bootstrap";
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import React, { Fragment, useContext } from "react";
import { Link } from "react-router-dom";
import AuthContext from "../API/context/AuthContext";
import LogOutBtn from "../authorization/LogOutBtn";



function NavBar() {
  const {loggedIn} = useContext(AuthContext);
  console.log(loggedIn, "navbar");

  return (
    <Navbar bg="light" expand="lg">
      <Container>
          <Link to="/">Home</Link>
          <Link to="/federalregister">Federal Register</Link>
          {!loggedIn ? (
           <>
           <Link to="/login">Login</Link>
           <Link to="/register">Signup</Link>
         </>
          ) :  (
            <>
              <Link to="/profile">Profile</Link>
              
           <LogOutBtn />
          </>
          )}
        <Form>
          <Row className="align-items-center">
            <Col xs="auto">
              <Form.Label htmlFor="inlineFormInputName" visuallyHidden>
                Search
              </Form.Label>
              <Form.Control id="inlineFormInputName" placeholder="Search" />
            </Col>
            <Col xs={"auto"}>
              <Button id="searchBtn" variant="primary" type="submit">
                Search
              </Button>
            </Col>
          </Row>
        </Form>
      </Container>
    </Navbar>
  );
};

export default NavBar;
