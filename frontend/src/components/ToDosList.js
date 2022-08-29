import React from 'react'

const ToDoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.CreatorUser}
            </td>
            <td>
                {todo.title}
            </td>
            <td>
                {todo.created_at}
            </td>
        </tr>
    )
}

const ToDosList = ({todos}) => {
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
            {todos.map((todo) => <ToDoItem todo={todo} />)}
        </table>
    )
}

export default ToDosList