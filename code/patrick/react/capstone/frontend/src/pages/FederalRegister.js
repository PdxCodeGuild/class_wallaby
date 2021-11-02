import React, { useState, useEffect} from "react";
import { Container, ListGroup, ListGroupItem } from "react-bootstrap";
import SnipBtn from "../components/SnipBtn";
import Requests from '../API/Calls'
import axios from "axios";

function FederalRegister() {
  const [snippets, setSnippets] = useState([]);
  
 


  useEffect(() => {
    axios.get("http://localhost:8000/feed/all/")
    Requests.getAll().then((res) => {  
      setSnippets(res.data);
      console.log(res.data)
    });
  }, []);

  // const userId = 1; // need logged in user

  // const snipSubs = (item) => {
  //   console.log(item)
  //   for (let i = 0; i < item.length; i++) {
  //     if (item[i] in userId) {
  //       alert("contains user");
  //     } else {
        
  //       alert("contains user");
  //     }
  //   }
  // };

  
  return (
    <Container>
        <ListGroup>
    {snippets.map((item) => (
      <ListGroupItem>
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
          
        </div>
        <SnipBtn  id={snippets[item.id-1]} pk={snippets[item.id.pubDate]} />
      </ListGroupItem>
         ))}
    </ListGroup>
      </Container>
  );
}
export default FederalRegister;
