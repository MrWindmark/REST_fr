import React from "react";
import axios from 'axios';
// import logo from './logo.svg';
import {BrowserRouter, Link, Navigate, Route, Routes} from 'react-router-dom'
import './App.css';
import UserList from './components/User.js'
import ProjectList from "./components/Projects";
import NotesList from "./components/Notes";
import UserNotesList from "./components/UserNotes";
import LoginForm from "./components/auth";
import Cookies from 'universal-cookie';
// import {useNavigate} from "react-router";


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
            'notes': [],
            token: '',
            refresh: '',
            username: '',
            password: ''
        }
    }

    set_token(token, refresh) {
        const cookies = new Cookies()
        cookies.set('token', token)
        cookies.set('refresh_token', refresh)
        this.setState({'token': token, 'refresh': refresh}, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('', '')
        this.setState({
            'users': [],
            'projects': [],
            'notes': []
        })
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        const refresh = cookies.get('refresh_token')
        this.setState({'token': token, 'refresh_token': refresh}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api/token/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['access'], response.data['refresh'])
            }).catch(error => alert('Неверный логин или пароль'))
        // .then(() => alert(this.state.token))
    }

    refresh_token() {
        console.log(`We are in refresh line and do refresh!`)
        const cookies = new Cookies()
        const refresh = cookies.get('refresh_token')
        axios.post('http://127.0.0.1:8000/api/token/refresh/', {refresh})
            .then(response => {
                this.set_token(response.data['access'], refresh)
            }).catch(error => alert('Требуется повторный вход в уч.запись'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Bearer ' + this.state.token
        }
        return headers
    }

    load_data() {
        const urls = [
            'http://localhost:8000/api/users',
            'http://localhost:8000/api/projects',
            'http://localhost:8000/api/notes'
        ]
        const headers = this.get_headers()
        let req = urls.map(url => axios.get(url))

        Promise.all(req)
            .then(response => {
                // not work anyway...
                response.forEach((result) => {
                    if (result.status == "rejected") {
                        this.refresh_token()
                        this.load_data()
                    }
                });

                if (response[0].status !== 200 || response[1].status !== 200 || response[2].status !== 200) {
                    console.log(
                        `We are here and do refresh.
                        ${response[0].status} - ${response[1].status} - ${response[2].status}`
                    )
                    this.refresh_token()
                    this.load_data()
                }
                // else {
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
                // }
            }).catch(error => {
                console.log(`We are in catch and do refresh.`)
                this.refresh_token()
                this.load_data()
                console.log(error)
            }
        )
    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    deleteNote(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/notes/${id}`, {headers})
            .then(response => {
                this.setState({notes: this.state.notes.filter((item) => item.id !== id)})
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
                            {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> :
                                <Link to='/login'>Login</Link>}
                            <button onClick={() => this.refresh_token()}>Refresh token</button>
                            <button onClick={() => this.load_data()}>Load Data</button>
                        </ul>
                    </nav>
                    <Routes>
                        <Route path='/' element={<UserList users={this.state.users}/>}/>
                        <Route path="/users" element={<Navigate replace to="/"/>}/>
                        <Route path="/notes/user/:id" element={<UserNotesList notes={this.state.notes}/>}/>
                        <Route path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                        <Route path='/notes' element={
                            <NotesList notes={this.state.notes}
                                       deleteNote={(id) => this.deleteNote(id)}/>}
                        />
                        <Route path='/login' element={<LoginForm get_token={(username, password) =>
                            this.get_token(username, password)}/>}/>
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
