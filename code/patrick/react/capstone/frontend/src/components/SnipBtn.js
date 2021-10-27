import React from 'react';







export default function SnipBtn() {
    const [snipbtn, setSnipBtn] = React.useState("add")

    const toAdd = () => setSnipBtn("add")
    const toRemove = () => setSnipBtn("remove")

  



    return(
        <div className={snipbtn} >
            {snipbtn === 'add' ? 
            (<button className="btn btn-primary" onClick = {toRemove}>Add</button>)
            :
            (<button className="btn btn-success" onClick = {toAdd}>Added</button>)
               
            }
        </div>
    )
}