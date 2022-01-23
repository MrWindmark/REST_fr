import React from "react";
import axios from 'axios';
import logo from './logo.svg';
import {BrowserRouter, HashRouter, Link, Navigate, Route, Routes} from 'react-router-dom'
import './App.css';
import UserList from './components/User.js'
import ProjectList from "./components/Projects";
import NotesList from "./components/Notes";
import UserNotesList from "./components/UserNotes";


const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'notes': []
        }
    }

    componentDidMount() {
        const urls = [
            'http://localhost:8000/api/users',
            'http://localhost:8000/api/projects',
            'http://localhost:8000/api/notes'
        ]
        Promise.all([
            axios.get(urls[0]),
            axios.get(urls[1]),
            axios.get(urls[2])
        ]).then(response => {
            const users = response[0].data['results']
            const projects = response[1].data['results']
            const notes = response[2].data['results']
            console.log(users, projects, notes)
            this.setState(
                {
                    'users': users,
                    'projects': projects,
                    'notes': notes
                }
            )
        }).catch(error => console.log(error))

    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/notes'>Notes</Link>
                            </li>
                        </ul>
                    </nav>
                    <Routes>
                        <Route path='/' element={<UserList users={this.state.users}/>}/>
                        <Route path="/users" element={<Navigate replace to="/" />} />
                        <Route path="/user/:id" element={<UserNotesList notes={this.state.notes}/>} />
                        <Route path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                        <Route path='/notes' element={<NotesList notes={this.state.notes}/>}/>
                        <Route component={NotFound404}/>
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

export default App;
