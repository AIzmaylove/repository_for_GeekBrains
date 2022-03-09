from timeit import timeit
from random import randint, choice


M = 5
lst = [randint(0, 20) for _ in range(2 * M + 1)]

def give_me_median_2(lst):
    for i in range(len(lst)//2):
        lst.remove(max(lst))
    return max(lst)

print(lst)
print(give_me_median_2(lst))

t = (timeit("give_me_median_2(lst[:])", globals=globals(), number=10000))
print(f'замер по времени - ', t)

#масиив длинной 10 замер по времени -  0.017459799999999998
#масиив длинной 100 замер по времени - 0.2820659
#масиив длинной 1000 замер по времени - 21.9462264