import React from "react";
import {useParams} from "react-router";


const OneUserItem = ({users}) => {
    let {id} = useParams();
    let filtered_users = users.filter((user) => user.uuid == id)
    return (
        <table>
            <tr>
                <th>Никнейм</th>
                <th>Имя</th>
                <th>Фамилия</th>
                <th>Почта</th>
            </tr>
            {filtered_users.map((user) => <UserItem user={user}/>)}
        </table>
    )

}

const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.username}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <th>Никнейм</th>
            <th>Имя</th>
            <th>Фамилия</th>
            <th>Адрес почты</th>
            {users.map((user) => <UserItem user={user}/>)}
        </table>
    )
}


export default UserList
