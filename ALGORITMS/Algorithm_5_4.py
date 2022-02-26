from collections import OrderedDict
from timeit import timeit

def my_hand():
    hand_dict = dict()
    hand_dict['one'] = 1
    hand_dict['three'] = 3
    hand_dict['two'] = 2
    hand_dict['four'] = 4
    hand_dict['five'] = 5
    hand_dict.popitem()
    hand_dict_2 = dict()
    hand_dict_2['девять'] = 9
    hand_dict_2['восемь'] = 8
    hand_dict_2['семь'] = 7
    hand_dict_2['шесть'] = 6
    hand_dict_2['пять'] = 5
    c_hand_dict = hand_dict.copy()
    numbers_2 = OrderedDict(девять=9, восемь=8, семь=7, шесть=6, пять=5)
    hand_dict.update(hand_dict_2)
    hand_dict.clear()
    #hand_dict.update(numbers_2) # когда добавляешь словарь OrderedDict замеры по времени незначительно увеличиваются.
    return hand_dict, c_hand_dict



def my():
    numbers = OrderedDict(one=1, three=3, two=2, four=4, five=5)
    numbers.popitem(last=True)
    numbers_2 = OrderedDict(девять=9, восемь=8, семь=7, шесть=6, пять=5)
    c_numbers = numbers.copy()
    numbers.update(numbers_2)
    numbers.clear()

    #numbers.move_to_end('one')
    return numbers , c_numbers



print(my_hand())
print(my())

print(f'Обычный словарь - ' ,timeit("my_hand()", globals=globals()))
print(f'ORDEREDDICT - ', timeit("my()", globals=globals()))


#  Пример из методички
def for_example_1():
    a = {'x':0, 'y':0}
    b = {'x':0, 'y':0}
    a['x'] = float(3)
    a['y'] = float(4)
    b['x'] = float(5)
    b['y'] = float(6)
    suma = {}
    mult = {}
    suma['x'] = a['x'] + b['x']
    suma['y'] = a['y'] + b['y']
    mult['x'] = a['x'] * b['x'] - a['y'] * b['y']
    mult['y'] = a['y'] * b['x'] + a['x'] * b['y']
    return 'Сумма:   %.2f+%.2fj' % (suma['x'], suma['y']) , 'Произв.: %.2f+%.2fj' % (mult['x'], mult['y'])


def for_example_2():
    i = OrderedDict (x=0, y=0)
    j = OrderedDict (x=0, y=0)
    i['x'] = float(3)
    i['y'] = float(4)
    j['x'] = float(5)
    j['y'] = float(6)
    suma = {}
    mult = {}
    suma['x'] = i['x'] + j['x']
    suma['y'] = i['y'] + j['y']
    mult['x'] = i['x'] * j['x'] - i['y'] * j['y']
    mult['y'] = i['y'] * j['x'] + i['x'] * j['y']
    return 'Сумма:   %.2f+%.2fj' % (suma['x'], suma['y']) , 'Произв.: %.2f+%.2fj' % (mult['x'], mult['y'])


#print(for_example_1())
#print(for_example_2())

print(f'Обычный словарь - ' ,timeit("for_example_1()", globals=globals()))
print(f'ORDEREDDICT - ', timeit("for_example_2()", globals=globals()))

#'''({}, {'one': 1, 'three': 3, 'two': 2, 'four': 4})
#(OrderedDict(), OrderedDict([('one', 1), ('three', 3), ('two', 2), ('four', 4)]))
#Обычный словарь -  2.2654069999999997
#ORDEREDDICT -  3.3761308
#Обычный словарь -  2.5739089
#ORDEREDDICT -  3.4776121999999994
#
#Process finished with exit code 0'''

# Полученные результаты показываю, что все выполненные операции с простым dict , выполняются быстрее.
# Возможно я не додумался до случая , где именно последовательность OrderedDict нужна. Но в том, что делал
# функционала более поздних версий Python хватает.
# единственное OrderedDict необходим, если хотим коллегам разработчикам сказать, что в словаре ВАЖНА последовательность
# элементов