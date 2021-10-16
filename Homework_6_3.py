import json
from itertools import zip_longest

with open('people.csv', 'r', encoding='utf-8') as file_1, open('hobby.csv', 'r', encoding='utf-8') as file_2:

    people = file_1.read().splitlines()
    hobby = file_2.read().splitlines()
if len(people) < len(hobby):
    print(1)
else:
    result = dict(zip_longest(people,hobby, fillvalue=None))
    with open('people_and_their_hobby(6_3).txt', 'w',encoding='utf-8') as f:
        json.dump(result,f,ensure_ascii=False)