import Button from "@restart/ui/esm/Button";
import axios from "axios";
import { useState } from "react";
import { Col, Form, Row } from "react-bootstrap";
import { useHistory } from "react-router";


function Search({ setSearchData }) {
  const [searchParams, setSearchParams] = useState([]);
  const history = useHistory();

  const SearchApi = (e) => {
    e.preventDefault();
    axios.get("http://localhost:8000/search/api/?q="+searchParams).then((res) => {
      console.log(res, " search results");
      setSearchData(res.data);
    });
    history.push("/searchresults");
  };

  return (
    <Form onSubmit={SearchApi}>
      <Row >
        <Col xs="auto" className="ml-5">
          <Form.Label htmlFor="inlineFormInputName" visuallyHidden>
            Search
          </Form.Label>
          <Form.Control
            onChange={(e) => setSearchParams(e.target.value)}
            value={searchParams}
            placeholder="Search"
            
          />
        </Col>
        <Col  >
          <Button
            id="searchBtn"
            className="btn btn-outline-dark button"
            variant="primary"
            type="submit"
          >
            Search
          </Button>
        </Col>
      </Row>
    </Form>
  );
}
export default Search;
