number = int(input())
exeption_1 = [2,3,4]
exeption_2 = [11,12,13,14]
if number % 100 in exeption_2:
    print(number, " процентов")
elif number % 10 == 1:
    print(number," процент")
elif number % 10 in exeption_1:
    print(number, " процента")
else:
    print(number, " процентов")


