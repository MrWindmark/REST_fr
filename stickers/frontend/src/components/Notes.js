import React from "react";
import {Link} from "react-router-dom";


const NoteItem = ({note, deleteNote}) => {
    return (
        <tr>
            <td>{note.title}</td>
            <td>{note.inner_text}</td>
            <td>{note.created_at}</td>
            <td>{note.Date}</td>
            <td>{note.is_complited.toString()}</td>
            <td>{note.project_id.name}</td>
            <td>
                <button type='button' onClick={() => deleteNote(note.uuid)}>Delete</button>
            </td>
        </tr>
    )
}

const NotesList = ({notes, deleteNote}) => {
    return (
        <div>
            <Link to='/notes/create'>Create</Link>
            <table>
                <th>Название</th>
                <th>Описание</th>
                <th>Дата создания</th>
                <th>Дата завершения</th>
                <th>Статус</th>
                <th>Имя проекта</th>
                <th></th>
                {notes.map((elem) => <NoteItem note={elem} deleteNote={deleteNote}/>)}
            </table>
        </div>
    )
}

export default NotesList
