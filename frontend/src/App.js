import React from 'react'
import axios from 'axios'
import AuthorList from './components/AuthorList.js'
import UsersList from './components/UsersList.js'
import ProjectsList from './components/ProjectsList.js'
import ToDosList from './components/ToDosList.js'
import LoginForm from './components/LoginForm.js'
import ToDoForm from './components/ToDoForm.js'
import ProjectForm from './components/ProjectForm.js'
import Navbar from './components/Menu.js'
import Footer from './components/Footer.js'
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate} from 'react-router-dom'



class App extends React.Component{
    constructor(props) {
        super(props)

        this.state = {
            'authors':[],
            'CustomUsers':[],
            'Projects':[],
            'ToDo':[],
            'token': ''
        }
    }

    obtainAuthToken(login, password) {
        axios
            .post('http://localhost:8000/api-auth-token/', {
                'username': login,
                'password': password
            })
            .then(response => {
                const token = response.data.token
                console.log('token:', token)
                localStorage.setItem('token', token)
                this.setState({
                    'token': token
                },this.getData)
             })
            .catch(error => console.log(error))
    }

    isAuth() {
        return !!this.state.token
    }


//    create_project(title, link_to_repo, users) {
//        const headers = this.get_headers()
//        const data = { title: title, link_to_repo: link_to_repo, users: [parseInt(users, 10)] }
//        axios
//            .post('http://127.0.0.1:8000/api/projects/', data, { headers })
//            .then(response => {
//                let new_project = response.data
//                const users = this.state.users.filter((item) => item.id === new_project.users)[0]
//                new_project.users = users
//                this.setState({ projects: [...this.state.projects, new_project] })
//            }).catch(error => console.log(error))
//    }


    create_project(title, link_to_repo, users){
        console.log(title, link_to_repo, users)

        let headers = this.getHeaders()

        axios
             .post('http://localhost:8000/api/Project/',{'title': title, 'link_to_repo': link_to_repo, 'users': users} , {'headers': headers})
             .then(response => {
                this.getData()
             })
             .catch(error => {
                console.log(error)
             })

    }

     deleteProject(id) {
        console.log(id)
        const headers = this.get_headers()
        axios
            .delete('http://localhost:8000/api/Project/${id}', {'headers': headers})
            .then(response => {
                this.setState({Projects: this.state.Projects.filter((item)=>item.id !== id)})
            })
            .catch(error => console.log(error))
    }




    create_todo(title, project){
        console.log(title, project)

        let headers = this.getHeaders()

        axios
             .post('http://localhost:8000/api/ToDo/',{'title': title, 'project': project} , {'headers': headers})
             .then(response => {
                this.getData()
             })
             .catch(error => {
                console.log(error)
             })

    }

    deleteToDo(id) {
        console.log(id)
        const headers = this.get_headers()
        axios
            .delete('http://localhost:8000/api/ToDo/${id}', {'headers': headers})
            .then(response => {
                this.setState({ToDos: this.state.ToDos.filter((item)=>item.id !== id)})
            })
            .catch(error => console.log(error))
    }




    componentDidMount() {
        let token = localStorage.getItem('token')
        this.setState({
            'token': token
        },this.getData)
    }

    getHeaders() {
        if (this.isAuth()) {
            return {
                'Authorization': 'Token ' + this.state.token
            }
        }
        return {}
    }



    getData() {
        let headers = this.getHeaders()

        axios
             .get('http://localhost:8000/api/CustomUser/', {'headers': headers})
             .then(response => {
                const CustomUsers = response.data
                this.setState({
                    'CustomUsers': CustomUsers
                })
             })
             .catch(error => {
                console.log(error)
                this.setState({'CustomUsers': [] })
             })

        axios
            .get('http://localhost:8000/api/authors/', {'headers': headers})
            .then(response => {
                const authors = response.data
                this.setState({
                        'authors': authors
                    })
            })
            .catch(error => {
                console.log(error)
                this.setState({'authors': [] })
             })

        axios
            .get('http://localhost:8000/api/Project/', {'headers': headers})
            .then(response => {
                const Project = response.data
                this.setState({
                        'Projects': Project
                    })
            })
            .catch(error => {
                console.log(error)
                this.setState({'Projects': [] })
             })

        axios
            .get('http://localhost:8000/api/ToDo/', {'headers': headers})
            .then(response => {
                const ToDos = response.data
                this.setState({
                        'ToDos': ToDos
                    })
            })
            .catch(error => {
                console.log(error)
                this.setState({'ToDos': [] })
             })


    }


    logOut(){
        localStorage.setItem('token', '')
        this.setState({
            'token': ''
        },this.getData)
    }



    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li> <Link to="/">Users</Link> </li>
                        <li> <Link to="/authors">Authors</Link> </li>
                        <li> <Link to="/Project">Projects</Link> </li>
                        <li> <Link to="/ToDos">ToDo</Link> </li>
                        <li> <Link to="/create_todo">Create ToDo</Link> </li>
                        <li> <Link to="/create_project">Create Project</Link> </li>
                        <li> {this.isAuth() ? <button onClick={() => this.logOut()}>Logout</button> : <Link to="/login">Login</Link> } </li>

                    </nav>

                    <Routes>
                        <Route exact path='/' element={<UsersList CustomUsers={this.state.CustomUsers} />} />
                        <Route exact path='/authors' element={<AuthorList authors={this.state.authors} />} />
                        <Route exact path='/login' element={<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login,password)}/>} />
//                        <Route exact path='/ToDos' element={<ToDosList ToDos={this.state.ToDos} />} />
                        <Route exact path='/ToDos' element={() => <ToDosList ToDos={this.state.ToDos} deleteToDo={(id)=>this.deleteToDo(id)} />} />
                        <Route exact path='/create_todo' element={<ToDoForm ToDos={this.state.ToDos} />} />

                        <Route path='/Project'>
                            <Route index element={<ProjectsList Projects={this.state.Projects} />} />
                            <Route path=':project_id' element={<ProjectsList Projects={this.state.Projects} />} />
                        </Route>
                        <Route exact path='/create_project' element={<ProjectForm CustomUsers={this.state.CustomUsers} create_project={(title, link_to_repo, users) => this.create_project(title, link_to_repo, users)} />} />
                    </Routes>
                </BrowserRouter>
            </div>
        )

//        return (
//            <div>
//              <header>
//              <Navbar navbarItems={this.state.navbarItems} />
//              </header>
//              <main role="main" class="flex-shrink-0">
//              <div className="container">
//                <UsersList CustomUsers={this.state.CustomUsers} />
//              </div>
//              </main>
//                <Footer/>
//            </div>
//
//
//            )

    }
}


export default App;


