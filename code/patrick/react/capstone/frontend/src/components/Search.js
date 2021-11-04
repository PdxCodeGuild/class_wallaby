import Button from "@restart/ui/esm/Button";
import axios from "axios";
import { useState } from "react";
import { Col, Form, Row } from "react-bootstrap";
import { useHistory } from "react-router";
import SearchResults from "../pages/SearchResults";


function Search(props) {
    const [searchParams, setSearchParams] = useState("")
    const [searchData, setSearchData] = useState([])
    const history = useHistory();

    const SearchApi = (e) =>  {
        e.preventDefault();
         axios.get("http://localhost:8000/search/api/?q=", searchParams).then((res) => {
            console.log(res, ' search results');
            setSearchData(res.data)
    }).then((res)=> (res))
    history.push("/searchresults")


    }


    return ( 
        <Form onSubmit={SearchApi}>
          <Row className="align-items-center">
            <Col xs="auto">
              <Form.Label htmlFor="inlineFormInputName" visuallyHidden>
                Search
              </Form.Label>
              <Form.Control onChange={(e) => setSearchParams( e.target.value)} value={searchParams}  placeholder="Search" />
            </Col>
            <Col xs={"auto"}>
              <Button id="searchBtn" className="btn btn-primary" variant="primary" type="submit">
                Search
              </Button>
            </Col>
          </Row>
        </Form>
     );
}
export default Search;