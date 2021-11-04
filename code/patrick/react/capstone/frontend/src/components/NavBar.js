import { Navbar } from "react-bootstrap";
import Container from "react-bootstrap/Container";
import React, { Fragment, useContext, useState } from "react";
import { Link } from "react-router-dom";
import AuthContext from "../API/context/AuthContext";
import LogOutBtn from "../authorization/LogOutBtn";
import Search from "./Search";



function NavBar() {
  const {loggedIn} = useContext(AuthContext);
  const [searchData, setSearchData] = useState([])
  console.log(searchData, " navbar searchdata")

  function handleChange(newValue){
    setSearchData(newValue)
  }

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
        <Search searchData={searchData} onChange={handleChange}/>
      </Container>
    </Navbar>
  );
};

export default NavBar;
