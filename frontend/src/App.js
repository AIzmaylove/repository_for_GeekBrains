import React from 'react'
import axios from 'axios'
import AuthorList from './components/AuthorList.js'
import UsersList from './components/UsersList.js'
import ProjectsList from './components/ProjectsList.js'
import ToDosList from './components/ToDosList.js'
import LoginForm from './components/LoginForm.js'
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
        return this.state.token != ''
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
                this.setState(
                    {
                        'CustomUsers': CustomUsers
                    }
                )

                this.state.CustomUsers = CustomUsers

             })
             .catch(error => console.log(error))


        axios
            .get('http://localhost:8000/api/authors/', {'headers': headers})
            .then(response => {
                const authors = response.data
                this.setState(
                    {
                        'authors': authors
                    }
                )

                this.state.authors = authors

            })
            .catch(error => console.log(error))

        axios
            .get('http://localhost:8000/api/Project/', {'headers': headers})
            .then(response => {
                const Project = response.data
                this.setState(
                    {
                        'Projects': Project
                    }
                )

                this.state.Project = Project

            })
            .catch(error => console.log(error))

        axios
            .get('http://localhost:8000/api/ToDo/', {'headers': headers})
            .then(response => {
                const ToDos = response.data
                this.setState(
                    {
                        'ToDos': ToDos
                    }
                )

                this.state.ToDos = ToDos

            })
            .catch(error => console.log(error))
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
                        <li> <Link to="/projects">Projects</Link> </li>
                        <li> <Link to="/ToDo">ToDo</Link> </li>
                        <li> {this.isAuth() ? <button onClick={() => this.logOut()}>Logout</button> : <Link to="/login">Login</Link> } </li>

                    </nav>

                    <Routes>
                        <Route exact path='/' element={<UsersList CustomUsers={this.state.CustomUsers} />} />
                        <Route exact path='/authors' element={<AuthorList authors={this.state.authors} />} />
                        <Route exact path='/login' element={<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login,password)}/>} />
                        <Route exact path='/ToDos' element={<ToDosList ToDos={this.state.ToDos} />} />
                        <Route path='/projects'>
                            <Route index element={<ProjectsList Projects={this.state.Projects} />} />
                            <Route path=':project_id' element={<ProjectsList Projects={this.state.Projects} />} />
                        </Route>

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


