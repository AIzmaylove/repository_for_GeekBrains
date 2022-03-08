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
def my_func(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr

#memory_usage: 1.98046875 Mib
#Profile - 25.7 Mib

@decor
def my_func_2(n):
    new_list = filter(lambda x: x % 2 == 0, range(len(n)))
    return new_list

#memory_usage: 0.0 Mib
#Profile - 24.3 Mib

a = list(range(100000))
my_func(a)
my_func_2(a)