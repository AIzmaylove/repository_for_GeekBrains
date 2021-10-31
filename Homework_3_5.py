from random import choice

def get_jokes(jokes=1):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = int(input('Господин, сколько изволите шуток? '))
    joke_list = []

    for joke in range(jokes):
        joke = ' '.join([choice(nouns), choice(adverbs), choice(adjectives)])
        joke_list.append(joke)
    print(joke_list)

get_jokes()

'''Пока получилось так, хочу еще добавить момент исключения ошибки , если пользователь вводит не число
, но пока не добил эту версию.'''
