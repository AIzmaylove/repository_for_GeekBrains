users = {'a.medvede': {'password':'pass1','activation': True }, 'a.izmaylov': {'password':'pass2','activation': False}}
# O(N)
def authorization_f(users, user_name,user_password):
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return "Добро пожаловать! Доступ разрешен."
            elif value['password'] == user_password and not value['activation']:
                return "Учетная запись не активна! Пройдите активацию."
            elif value['password'] != user_password:
                return "Неверно введен пароль!"
    return "Данного пользователя не существует"

print(authorization_f(users, 'a.medvede','pass1'))

#O(1)
'''def authorization_s(users, user_name,user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password and users[user_name]['activation']:
            return "Добро пожаловать! Доступ разрешен."
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']:
            return "Учетная запись не активна! Пройдите активацию."
        elif users[user_name]['password'] != user_password:
            return "Неверно введен пароль!"
    else:
        return "Данного пользователя не существует"
'''
