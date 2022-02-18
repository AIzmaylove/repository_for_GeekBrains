from timeit import timeit

nums = [1,2,3,4,5,6,7,8,9,10,11,12]
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


print(func_1(nums))
print(func2(nums))
#Вызов исходной функции 3 раза
print(timeit("func_1(nums)", globals=globals()))
print(timeit("func_1(nums)", globals=globals()))
print(timeit("func_1(nums)", globals=globals()))
#Вызов получившейся функции 3 раза
print(timeit("func2(nums)", globals=globals()))
print(timeit("func2(nums)", globals=globals()))
print(timeit("func2(nums)", globals=globals()))