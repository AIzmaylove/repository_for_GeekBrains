import itertools
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Станислав'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б',
]

# result = zip(tutors, klasses)
# print(*result)

result = itertools.zip_longest(tutors, klasses)
print(*result)
