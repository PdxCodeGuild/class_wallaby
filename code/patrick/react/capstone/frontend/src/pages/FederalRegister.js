import React, { useState, useEffect, useContext } from "react";
import { Container, ListGroup, ListGroupItem } from "react-bootstrap";
import SnipBtn from "../components/SnipBtn";
import axios from "axios";
import "../css/CssClasses.css";
import AuthContext from "../API/context/AuthContext";


function FederalRegister() {
  const [snippets, setSnippets] = useState([]);
  const [requestInFlight, setRequestInFlight] = useState(false);
  const { loggedIn } = useContext(AuthContext);

  useEffect(() => {
    setRequestInFlight(true);
    axios
      .get("http://localhost:8000/feed/all/")
      .then((res) => {
        setSnippets(res.data);
        console.log(res.data);
      })
      .finally(() => setRequestInFlight(false));
  }, []);

 
  const spinner = (
    <div className="d-flex justify-content-center pt-5">
      <div className="spinner-border" role="status">
        <span className="sr-only"></span>
      </div>
    </div>
  );
  return requestInFlight ? spinner : 
  <Container >
  <ListGroup className="pt-2 ">
    {snippets.map((item) => (
      <ListGroupItem className="body ">
        <div key={item.id} >
          <a
            href={item.link}
            className="snippet list-group-item list-group-item-action mb-1" 
          >
            <div className=" ms-2 me-auto ">
              <div className=" fw-bold">{item.title}</div>
              <div>{item.pubDate}</div>
            </div>
          </a>
          {!loggedIn ? (
            <div></div>
          ) : (
          <SnipBtn id={item} className="btn" />
          )}
        </div>
      </ListGroupItem>
    ))}
  </ListGroup>
</Container>;
}
export default FederalRegister;
