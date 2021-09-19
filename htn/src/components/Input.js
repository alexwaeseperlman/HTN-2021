import React from "react";
import "./Input.css"

const Input = () => {

    return (
        <div className="box">
            <form className="form-style-2">
                <label htmlfor="myfile">Select an image: <br /> </label>
                <input type="file" id="myFile" name="filename" className="input-field"/>< br />< br />
                <button>Submit</button> 
            </form>
        </div>)
}

export default Input;