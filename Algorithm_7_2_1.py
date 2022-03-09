from random import randint, choice
from timeit import timeit

def give_me_median_1(array, k): #Быстрая сортировка
    if len(array) == 1:
        return array[0]

    pivot = choice(array)

    left_el = [el for el in array if el < pivot]
    right_el = [el for el in array if el > pivot]
    pivots = [el for el in array if el == pivot]

    if k < len(left_el):
        return give_me_median_1(left_el, k)
    elif k < len(left_el) + len(pivots):
        return pivots[0]
    else:
        return give_me_median_1(right_el, k - len(left_el) - len(pivots))


M = 5
lst = [randint(0, 20) for _ in range(2 * M + 1)]
print(f'Исходный список:\n{lst}')
print(f'Медианой списка является:\n{give_me_median_1(lst, len(lst) / 2)}')
lst.sort()
print(f'Проверка!\nСписок после сортировки:\n{lst}')
print(f'Медианой списка является:\n{lst[len(lst) // 2]}')

t = (timeit("give_me_median_1(lst[:], M)", globals=globals(), number=10000))
print(f'замер по времени - ', t)

#Массив длинной 10 замер по времени -  0.09798649999999999
#Массив длинной 100 замер по времени -  0.2863432
#Массив длинной 1000 замер по времени - 2.3778194


#Взял пример с урока. Пытался разобраться с Кучей - не удалось
def gnome_method(lst):
    i = 1
    while i < len(lst):
        if not i or lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i] , lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
    return (f' {lst} \n Медианой списка является: \n {lst[len(lst) // 2]}')

print(gnome_method(lst))
t2 = (timeit("gnome_method(lst[:])", globals=globals(), number=10000))
print(f'замер по времени - ', t2)

#Массив длинной 10 замер по времени -  0.02943240000000001
#Массив длинной 100 замер по времени - 0.24185420000000002
#Массив длинной 1000 замер по времени - 2.5527133