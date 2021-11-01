import React, { useState, useEffect} from "react";
import { Container, ListGroup, ListGroupItem } from "react-bootstrap";
import SnipBtn from "../components/SnipBtn";
import Requests from '../API/Calls'
import axios from "axios";

function FederalRegister() {
  const [saved, setSaved] = useState([])
  const [snipbtn, setSnipBtn] = React.useState("add")
  const toAdd = () => setSnipBtn("add")
  const toRemove = () => setSnipBtn("remove")
  const [snippets, setSnippets] = useState([]);

  // console.log(length.snippets[2])

  async function getSnips() {
    await axios.get("http://localhost:8000/feed/all/")
    .then(res =>{
      console.log(res)
    })
  }

  useEffect(() => {
    axios.get("http://localhost:8000/federalregister")
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
        
        alert("contains user");
      }
    }
  };

  
  return (
    <Container>
        <ListGroup as="ol" numbered>
      <ListGroupItem>
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
          
          <SnipBtn id={snippets[item.id]} />
        </div>
         ))}
      </ListGroupItem>
    </ListGroup>
      </Container>
  );
}
export default FederalRegister;
