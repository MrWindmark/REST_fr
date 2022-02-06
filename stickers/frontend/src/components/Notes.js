import React from "react";


const NoteItem = ({note}) => {
    return (
        <tr>
            <td>{note.title}</td>
            <td>{note.inner_text}</td>
            <td>{note.created_at}</td>
            <td>{note.Date}</td>
            <td>{note.is_complited.toString()}</td>
            <td>{note.project_id.name}</td>
        </tr>
    )
}

const NotesList = ({notes}) => {
    return (
        <table>
            <th>Название</th>
            <th>Описание</th>
            <th>Дата создания</th>
            <th>Дата завершения</th>
            <th>Статус</th>
            <th>Имя проекта</th>
            {notes.map((elem) => <NoteItem note={elem}/>)}
        </table>
    )
}

export default NotesList
