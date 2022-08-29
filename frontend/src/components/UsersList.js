const UsersItem = ({CustomUser}) => {
    return (
        <tr>
            <td>
                {CustomUser.username}
            </td>
            <td>
                {CustomUser.first_name}
            </td>
            <td>
                {CustomUser.last_name}
            </td>
            <td>
                {CustomUser.email}
            </td>
        </tr>
    )
}

const UsersList = ({CustomUsers}) => {
    return (
        <table>
            <th>
                Usersname
            </th>
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                Email
            </th>
            {CustomUsers.map((CustomUser) => <UsersItem CustomUser={CustomUser} />)}
        </table>
    )
}

export default UsersList