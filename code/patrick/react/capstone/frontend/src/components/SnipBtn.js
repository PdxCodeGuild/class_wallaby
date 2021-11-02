import axios from "axios";
import React, { useEffect, useState } from "react";


export default function SnipBtn(id) {
  const [snipDetail, setSnipDetail] = useState(id.id.subscriber);
  const [snipbtn, setSnipBtn] = useState("add");

  async function UpdateSubs() {
    const data = {
      data:{
        data: {      
          "subscriber": [1]
        }
          }
      }
        
        
      
   

    console.log((id.id.id), " test")
    axios.patch(`http://localhost:8000/snipsubs/1`, data).then((res) => {  
    console.log(res);
    });
  } 

  useEffect(() => {}, []);

  function toAdd() {
    console.log(localStorage["UserID"])
    setSnipDetail((snipDetail) => [...snipDetail, 1]);
    setSnipBtn("remove");
    UpdateSubs()
  }

  function toRemove() {
    if (snipDetail.includes(1) === true) {
      const index = snipDetail.indexOf(1);
      if (index > -1) {
        snipDetail.splice(index, 1);
      } else {
        snipDetail.shift();
      }
    }
    setSnipDetail(snipDetail);
    setSnipBtn("add");
    console.log(snipDetail, " remove");
    UpdateSubs()
  }

  console.log(snipDetail, " check ");

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
