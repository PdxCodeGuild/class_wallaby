import { Container, ListGroup, ListGroupItem } from "react-bootstrap";
import SnipBtn from "../components/SnipBtn";
import AuthContext from "../API/context/AuthContext";
import { useContext } from "react";


function SearchResults({searchData}) {
  const { loggedIn } = useContext(AuthContext);

return (
    <Container>
        <ListGroup>
    {searchData.map((item) => (
        <div key={item.id}>
      <ListGroupItem>
          <a href={item.link} className="list-group-item list-group-item-action">
            <div className="ms-2 me-auto">
              <div className="fw-bold">{item.title}</div>
              <div>{item.pubDate}</div>
            </div>
          </a>
          {!loggedIn ? (
            <div></div>
          ) : (
        <SnipBtn  id={item}  />
        )}
      </ListGroupItem>
        </div>
         ))}
    </ListGroup>
      </Container>
  );
}
export default SearchResults;
