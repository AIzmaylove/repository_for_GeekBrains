import collections

while True:
    try:
        n = int(input('Введите количество компаний для расчета прибыли: '))
    except ValueError:
        print('Вы ввели недопустимое значение')
        continue
    break

companies = collections.defaultdict()
c_profit = collections.deque()
c_underprofit = collections.deque()
all_profit = 0
QUARTER = 4

for i in range(n):
    name = input(f'\nВведите название {i+1}й компании: ')
    profit = 0
    q = 1
    while q <= QUARTER:
        try:
            profit += float(input(f'Введите прибыль за {q}й квартал: '))
        except ValueError:
            print('Вы ввели недопустимое значение')
            continue
        q += 1
    companies[name] = profit
    all_profit += profit

mid_profit = all_profit / n
for i, item in companies.items():
    if item >= mid_profit:
        c_profit.append(i)
    else:
        c_underprofit.append(i)
print(f'Средняя годова прибыль для всех компаний : {mid_profit}')
print(f'Прибыль выше среднего у {len(c_profit)} компаний:')
for name in c_profit:
    print(name)
print(f'Прибыль ниже среднего у {len(c_underprofit)} компаний:')
for name in c_underprofit:
    print(name)