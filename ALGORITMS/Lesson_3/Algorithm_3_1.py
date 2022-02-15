import time

def calc_time(func):
    def wrapper(lengh):
        start = time.time()
        func(lengh)
        end = time.time()
        print("time: ",end - start)
    return wrapper

"""
Задание 1.
Реализуйте функции:
a) заполнение списка, оцените сложность в O-нотации
   заполнение словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени"""

@calc_time
def append_to_array(n): ### O(N)
    result = [i for i in range(n)]
    print("Array with len {0} create".format(str(n)))

@calc_time
def append_to_dict(n): #### O(1)
    result = {x: y for x, y in zip(range(n), range(n))}
    print("Dictionary with len {0} create".format(str(n)))

append_to_array(40)
append_to_dict(40)

array = [1,2,3,4,5,6,7]
my_dict = {1:1,2:2,3:3,4:4,5:5,6:6,7:7}

"""
b) получение элемента списка, оцените сложность в O-нотации
   получение элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
"""

@calc_time
def get_element_from_array(n): ### O(1)
    print("Value element witn index {0}: {1} in array".format(str(n),str(array[n])))

@calc_time
def get_element_from_dict(n): ### O(1)
    print("Value element witn key {0}: {1} in dict".format(str(n),str(my_dict[n])))


get_element_from_array(3)
get_element_from_dict(3)

"""
с) удаление элемента списка, оцените сложность в O-нотации
   удаление элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
"""

@calc_time
def delete_element_from_array(n):   ### O(N)
    array.pop(n)
    print("Delete element witn index {0} from array".format(str(n)))

@calc_time
def get_element_from_dict(n): ### O(1)
    del my_dict[n]
    print("Delete element witn key {0} from array".format(str(n)))

delete_element_from_array(3)
get_element_from_dict(3)