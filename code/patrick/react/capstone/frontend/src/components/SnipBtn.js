import Button from "@restart/ui/esm/Button";
import axios from "axios";
import React, { useState } from "react";
import { Spinner } from "react-bootstrap";

export default function SnipBtn(id) {
  const [snipDetail, setSnipDetail] = useState(id.id["subscriber"]);
  const [userID, setUserID] = useState(parseInt(localStorage["UserID"]));
  const [requestInFlight, setRequestInFlight] = useState(false);

  async function UpdateSubs(snipDetail) {
    const data = {
      subscriber: snipDetail,
    };
    console.log(data, " request details sent");
    setRequestInFlight(true);
    return axios
      .patch(`http://localhost:8000/snipsubs/${id.id["id"]}`, data)
      .then((res) => {
        console.log(res.data.subscriber, " return patch request");
        setSnipDetail(snipDetail);
      })
      .finally(() => setRequestInFlight(false));
  }

  function toAdd() {
    UpdateSubs([...snipDetail, userID]);
  }

  function toRemove() {
    let index = snipDetail.indexOf(userID);
    snipDetail.splice(index, 1);

    UpdateSubs(snipDetail);
    
  }

  const b = (
    <div>
      {snipDetail.includes(userID) ? (
        <button className="btn btn-success" onClick={toRemove}>
          Added
        </button>
      ) : (
        <button className="btn btn-primary" onClick={toAdd}>
          Add
        </button>
      )}
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
  return requestInFlight? spinner : b
}


