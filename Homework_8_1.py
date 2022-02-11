import re

my_mail_adress = 'someonegeek@brains.ru'
user_name = re.split(r'@', my_mail_adress)

try:
    index = my_mail_adress.index('.') and my_mail_adress.index('@')
    print('username:', user_name[0],'\n','domain:', user_name[1])
except ValueError:
    index = len(my_mail_adress)
    print('Введен неверный адрес')

