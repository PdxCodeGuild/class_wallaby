import Button from "@restart/ui/esm/Button";
import axios from "axios";
import React, { useState } from "react";
import { Spinner } from "react-bootstrap";

export default function SavedBtn(id, updatePageState) {
  const [requestInFlight, setRequestInFlight] = useState(false);
  const [snipDetail, setSnipDetail] = useState(id.id["subscriber"]);
  const [userID, setUserID] = useState(parseInt(localStorage["UserID"]));

  async function UpdateSubs(snipDetail) {
    const data = {
      subscriber: snipDetail,
    };
    console.log(data, " request details sent");
    setRequestInFlight(true);
    return axios
      .patch(`http://localhost:8000/snipsubs/${id.id.id}`, data)
      .then((res) => {
        console.log(res.data.subscriber, " return patch request");
        setSnipDetail(snipDetail);
      })
      .finally(() => setRequestInFlight(false));
  }

  function toRemove(e) {
    let index = snipDetail.indexOf(userID);
    snipDetail.splice(index, 1);
    UpdateSubs(snipDetail);
  }

  const b = (
    <div>
      <button className="btn btn-danger" onClick={toRemove}>
        Delete
      </button>
    </div>
  );
  const spinner = (
    <Button variant="primary" disabled>
      <Spinner
        as="span"
        animation="border"
        size="sm"
        role="status"
        aria-hidden="true"
      />
      <span className="visually-hidden">Loading...</span>
    </Button>
  );
  return requestInFlight ? spinner : b;
}
