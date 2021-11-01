import axios from 'axios';
import React, { useState } from 'react';


function UpdateImage() {
    const [image, setImage] = useState(null)

    const ImageChange = (e) => {
        setImage(
            e.target.files[0]
          )
        }
    const Submit = (e) => {
        e.preventDefault();
        const form_data = new FormData();
        form_data.append('image', image)

        axios.patch("http://localhost:8000/imageupload/", form_data)
        .then(res => {
            console.log(res.data);
          })
          .catch(err => console.log(err))
    }

    return (
        <form onSubmit={Submit}>
          {/* <p>
            <input type="text" placeholder='Title' id='title' value={this.state.title} onChange={this.handleChange} required/>
          </p>
          <p>
            <input type="text" placeholder='Content' id='content' value={this.state.content} onChange={this.handleChange} required/>

          </p> */}
          <p>
            <input type="file"
                   id="image"
                   accept="image/png, image/jpeg"  onChange={ImageChange} required/>
          </p>
          <input type="submit"/>
        </form>
     );
}

export default UpdateImage;