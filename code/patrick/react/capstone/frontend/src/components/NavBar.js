import { Navbar, NavbarBrand, Nav, Dropdown } from "react-bootstrap";
import "../css/CssClasses.css";
import Container from "react-bootstrap/Container";
import React, { useContext } from "react";

import AuthContext from "../API/context/AuthContext";
import LogOutBtn from "../authorization/LogOutBtn";
import Search from "./Search";
import Avatar from "react-avatar";
import { Link } from "react-router-dom";

function NavBar({ setSearchData }) {
  const { loggedIn } = useContext(AuthContext); // globally available login information for routing and avatar for navbar.
  const { avatarImg } = useContext(AuthContext);
  const {profileName} = useContext(AuthContext);
  

  return (
    <Navbar bg="light" expand="md">
      <Container>
        <NavbarBrand className="navItem" href="/">
          Info App
        </NavbarBrand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse>
          <Nav className="me-auto">
            <Nav.Link className="navItem" href="/federalregister">
              Federal Register
            </Nav.Link>
            {!loggedIn ? (
              <>
                <Nav.Link className="navItem" href="/login">
                  Login
                </Nav.Link>
                <Nav.Link className="navItem" href="/register">
                  Register
                </Nav.Link>
              </>
            ) : (
              <>
                
              </>
            )}
          </Nav>
          <div className="p-2">
          <Search setSearchData={setSearchData} />
          </div>
          {!loggedIn ? (
            <div></div>
          ) : (
            <Dropdown  >
              <div className="vr mx-3" />
              <Avatar src={avatarImg} className="avatarImage " size="50" />
                <Dropdown.Toggle className="btn btn-dark btn-outline-light mx-1"  id="dropdown-basic">
                 Welcome, {profileName} 
                </Dropdown.Toggle>

                <Dropdown.Menu>
                  <Dropdown.Item href="/profile">
                 
                  Profile
              
                  </Dropdown.Item>
                  <Dropdown.Item>
                  <LogOutBtn />
                  </Dropdown.Item>
                </Dropdown.Menu>
              </Dropdown>
          )}   
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavBar;
