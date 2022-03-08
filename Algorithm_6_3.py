''' Задание из курса основ. Урок 1 задание 1'''

from memory_profiler import profile
from memory_profiler import memory_usage

def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение memory_usage: {mem_diff} Mib")
        return res
    return wrapper

nums = 3564365463546354513541365416355413524135416534165345134514565651665566565

@profile
def conk():
    my_time = int(input('Введите число: '))
    days = my_time // 86400
    hours = (my_time - (days * 86400)) // 3600
    minutes = (my_time - ((days * 86400) + (hours * 3600))) // 60
    secunds = (my_time - ((days * 86400) + (hours * 3600) + (minutes * 60)))
    print(days, 'd')
    print(hours, 'h')
    print(minutes, 'm')
    print(secunds, 's')


conk()
#Выполнение memory_usage: 0.05078125 Mib
# Profile - 19.6 Mib

'''
@decor
def f_str(duration):
    month = duration // 2592000
    d = (duration - month * 2592000) // 86400
    h = (duration - month * 2592000 - d * 86400) // 3600
    m = (duration - month * 2592000 - d * 86400 - h * 3600) // 60
    s = duration % 60

    print(f'{month} месяца {d} дней {h} часов {m} минут {s} секунд')


f_str(nums)'''
#Выполнение memory_usage: 0.0234375 Mib , уменьшил результат в 2 раза
# Profile - 19.6 Mib остался прежним