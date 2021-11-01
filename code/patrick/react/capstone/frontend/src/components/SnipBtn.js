import axios from 'axios';
import React, { useState } from 'react';


export default function SnipBtn(id) {
    const [snipDetail, setSnipDetail] = useState([])
    const [snipbtn, setSnipBtn] = useState("add")
    
    const toAdd = () => {
        setSnipDetail(id)
        setSnipBtn("remove")

    }
    
    const toRemove = () => {
    setSnipBtn("add")
    console.log({id})
    
}    

useEffect(() => {
    axios.get("http://localhost:8000/snipsubs/1").then((res) => {
  



    return(
        <div className={snipbtn} >
            {snipbtn === 'add' ? 
            (<button className="btn btn-primary" onClick= {toAdd}>Add</button>)
            :
            (<button className="btn btn-success" onClick = {toRemove}>Added</button>)
               
            }
        </div>
    )
}