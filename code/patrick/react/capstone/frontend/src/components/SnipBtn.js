import axios from "axios";
import React, { useEffect, useState } from "react";

export default function SnipBtn(id) {
  var [snipDetail, setSnipDetail] = useState(id.id.subscriber);
  const [snipbtn, setSnipBtn] = useState("add");
  const userID = localStorage["UserID"];
  

  async function UpdateSubs() {
    const data = {
      subscriber: snipDetail,
    };
    console.log(data, " request details sent");
    await axios
      .patch(`http://localhost:8000/snipsubs/${id.id.id}`, data)
      .then((res) => {
        console.log(res.data.subscriber, " return patch request");
        setSnipDetail(res.subscriber);
      });
  }

  function toAdd() {
    setSnipDetail(snipDetail)
    if (snipDetail.includes(userID) !== true) {
      console.log(snipDetail)
      setSnipDetail(snipDetail => [...snipDetail, userID]);
      console.log("is not subscribed test");
      setSnipBtn("remove");
      UpdateSubs();
      console.log(snipDetail)

    }
  }

  function toRemove() {
    if (snipDetail.includes(userID) === true) {
    let index = snipDetail.indexOf(userID);
    snipDetail.splice(index, 1);
    console.log(snipDetail, " remove button output");
    setSnipDetail(snipDetail);
    setSnipBtn("add");
    UpdateSubs();
    }
  }

  return (
    <div className={snipbtn}>
      {snipbtn === "add" ? (
        <button className="btn btn-primary" onClick={toAdd}>
          Add
        </button>
      ) : (
        <button className="btn btn-success" onClick={toRemove}>
          Added
        </button>
      )}
    </div>
  );
}
