"""Домашнее задание 6 урока из курса основ.  """

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

@decor
def first_try():
    with open('find_logs.txt', 'r', encoding="utf-8") as f:
        remote_list = [line[:line.find(' ')] for line in f]

    list_max = max(set(remote_list), key=remote_list.count)
    print(list_max,remote_list.count(list_max))

#Выполнение memory_usage: 0.16015625 Mib

@decor
def second_try():
    result = dict()

    with open("find_logs.txt") as f:
        for i in f:
            addr = i.split(" ")[0]
            if addr not in result:
                result[addr] = 1
            else:
                result[addr] += 1

    print(result)
    result_addr = ""
    max = 0

    for addr in result:
        if result[addr] > max:
            result_addr = addr
            max = result[addr]


    print(result_addr)

#Выполнение memory_usage: 0.234375 Mib

first_try()

second_try()
# Профилирование по памяти profile показывает, что второе решение более выигрышное.
# Выполнение memory_usage first_try() в два раза меньше second_try()