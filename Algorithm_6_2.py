''' Задача с курса Алгоритмов. Урок 2 задание 2.
Удалось улучшить показатели memory_usage на порядок, а profile на 0.1 стал больше'''

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
'''
@decor
def func(func_nums):
    def my_func(number, chet = 0, nechet = 0):
        if number == 0:
            print(f'четных {chet}, нечетных {nechet}')
        else:
            current_number = number % 10
            number = number // 10
            if current_number % 2 == 0:
                chet += 1
            else:
                nechet += 1
            return my_func(number, chet, nechet)  

    print(f"{my_func(func_nums)}")
#Выполнение memory_usage: 0.03515625 Mib
#profile - 19.7 Mib
'''


@profile
def func_2(nums):
    even = 0
    not_even = 0
    for i in str(nums):
        if int(i) % 2 == 0:
            even += 1
        else:
            not_even += 1
    return even, not_even

#Выполнение memory_usage: 0.0078125 Mib
#profile - 19.6 Mib

number = int("4645684555456655656455451515341351352143524135241324135213521532135213521352413524535645345453")
user_nums = int("4645684555456655656455451515341351352143524135241324135213521532135213521352413524535645345453")
#print(func(user_nums))
print(func_2(user_nums))