import React from "react";
import {Link} from "react-router-dom";


const ProjectItem = ({project}) => {
    let users = project.included_users.map((elem) => <Link to={`/user/${elem.uuid}`}>{elem.username.toString() + ' '}</Link>)


    let data = (<tr>
            <td>{project.name}</td>
            <td>{project.repo_link}</td>
            <td>{users}</td>
        </tr>)
    return data
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <th>Название</th>
            <th>Адрес репозитория</th>
            <th>Пользователи</th>
            {projects.map((elem) => <ProjectItem project={elem}/>)}
        </table>
    )
}

export default ProjectList
