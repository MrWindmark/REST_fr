import {useParams} from "react-router";
import React from "react";

const UserNotesList = ({notes}) => {
    let {id} = useParams();
    let filtered_users = notes.filter((note) => note.creator.id === id)
     return (
        <table>
            <th>Название</th>
            <th>Описание</th>
            <th>Дата создания</th>
            <th>Дата завершения</th>
            <th>Статус</th>
            <th>Создатель</th>
            {filtered_users.map((note) => <UserNote note={note}/>)}
        </table>
    )
}

const UserNote = ({note}) => {
    return (
        <tr>
            <td>{note.title}</td>
            <td>{note.inner_text}</td>
            <td>{note.created_at}</td>
            <td>{note.Date}</td>
            <td>{note.is_complited.toString()}</td>
            <td>{note.creator.username}</td>
        </tr>
    )
}

export default UserNotesList