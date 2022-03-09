import random
from timeit import timeit

def buble_sort(array, reverse=False):
    if reverse:
        left = 1
        right = 0
    else:
        left = 0
        right = 1
    n = 1
    length = len(array)
    while n < length:
        count = True
        for i in range(n - 1, length - n):
            if array[i + left] > array[i + right]:
                array[i], array[i + 1] = array[i + 1], array[i]
                count = False
        if count:
            break
        for j in range(length - n, n - 1, -1):
            if array[j - left] < array[j - right]:
                array[j], array[j - 1] = array[j - 1], array[j]
        n += 1


#lst = [random.randint(-100, 99) for _ in range(1000)]
lst = [random.randint(-100, 99) for _ in range(10)]

random.shuffle(lst)
print(f'Список до сортировки:\n{lst}')
buble_sort(lst, reverse=True)
print(f'Список после сортировки:\n{lst}')

def buble_sort_2(lst):
    flag = True
    while flag:
        flag = False
        for i in range(len(lst) - 1):
            if lst[i+1] > lst[i]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = True
    return lst



print(f'Сортировка 2 - ' , buble_sort_2(lst[:]))

t1 = (timeit("buble_sort(lst[:])", globals=globals(), number=1000))
t2 = (timeit("buble_sort_2(lst[:])", globals=globals(), number=1000))

print(f'Сортировка 1 время - ' , t1)
print(f'Сортировка 2 время - ' ,t2)
print(f'Разница по скорости : {(t1-t2)/t1*100} %')

############################################################

"""Список до сортировки:
[-86, -45, -73, 29, 72, -83, -42, 69, -79, -41]
Список после сортировки:
[72, 69, 29, -41, -42, -45, -73, -79, -83, -86]
Сортировка 2 -  [72, 69, 29, -41, -42, -45, -73, -79, -83, -86]

замеры на 1000 массиве:
Сортировка 1 время -  149.2345871
Сортировка 2 время -  0.09913409999998635

замеры на 10 массиве:
Сортировка 1 время -  0.015860899999999997
Сортировка 2 время -  0.0011377999999999978
"""

""" Вывод: доработка имеет смысл , если работаем с небольшими массивами"""