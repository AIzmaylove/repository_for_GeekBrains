import React from 'react'

class ProjectForm extends React.Component{
    constructor(props) {
        super(props)

        this.state = {
            'title': '',
            'link_to_repo': '',
            'users': []
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }



    handleSubmit(event) {

        this.props.create_project(this.state.title, this.state.link_to_repo, this.state.users)

        event.preventDefault()
    }

    render() {
        return (
            <div>
                <form onSubmit={(event)=> this.handleSubmit(event)}>
                    <input type="text" name="title" placeholder="title" value={this.state.title} onChange={(event) => this.handleChange(event)}/>

            <div className="form-group">
                    <label for="link_to_repo">link_to_repo - </label>

                    <input type="text" className="form-control" name="link_to_repo" value={this.state.link_to_repo} onChange={(event) => this.handleChange(event)} />
            </div>
            <div className="form-group">
                    <label for="users">users - </label>

                    <select multiple name="users" className="form-control" onChange={(event) => this.handleChange(event)} >
                        {this.props.CustomUsers.map((item) => <option value={item.id}>{item.username}</option>)}
                    </select>
            </div>


                    <input type="submit" value="Create" />
                </form>
          </div>
        )


    }
}


export default ProjectForm;


