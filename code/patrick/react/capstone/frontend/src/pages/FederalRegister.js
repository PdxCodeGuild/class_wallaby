import axios from "axios";
import React, { useState, useEffect } from "react";
import { ListGroup } from "react-bootstrap";


function FederalRegister() {
  const [snippets, setSnippets] = useState([]);
  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/feed/all/`).then((res) => {
      setSnippets(res.data);
    });
  }, []);

 const AddUserToSnippet = (item) => {
   console.log(item)
 }

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
          <button type='submit' onClick={AddUserToSnippet(item.id)} className="btn btn-primary">Add Snippet</button>
          
        </div>
      ))}
    </ListGroup>
  );
}
export default FederalRegister;




 