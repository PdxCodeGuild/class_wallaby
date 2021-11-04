import { Navbar } from "react-bootstrap";
import Container from "react-bootstrap/Container";
import React, { useContext } from "react";
import { Link } from "react-router-dom";
import AuthContext from "../API/context/AuthContext";
import LogOutBtn from "../authorization/LogOutBtn";
import Search from "./Search";

function NavBar({setSearchData}) {
  const {loggedIn} = useContext(AuthContext);

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
        <Search setSearchData={setSearchData}/>
      </Container>
    </Navbar>
  );
};

export default NavBar;
