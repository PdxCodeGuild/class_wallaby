import React, { useState, useEffect } from "react";
import { Container, ListGroup, ListGroupItem } from "react-bootstrap";
import SnipBtn from "../components/SnipBtn";
import axios from "axios";


function FederalRegister() {
  const [snippets, setSnippets] = useState([]);
  const [requestInFlight, setRequestInFlight] = useState(false);

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

  const isLoaded = (
    <Container>
      <ListGroup>
        {snippets.map((item) => (
          <ListGroupItem>
            <div key={item.id}>
              <a
                href={item.link}
                className="list-group-item list-group-item-action"
              >
                <div className="ms-2 me-auto">
                  <div className="fw-bold">{item.title}</div>
                  <div>{item.pubDate}</div>
                </div>
              </a>
              <SnipBtn id={item} />
            </div>
          </ListGroupItem>
        ))}
      </ListGroup>
    </Container>
  );
  const spinner = (
    <div className="d-flex justify-content-center pt-5">
      <div className="spinner-border" role="status">
        <span className="sr-only"></span>
      </div>
    </div>
  );
  return requestInFlight ? spinner : isLoaded;
}
export default FederalRegister;
