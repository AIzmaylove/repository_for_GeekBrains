"""Вариант решения , в котром числа после возыедения в степень переводим
в строки(str)"""
# result = []
#
# for num in range(1,1002,2):
#     tmp_int = [int(j) for j in str(num**3)]
#     if sum(tmp_int) % 7 == 0:
#         result.append(num)
# print(result)


"""Вариант с использованием арифметических операций"""
input = [i**3+17 for i in range(1,1001,2)]
output = 0

for x in input:
    canon = x
    res = []
    counter = 10

    while True:
        remainder = x % counter
        res.append(remainder // (counter // 10))
        x = x - remainder
        counter = counter * 10
        if counter > x:
            remainder = x % counter
            res.append(remainder // (counter // 10))
            break

    result = 0
    for i in res:
        result += i
    if result % 7 == 0:
        output += canon
print(output)
