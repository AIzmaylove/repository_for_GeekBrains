import React from 'react'

const ToDoItem = ({ToDo, deleteToDo}) => {
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
            <td>
                <button onClick={() => deleteToDo(ToDo.id) }type='button'> Delete</button>
            </td>
        </tr>
    )
}

const ToDosList = ({ToDos, deleteToDo}) => {
    let filtered_ToDos = ToDos.filter(ToDo => ToDo.is_active == 1)
    return (
        <table>
            <tr>
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
                <th></th>
            </tr>


            {ToDos.map((ToDo) => <ToDoItem ToDo={ToDo} deleteToDo={deleteToDo}/>)}
        </table>
    )
}

export default ToDosList