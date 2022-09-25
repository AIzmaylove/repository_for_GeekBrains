import React from 'react'

class ToDoForm extends React.Component{
    constructor(props) {
        super(props)

        this.state = {
            'title': '',
            'project': '',
            'CreatorUser': [],
            'description': '',
            'completed': '',
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }


    handleProjectSelect(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'project': []
            })
            return;
        }
        let project = []

        for(let option of event.target.selectedOptions) {
            project.push(option.value)
        }
        this.setState({
            'project': project
        })
    }



    handleSubmit(event) {
        this.props.create_todo(this.state.title, this.state.project, this.state.CreatorUser, this.state.description)
        event.preventDefault()
    }

    render() {
        return (
            <div>
                <form onSubmit={(event)=> this.handleSubmit(event)}>
                    <input type="text" name="title" placeholder="title" value={this.state.title} onChange={(event) => this.handleChange(event)}/>

                    <select multiple onChange={(event) => this.handleProjectSelect(event)}>
                        {this.props.ToDos.map((ToDo) => <option value={ ToDo.id }>{ToDo.project} </option> )}
                    </select>

                    <input type="text" name="description" placeholder="description" value={this.state.description} onChange={(event) => this.handleChange(event)}/>


                    <input type="submit" value="Create" />
                </form>
            </div>
        )


    }
}


export default ToDoForm;


