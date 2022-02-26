from collections import deque
from timeit import timeit

# DEQUE
def deque_list():
    my_list_1 = list('Hello World!')
    deq_list = deque(my_list_1)
    a = range(10)
    for i in a:
        deq_list.append('!')
    return deq_list

def deque_list_2():
    my_list_1 = list('Hello World!')
    deq_list = deque(my_list_1)
    a = range(10)
    for i in a:
        deq_list.pop()
    return deq_list

def deque_list_3():
    my_list_1 = list('Hello World!')
    deq_list = deque(my_list_1)
    a = range(10)
    for i in a:
        deq_list.extend('Stop WAR!')
    return deq_list


def order_list():
    my_list_2 = list('Hello World!')
    a = range(10)
    for i in a:
        my_list_2.append('!')
    return my_list_2

def order_list_2():
    my_list_2 = list('Hello World!')
    a = range(10)
    for i in a:
        my_list_2.pop()
    return my_list_2

def order_list_3():
    my_list_2 = list('Hello World!')
    a = range(10)
    for i in a:
        my_list_2.extend('Stop WAR!')
    return my_list_2



#print(deque_list())
#print(order_list())
#print(deque_list_2())
#print(order_list_2())
#print(deque_list_3())
#print(order_list_3())

print(f'DEQUE - ', timeit("deque_list()", globals=globals()))
print(f'Обычный list -' ,timeit("order_list()", globals=globals()))
print(f'DEQUE - ', timeit("deque_list_2()", globals=globals()))
print(f'Обычный list - ' ,timeit("order_list_2()", globals=globals()))
print(f'DEQUE - ', timeit("deque_list_3()", globals=globals()))
print(f'Обычный list - ' ,timeit("order_list_3()", globals=globals()))

def deque_list_4():
    my_list_1 = list('Hello World!')
    deq_list = deque(my_list_1)
    a = range(10)
    for i in a:
        deq_list.appendleft('!')
    return deq_list

def order_list_4():
    my_list_2 = list('Hello World!')
    a = range(10)
    for i in a:
        my_list_2.insert(0,'!')
    return my_list_2

#print(deque_list_4())
#print(order_list_4())

print(f'DEQUE - ', timeit("deque_list_4()", globals=globals()))
print(f'Обычный list - ' ,timeit("order_list_4()", globals=globals()))

def deque_list_5():
    my_list_1 = list('Hello World!')
    deq_list = deque(my_list_1)
    a = range(10)
    for i in a:
        deq_list.popleft()
    return deq_list

def order_list_5():
    my_list_2 = list('Hello World!')
    a = range(10)
    for i in a:
        my_list_2.pop(0)
    return my_list_2

#print(deque_list_5())
#print(order_list_5())

print(f'DEQUE - ', timeit("deque_list_5()", globals=globals()))
print(f'Обычный list - ' ,timeit("order_list_5()", globals=globals()))

def deque_list_6():
    my_list_1 = list('Hello World!')
    deq_list = deque(my_list_1)
    a = range(10)
    for i in a:
        deq_list.extendleft('!RAW POTS')
    return deq_list

def order_list_6():

    my_list_2 = list('Hello World!')
    a = range(10)
    for i in a:
        my_list_2.insert(0, list('Stop WAR!'))
    return my_list_2

#print(deque_list_6())
#print(order_list_6())

print(f'DEQUE - ', timeit("deque_list_6()", globals=globals()))
print(f'Обычный list - ' ,timeit("order_list_6()", globals=globals()))

def deque_list_7():
    my_list_1 = list('Hello World!')
    deq_list = deque(my_list_1)
    a = range(10)
    for i in a:
        x = deq_list[3]
    return x

def order_list_7():

    my_list_2 = list('Hello World!')
    a = range(10)
    for i in a:
        x = my_list_2[3]
    return x

print(f'DEQUE - ', timeit("deque_list_7()", globals=globals()))
print(f'Обычный list - ' ,timeit("order_list_7()", globals=globals()))


# Итог:
# .append результат deque мелденее, чем list
# .pop результат deque быстрее, чем list
# .extend результат deque мелденее, чем list
# .appendleft результат deque быстрее, чем list
# .popleft результат deque быстрее, чем list
# .extendleft результат deque быстрее, чем list (в два раза)
# .получение элемента deque работает медленнее, чем list