from itertools import zip_longest

with open('people.csv', 'r', encoding='utf-8') as file_1, open('hobby.csv', 'r', encoding='utf-8') as file_2:

    people = file_1.read().splitlines()
    hobby = file_2.read().splitlines()
result = ((people, hobby) for people, hobby in zip_longest(people, hobby, fillvalue=None))

with open('people_and_their_hobby(6_4).txt', 'w',encoding='utf-8') as f:
    for i in result:
        f.write(f'{i[0]}: {i[1]}\n')