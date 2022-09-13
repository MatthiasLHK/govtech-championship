import React, { Component } from 'react';
import axios from 'axios';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';
import './TextBox.css'

class TextBox extends Component {

    constructor(props) {
        super(props);
        this.state = {
            value: ""
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }
    
    handleSubmit(event) {
        event.preventDefault();
        axios.post(this.props.api, {info: this.state.value}).then(res => {console.log(res)})
        this.setState({value: ''})
    }

    render() {
        return (
            <Form className="form" onSubmit={this.handleSubmit}>
                <Form.Group className="input-form">
                    <div className="textboxheader">
                        <div className="header">{this.props.header}</div>
                        <Form.Control
                        className="input-form-text"
                        as="textarea"
                        placeholder={this.props.placeholder}
                        onChange={this.handleChange}
                        value={this.state.value}
                        />
                    </div>
                    <div className="button">
                        <Button
                        className="input-form-submit-button"
                        variant="danger"
                        type="submit"
                        // onClick={this.handleSubmit}
                        >
                            Submit
                        </Button>
                    </div>
                </Form.Group>
            </Form>
        )
        // return (
        //     <form onSubmit={this.handleSubmit}>
        //         <label>
        //             {this.props.title}:<br></br>
        //             <textarea value={this.state.value} onChange={this.handleChange} />
        //         </label>
        //         <input type="submit" value="Submit" />
        //     </form>
        // );
    }
}

export default TextBox