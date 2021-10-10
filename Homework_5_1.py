# import sys
# n = int(input('Введите число: '))
# nums_gen = (num ** 2 for num in range(1, n, 2))
# print(type(nums_gen), sys.getsizeof(nums_gen))
# print(nums_gen)
# def odd_nums():
#     nums = []
#     n = int(input('Число '))
#     for num in range(1, n + 1, 2):
#         nums.append(num)
#
#         yield nums
#
# tmp = odd_nums()
# for num in tmp:
#     print(num)

#
# def letters_generator(start, end):
#    for code in range(ord(start), ord(end) + 1):
#        yield chr(code)
#
# x = letters_generator('A', 'Z')
# print(*x)

def nums_generator(max_num):
   for num in range(1, max_num + 1, 2):
       yield num

nums_gen = nums_generator(10)
print(*nums_gen)
print(type(nums_gen))

#
# def letters_generator(start, end):
#    for code in range(ord(start), ord(end) + 1):
#        yield chr(code)
#
#
# eng_uppercase_letters = letters_generator('A', 'Z')
# print(*eng_uppercase_letters, sep=' ')