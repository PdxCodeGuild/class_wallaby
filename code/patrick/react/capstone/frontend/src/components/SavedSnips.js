import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { Container, ListGroup, ListGroupItem } from 'react-bootstrap';
import SavedBtn from './SavedBtn';

function SavedSnips() {
    const [requestInFlight, setRequestInFlight] = useState(false);   
    const [snippets, setSnippets] = useState([])
 
    
    useEffect(() => {
        setRequestInFlight(true)
        axios.get("http://localhost:8000/savedsnips/")
        .then((res) => {  
          setSnippets(res.data);
          console.log(res.data)
        }).finally(() => setRequestInFlight(false))
      }, []);
    
      const deleteUser = id => setSnippets(snippets.filter(item => item.id !== id));
      console.log(deleteUser, " delete user")

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
         <div onClick={() => deleteUser(item.id)}> {/* bubler to remove snippet from   */}
        <SavedBtn id={item}  />
          </div>
      </ListGroupItem>
         ))}
    </ListGroup>
      </Container>
    );
}

export default SavedSnips;