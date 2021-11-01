import axios from 'axios';
import React, { useState } from 'react';


function UserSnippets() {
    // cosnt [snips, setSnips ] = useState(undefined)

    async function savedSnips() {
        await axios
       .patch("http://localhost:8000/imageupload/")
       .then(res => {
         console.log(res)
       })
       .catch((err) => {
           console.log(err)
        })
   }

    
//   useEffect(() => {
    
    return ( 
        <div>

            <p>Saved Snips</p>
        </div>
     );
}

export default UserSnippets;