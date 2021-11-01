import React, { useState, useEffect} from "react";
import { Container, ListGroup, ListGroupItem } from "react-bootstrap";
import SnipBtn from "../components/SnipBtn";
import Requests from '../API/Calls'
import axios from "axios";

function FederalRegister() {
  const [snippets, setSnippets] = useState([]);
  const [userID, setUserID] = useState("")
   
console.log(userID)

  useEffect(() => {

    axios.get("http://localhost:8000/dj-rest-auth/user/").then((res)=>{
      setUserID(res.data.pk)
  })
    axios.get("http://localhost:8000/federalregister")
    Requests.getAll().then((res) => {
      console.log(res.data)
      setSnippets(res.data);
      
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
          
          <SnipBtn id={snippets[item.id-1]} pk={userID}/>
        </div>
      </ListGroupItem>
         ))}
    </ListGroup>
      </Container>
  );
}
export default FederalRegister;
