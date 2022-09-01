import React from 'react'

const ProjectItem = ({Project}) => {
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
        </tr>
    )
}

const ProjectsList = ({Projects}) => {
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

            {Projects.map((Project)  => <ProjectItem Project={Project} />)}
        </table>
    )
}

export default ProjectsList