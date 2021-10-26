import { Navbar, Nav, NavDropdown } from "react-bootstrap";
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import React, { useState, useEffect, Fragment } from "react";
import { Link } from "react-router-dom";

  const NavBar = () => {
  const [isAuth, setIsAuth] = useState(false);

  useEffect(() => {
    if (localStorage.getItem("token") !== null) {
      setIsAuth(true);
    }
  }, []);

  
    return (
      <Navbar bg="light" expand="lg">
        <Container>
          <Navbar.Brand href="/">Home Page</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="/">Link</Nav.Link>
              <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                <NavDropdown.Item href="/federalregister">
                  Federal Register
                </NavDropdown.Item>
                <NavDropdown.Item href="/about">Action</NavDropdown.Item>
                {isAuth === true ? (
              <Fragment>
                {" "}
                <NavDropdown.Item>
                  <Link to="/profile">Dashboard</Link>
                </NavDropdown.Item>
                
                <NavDropdown.Item>
                <Link to="/logout">Logout</Link>
                </NavDropdown.Item>
              </Fragment>
            ) : (
              <Fragment>
                {" "}
                <NavDropdown.Item>
                  <Link to="/login">Login</Link>
                </NavDropdown.Item>
                <NavDropdown.Item>
                  <Link to="/signup">Signup</Link>
                </NavDropdown.Item>
              </Fragment>
            )}
               
              </NavDropdown>
            </Nav>
          </Navbar.Collapse>
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
