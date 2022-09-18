import React from 'react'

const ProjectItem = ({Project, deleteProject}) => {
    return (
        <tr>
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
    let filtered_Projects = Projects.filter(Project => Project.is_active == 1)
    return (
        <table>
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