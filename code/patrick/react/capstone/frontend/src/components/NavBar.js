import React from 'react';
import {Navbar, Nav, NavDropdown} from 'react-bootstrap';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';



const NavBar = () => {
    return (
        <Navbar bg="light" expand="lg">
        <Container>
          <Navbar.Brand href="/">Home Page</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              
              <Nav.Link href="/">Link</Nav.Link>
              <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                <NavDropdown.Item href="/federalregister">Federal Register</NavDropdown.Item>
                <NavDropdown.Item href="/about">Action</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
              </NavDropdown>
            </Nav>
          </Navbar.Collapse>
          <Form>
            <Row className="align-items-center">
              <Col xs="auto" >
                <Form.Label htmlFor="inlineFormInputName" visuallyHidden>
                Search
                </Form.Label>
                <Form.Control id="inlineFormInputName" placeholder="Search" />
              </Col>
              <Col xs={"auto"} >
                <Button id="searchBtn" variant="primary" type="submit">Search</Button>
              </Col>
            </Row>
          </Form>
        </Container>
        </Navbar>  
    )
}
 
export default NavBar;