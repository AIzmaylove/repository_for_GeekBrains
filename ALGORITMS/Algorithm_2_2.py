'''Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).'''
def my_func(number, chet = 0, nechet = 0):

    if number == 0:
        print(f'Введено нулевое значение ({chet}, {nechet})')
    else:
        current_number = number % 10
        number = number // 10
        if current_number % 2 == 0:
            chet += 1
        else:
            nechet += 1
        return my_func(number, chet, nechet)

number = int(input('Введите число: '))
my_func(number)