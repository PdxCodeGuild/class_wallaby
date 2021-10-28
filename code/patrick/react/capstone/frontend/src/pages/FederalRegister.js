import React, { useState, useEffect} from "react";
import { ListGroup } from "react-bootstrap";
import SnipBtn from "../components/SnipBtn";
import Requests from '../API/Calls'

function FederalRegister() {

  const [snippets, setSnippets] = useState([]);

  useEffect(() => {
    Requests.getAll().then((res) => {
      setSnippets(res.data);
      
    });
  }, []);

  const userId = 1; // need logged in user

  const snipSubs = (item) => {
    console.log(item)
    for (let i = 0; i < item.length; i++) {
      if (item[i] in userId) {
        alert("contains user");
      } else {
        //patch the user into the subscriber section using an axiox patch request.
        alert("contains user");
      }
    }
  };

  
  return (
    <ListGroup as="ol" numbered>
      {snippets.map((item) => (
        <div key={item.id}>
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
          <div onClick={() => snipSubs(item)}>
            <SnipBtn />   /Need to be able to render each view and assign a add/added depending if user has added them or not already
          </div>
        </div>
      ))}
    </ListGroup>
  );
}
export default FederalRegister;
