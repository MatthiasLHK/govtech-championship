import React, { Component } from 'react';
import axios from 'axios';

class TextBox extends Component {

    constructor(props) {
        super(props);
        this.state = {
            value: this.props.value
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }
    
    handleSubmit(event) {
        // alert('An essay was submitted: ' + this.state.value);
        axios.post(this.props.api, {info: this.state.value}).then(res => {console.log(res)})
        event.preventDefault();
        this.setState({value:''})
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>
                    {this.props.title}:<br></br>
                    <textarea value={this.state.value} onChange={this.handleChange} />
                </label>
                <input type="submit" value="Submit" />
            </form>
          );
    }
}

export default TextBox