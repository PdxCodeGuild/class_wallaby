import { Container, ListGroup, ListGroupItem } from "react-bootstrap";
import SnipBtn from "../components/SnipBtn";


function SearchResults({searchData}) {

return (
    <Container>
        <ListGroup>
    {searchData.map((item) => (
      <ListGroupItem>
        <div key={item.id}>
          <a href={item.link} className="list-group-item list-group-item-action">
            <div className="ms-2 me-auto">
              <div className="fw-bold">{item.title}</div>
              <div>{item.pubDate}</div>
            </div>
          </a>
        <SnipBtn  id={item}  />
        </div>
      </ListGroupItem>
         ))}
    </ListGroup>
      </Container>
  );
}
export default SearchResults;
