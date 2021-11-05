import { Navbar, NavbarBrand, Nav } from "react-bootstrap";
import "../css/Navbar.css";
import Container from "react-bootstrap/Container";
import React, { useContext } from "react";

import AuthContext from "../API/context/AuthContext";
import LogOutBtn from "../authorization/LogOutBtn";
import Search from "./Search";
import Avatar from 'react-avatar';

function NavBar({ setSearchData }) {
  const { loggedIn } = useContext(AuthContext); // globally available login information for routing and avatar for navbar.
  const { avatarImg } = useContext(AuthContext);
  console.log(avatarImg)

  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <NavbarBrand className="navItem" href="/">Home</NavbarBrand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link className="navItem" href="/federalregister">Federal Register</Nav.Link>
            {!loggedIn ? (
              <>
                <Nav.Link className="navItem" href="/login">Login</Nav.Link>
                <Nav.Link className="navItem" href="/register">Register</Nav.Link>
              </>
            ) : (
              <>
                <Nav.Link className="navItem" href="/profile">Profile</Nav.Link>
                <LogOutBtn />
              </>
          )}
          </Nav>
          {!loggedIn ? (
            <div></div>
          ) : ( 
            <Avatar src={avatarImg} className="avatarImage" size="50"/>
          )}
            <Search setSearchData={setSearchData} />
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavBar;
