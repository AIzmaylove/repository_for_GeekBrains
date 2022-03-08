import numpy
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
def my_func():
    arr = [i for i in range(1, 1000000, 2)]
    return arr

#Profile - 51.8 Mib
#memory_usage: 20.19921875 Mib

@decor
def my_func_2():
    arr = numpy.arange(1, 1000000, 2)
    return arr

#Profile - 34.5 Mib
#memory_usage: 1.91015625 Mib

my_func()
my_func_2()

