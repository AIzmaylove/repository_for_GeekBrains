'''В первом задании словарь вынес за пределы, тела функции, но работет и так и так.
Здесь оставил в функции. Хотел бы узнать есть ли какая то координальная разница?'''
def num_translate_adv():
    words = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }

    chars_array = "abcdefghijklmnopqrstuvwxyz"

    x = input('Введите число от 0 до 10 на английском языке ')
    if x[0] in chars_array:
        print(words.get(x))
    else:
        print(words.get(x.lower()).title())

num_translate_adv()