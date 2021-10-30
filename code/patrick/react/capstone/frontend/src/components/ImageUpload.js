import React, {useRef} from 'react'

function FileUpload() {
    const fileInput = useRef(null)

    const handleFileInput = (e) => {
        // handle validations
        onclick(e.target.files[0])
    }

    return (
        <div className="file-uploader">
            
        </div>
    )
}
export default FileUpload