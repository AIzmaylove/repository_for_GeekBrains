from statistics import median
from timeit import timeit
from random import randint

def give_me_median_3(lst):
    return median(lst[:])

M = 500
lst = [randint(0, 20) for _ in range(2 * M + 1)]

print(lst[:])
print(f'Медиана - ', give_me_median_3(lst[:]))

t = (timeit("give_me_median_3(lst[:])", globals=globals(), number=10000))
print(f'замер по времени - ', t)

#масиив длинной 10 замер по времени -  0.0100448
#масиив длинной 100 замер по времени - 0.0849238
#масиив длинной 1000 замер по времени - 1.3396802

#Вывод: судя по по замерам , лучше всего с массивами 1000 справляется вариант 3
#со встроенными функциями. Самым медленным оказался вариант - без сортировки