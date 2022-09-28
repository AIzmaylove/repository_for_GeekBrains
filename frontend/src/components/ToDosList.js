import React from 'react'

const ToDoItem = ({ToDo, deleteToDo}) => {
    return (
        <tr>
            <td>
                {ToDo.id}
            </td>
            <td>
                {ToDo.title}
            </td>
            <td>
                {ToDo.project}
            </td>
            <td>
                {ToDo.CreatorUser}
            </td>
            <td>
                {ToDo.description}
            </td>

            <td>
                <button onClick={() => deleteToDo(ToDo.id) }type='button'> Delete</button>
            </td>
        </tr>
    )
}

const ToDosList = ({ToDos, deleteToDo}) => {

    return (
        <table>
            <tr>
                <th>
                    ID
                </th>
                <th>
                    Title
                </th>
                <th>
                    project
                </th>
                <th>
                    CreatorUser
                </th>
                <th>
                    description
                </th>

                <th></th>
            </tr>


            {ToDos.map((ToDo) => <ToDoItem ToDo={ToDo} deleteToDo={deleteToDo}/>)}
        </table>
    )
}

export default ToDosList