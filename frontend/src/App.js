import React from 'react'
import axios from 'axios'
import AuthorList from './components/AuthorList.js'
import UsersList from './components/UsersList.js'
import ProjectsList from './components/ProjectsList.js'
import ToDosList from './components/ToDosList.js'
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
            'ToDo':[]
        }
    }



    componentDidMount() {
        axios
             .get('http://localhost:8000/api/CustomUser/')
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
            .get('http://localhost:8000/api/authors/')
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
            .get('http://localhost:8000/api/Project/')
            .then(response => {
                const Project = response.data
                this.setState(
                    {
                        'Project': Project
                    }
                )

                this.state.Project = Project

            })
            .catch(error => console.log(error))

        axios
            .get('http://localhost:8000/api/ToDo/')
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


    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li> <Link to="/">Users</Link> </li>
                        <li> <Link to="/authors">Authors</Link> </li>
                        <li> <Link to="/projects">Projects</Link> </li>
                        <li> <Link to="/ToDo">ToDo</Link> </li>
                    </nav>

                    <Routes>
                        <Route exact path='/' element={<UsersList CustomUsers={this.state.CustomUsers} />} />
                        <Route exact path='/authors' element={<AuthorList authors={this.state.authors} />} />
                        <Route exact path='/project' element={<ProjectsList Projects={this.state.Projects} />} />
                        <Route exact path='/todo' element={<ToDosList ToDos={this.state.ToDos} />} />
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


