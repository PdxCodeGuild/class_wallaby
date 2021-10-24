import axios from "axios";
import React, { useState, useEffect } from "react";
import { ListGroup, Badge } from "react-bootstrap";


function FederalRegister() {
  const [posts, setPosts] = useState([]);
  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/feed/all/`).then((res) => {
      const feeds = res.data;
      setPosts(feeds);
    });
  }, []);

  return (
    <ListGroup as="ol" numbered>
      {posts.map((item) => (
        <div key={item.id}>
          <a
            href={item.link}
            as="li"
            className="list-group-item list-group-item-action"
          >
            <div className="ms-2 me-auto">
              <div className="fw-bold">{item.title}</div>
            </div>
          </a>
          
        </div>
      ))}
    </ListGroup>
  );
}
export default FederalRegister;

