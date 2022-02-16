import React from "react";


class LoginForm extends React.Component {
    history;
    constructor(props) {
        super(props);
        this.state = {username: '', password: ''}

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmitEvents = this.handleSubmitEvents.bind(this);
    }


    handleChange(event) {
        this.setState(
            {[event.target.name]: event.target.value}
        );
    }

    handleSubmitEvents(event) {
        this.props.get_token(this.state.username, this.state.password)
        event.preventDefault()
    }

    render() {
        return (
            <div class="LoginForm">
                <form onSubmit={this.handleSubmitEvents}>
                    {
                        //handle error condition
                    }
                    <label>User Name</label>
                    <input type="text" name="username" value={this.state.username}
                           onChange={this.handleChange}/>
                    <label>Password</label>
                    <input type="password" name="password" value={this.state.password}
                           onChange={this.handleChange}/>
                    <input type="submit" value="Log In"/>
                </form>
            </div>
        );
    }
}

export default LoginForm