from timeit import timeit

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    revers_num = int("".join(reversed(str(enter_num))))
    return revers_num


enter_num = 123456


#revers(enter_num)
#print(revers_2(enter_num))
#print(revers_3(enter_num))

#print(revers_4(enter_num))

print(f'функция №1 - ',timeit("revers(enter_num)", globals=globals()))
print(f'функция №2 - ',timeit("revers_2(enter_num)", globals=globals()))
print(f'функция №3 - ', timeit("revers_3(enter_num)", globals=globals()))
print(f'функция №4 - ',timeit("revers_4(enter_num)", globals=globals()))

### Функция №3 судя по замерам , выполняется быстрее всего.
### если придерживаться этого критерия , то значит эфективнее.
### думаю это достигается за счет того, что работает только встроенаая функция.
### и превосходит функцию №4 как минимум потому что в 4 таких функций больше.
