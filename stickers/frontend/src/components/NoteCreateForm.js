import React from "react";
import Select from 'react-select'


class NoteCreateForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name: '',
            project: null,
            inner_text: '',
            date: '01/01/1970',
            options: this.setOptions(props.projects)
        }
    }

    setOptions(projects) {
        let options_list = [];
        projects.forEach(
            (project) => {
                let tmp = {};
                tmp['value'] = project.uuid
                tmp['label'] = project.name
                options_list.push(tmp);
            });
        return options_list
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    };

    handleSelectChange = (selectedOption) => {
        this.setState({'project': selectedOption.value}, () =>
            console.log(`Option selected:`, this.state.project)
        );
    };

    handleSubmit(event) {
        // console.log(`Note name - ${this.state.name}`)
        // console.log(`Project ID - ${this.state.project}`)
        // console.log(`Inner text - ${this.state.inner_text}`)
        // console.log(`Task date - ${this.state.date}`)
        this.props.createNote(this.state.name, this.state.project,
            this.state.inner_text, this.state.date)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="name">Name</label>
                    <input type="text" className="form-control" name="name" value={this.state.name}
                           onChange={(event) => this.handleChange(event)}/>
                </div>

                <div className="form-group">
                    <label for="inner_text">Text</label>
                    <input type="text" className="form-control" name="inner_text" value={this.state.inner_text}
                           onChange={(event) => this.handleChange(event)}/>
                </div>

                <div className="form-group">
                    <label htmlFor="date">Target date</label>
                    <input type="date" className="form-control" name="date" value={this.state.date}
                           onChange={(event) => this.handleChange(event)}/>
                </div>

                <div className="form-group">
                    <label htmlFor="project">Project</label>
                    <Select name='project' options={this.state.options}
                            onChange={(event) => this.handleSelectChange(event)}/>

                </div>

                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );
    }

}


export default NoteCreateForm