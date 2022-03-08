''' пример с рекурсией взял из предыдущего задания'''
from memory_profiler import profile

@profile
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

user_nums = int("46456845554524135241324135270895096065813521532135213521352413524535645345453")
func(user_nums)

''' проблема с замером заключается в том, что сколько раз вызывается функция , столько таблиц с замерами и 
получаем. Чтобы избежать этого и получить одну таблицу, выполняем обёртывание на функции с рекурсией. 
Получем одну таблицу с замерами.'''