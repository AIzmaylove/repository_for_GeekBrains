import React from 'react'

class ToDoForm extends React.Component{
    constructor(props) {
        super(props)

        this.state = {
            'title': '',
            'project': 0
//            'CreatorUser'
//            'description'
//            'completed'
//            'created_at'
//            'updated_at'
//
//            'date_from'
//            'date_to'
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }


//    handlePasswordChange(event) {
//        this.setState({
//            'password': event.target.value
//        })
//    }

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
        this.props.create_todo(this.state.title, this.state.project)
        console.log(this.state.title, this.state.project)
        event.preventDefault()
    }

    render() {
        return (
            <div>
                <form onSubmit={(event)=> this.handleSubmit(event)}>
                    <input type="text" name="title" placeholder="title" value={this.state.title} onChange={(event) => this.handleChange(event)}/>
                    <select onChange={(event) => this.handleProjectSelect(event)}>

                        {this.props.ToDos.map((ToDo) => <option value={ ToDo.id }>{ToDo.project} </option> )}
                    </select>
                    <input type="submit" value="Create" />
                </form>
            </div>
        )


    }
}


export default ToDoForm;


