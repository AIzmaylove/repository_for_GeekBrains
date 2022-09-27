import React from 'react'

const ProjectItem = ({Project, deleteProject}) => {
    return (
        <tr>
            <td>
                {Project.id}
            </td>
            <td>
                {Project.title}
            </td>
            <td>
                {Project.users}
            </td>
            <td>
                {Project.link_to_repo}
            </td>
            <td>
                <button onClick={() => deleteProject(Project.id) }type='button'> Delete</button>
            </td>
        </tr>
    )
}

const ProjectsList = ({Projects, deleteProject}) => {

    return (
        <table>
            <th>
                ID
            </th>
            <th>
                Title
            </th>
            <th>
                Users
            </th>
            <th>
                Link
            </th>

            {Projects.map((Project) => <ProjectItem Project={Project} deleteProject={deleteProject}/>)}
        </table>
    )
}

export default ProjectsList