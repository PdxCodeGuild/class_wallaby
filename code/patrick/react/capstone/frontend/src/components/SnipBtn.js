import axios from "axios";
import React, { useEffect, useState } from "react";

export default function SnipBtn(id) {
  const [snipDetail, setSnipDetail] = useState(id.id.subscriber);
  const [snipbtn, setSnipBtn] = useState("add");
  const [userID, setUserID] = useState(parseInt(localStorage["UserID"]))
  
  useEffect(() => {
    UpdateSubs();
  }, [snipDetail]);
  
  function UpdateSubs() {
    const data = {
      subscriber: snipDetail,
    };
    console.log(data, " request details sent");
    axios
      .patch(`http://localhost:8000/snipsubs/${id.id.id}`, data)
      .then((res) => {
        console.log(res.data.subscriber, " return patch request");
      });
  }


  function toAdd() {
    if (snipDetail.includes(userID) !== true) {
      console.log("is not subscribed test");
    }
    setSnipDetail((snipDetail) => [...snipDetail, userID]);
    setSnipBtn("remove");
    UpdateSubs();
    console.log(snipDetail)
  }

  function toRemove() {
    let index = snipDetail.indexOf(userID);
    snipDetail.splice(index, 1);
    console.log(snipDetail, " remove button output");
    var x = [];
    for (let i = 0; i < snipDetail.length; i++) {
      if (snipDetail[i] !== 1) {
        x.push(snipDetail[i]);
        console.log(snipDetail[i], " inside the for loop");
      }
    }
    console.log(x, " for loop");
    setSnipDetail([x]);
    setSnipBtn("add");
    UpdateSubs();
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
