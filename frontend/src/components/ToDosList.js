import React from 'react'

const ToDoItem = ({ToDo}) => {
    return (
        <tr>
            <td>
                {ToDo.project}
            </td>
            <td>
                {ToDo.CreatorUser}
            </td>
            <td>
                {ToDo.title}
            </td>
            <td>
                {ToDo.created_at}
            </td>
        </tr>
    )
}

const ToDosList = ({ToDos}) => {
    return (
        <table>
            <th>
                Project
            </th>
            <th>
                Creator
            </th>
            <th>
                Title
            </th>
            <th>
                Date
            </th>
            {ToDos.map((ToDo) => <ToDoItem ToDo={ToDo} />)}
        </table>
    )
}

export default ToDosList