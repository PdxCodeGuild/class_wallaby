import axios from 'axios';
import React, { useEffect, useState } from 'react';


export default function SnipBtn(id, pk) {
    const [snipDetail, setSnipDetail] = useState([])
    const [snipbtn, setSnipBtn] = useState("add")

   

    const toAdd = () => {
        console.log(id.id.subscriber)
        setSnipDetail(id.id.subscriber)
        setSnipDetail((snipDetail) => [...snipDetail,  ])
        setSnipBtn("remove")
        
    }
    if (snipDetail.includes(1)) {
        console.log('test')
    }
    // else {
    //     console.log('null')
    // }
    
    const toRemove = () => {
        console.log(pk)
    const index = snipDetail.indexOf(pk)
    const update = snipDetail.splice(index, 1)
    // setSnipDetail(update)
    setSnipBtn("add")
    
    console.log(snipDetail)
}    

// useEffect(() => {
//     axios.get("http://localhost:8000/snipsubs/1").then((res) => {
//         console.log(res, 'response')
// })
// })
  



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