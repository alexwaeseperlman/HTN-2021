import React from "react";
import "./Input.css"

const Input = () => {

    return (
        <div className="box">
            <form className="form-style-2" action="/upload" method="post" enctype="multipart/form-data">
                <input type="number" name="x" />
	            <input type="number" name="y" />
                <label htmlfor="myfile">Select an image: <br /> </label>
                <input type="file" id="myFile" name="img" className="input-field"/>< br />< br />
                <button type="submit" action="submit">Submit</button>
            </form>
        </div>)
}

export default Input;