'''Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.'''

'''def reverse(n, r):
    if n == 0:
        return r
    else:
        return reverse(n // 10, r * 10 + n % 10)

number = int(input("Введите число: "))
reversed_number = reverse(number,0)
print(reversed_number)'''

'''если число заканчивается 0.'''
def reverse_2(n):
    rest_numb, numeral = divmod(n, 10)
    if rest_numb == 0:
        return str(numeral)
    else:
        return str(numeral) + str(reverse_2(rest_numb))

number = int(input("Введите число: "))
print(reverse_2(number))