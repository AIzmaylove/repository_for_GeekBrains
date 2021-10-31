""""Здесь не знаю, нужны ли какие-то комментарии. Методом проб и ошибок
пришел к данному решению. Единственное вывод можно сделать более красивым"""
my_time = int(input('Введите число: '))
days = my_time // 86400
hours = (my_time - (days * 86400)) // 3600
minutes = (my_time - ((days * 86400) + (hours * 3600))) // 60
secunds = (my_time - ((days * 86400) + (hours * 3600) + (minutes * 60)))
print(days, 'd')
print(hours, 'h')
print(minutes, 'm')
print(secunds, 's')