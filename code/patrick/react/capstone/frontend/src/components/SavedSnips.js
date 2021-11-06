import axios from "axios";
import React, { useEffect, useState } from "react";
import { Container, ListGroup, ListGroupItem } from "react-bootstrap";
import SavedBtn from "./SavedBtn";


function SavedSnips() { // 
  const [requestInFlight, setRequestInFlight] = useState(false);
  const [snippets, setSnippets] = useState([]);

  useEffect(() => {
    setRequestInFlight(true);
    axios
      .get("http://localhost:8000/savedsnips/")
      .then((res) => {
        setSnippets(res.data);
      })
      .finally(() => setRequestInFlight(false)); 
  }, []);

  function deleteUser(id) {
    setSnippets(snippets.filter((item) => item.id !== id));
  }

  const isLoaded = (
    <Container>
      <ListGroup className="mx-2 pt-3 rounded">
        
        {snippets.map((item) => (
            <div key={item.id}>
          <ListGroupItem>
              <a
                href={item.link}
                as="li"
                className="list-group-item list-group-item-action"
              >
                <div className="ms-2 me-auto">
                  <div className="fw-bold">{item.title}</div>
                  <div>{item.pubDate}</div>
                </div>
              </a>
            <div onClick={() => deleteUser(item.id)}> {/* bubbler to remove snippet from SavedSnips by filtering */}
              {" "}
              <SavedBtn id={item} />
            </div>
          </ListGroupItem>
            </div>
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

export default SavedSnips;
