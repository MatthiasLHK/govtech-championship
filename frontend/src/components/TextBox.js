import React, { Component } from 'react';
import axios from 'axios';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Alert from 'react-bootstrap/Alert'
import 'bootstrap/dist/css/bootstrap.min.css';
import './TextBox.css'

class TextBox extends Component {

    constructor(props) {
        super(props);
        this.state = {
            value: "",
            isError: false,
            errMess: '',
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value, isError: false});
    }
    
    handleSubmit(event) {
        event.preventDefault();
        axios.post(this.props.api, {info: this.state.value})
        .then(res => {
            console.log(res)
        })
        .catch(err => {
            this.setState({isError: true, errMess: err.response['data']})
        });
        this.setState({value: ''});
        // setTimeout(() => {  window.location.reload(false); }, 2000);
    }

    render() {
        return (
            <div>
                {
                    this.state.isError && <Alert>{this.state.errMess}</Alert>
                }
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
                            >
                                Submit
                            </Button>
                        </div>
                    </Form.Group>
                </Form>
            </div>           
        )
    }
}

export default TextBox