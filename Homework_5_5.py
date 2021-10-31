src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
answer = []

tmp = [answer.append(number) for number in src if src.count(number) == 1]

print(answer)

# for number in src:
#         if src.count(number) == 1:
#             answer.append(number)
#
# print(answer)