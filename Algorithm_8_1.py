"""Все идет очень тяжело. Поэтому переписывал код примера ручками, пытаясь разобраться"""

from collections import Counter, deque


class MyNode:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def tree_by_haffman(s):

    my_string_counter = Counter(s)

    sorted_str = deque(sorted(my_string_counter.items(), key=lambda item: item[1]))

    while len(sorted_str) > 1:

        weight = sorted_str[0][1] + sorted_str[1][1]
        node = MyNode(left=sorted_str.popleft()[0], right=sorted_str.popleft()[0])

        for i, item in enumerate(sorted_str):
            if weight > item[1]:
                continue
            else:
                sorted_str.insert(i, (node, weight))
                break
        else:
            sorted_str.append((node, weight))

    return sorted_str[0][0]


code_table = dict()


def my_way_code_haffman(tree, path=''):

    if not isinstance(tree, MyNode):
        code_table[tree] = path

    else:
        my_way_code_haffman(tree.left, path=f'{path}0')
        my_way_code_haffman(tree.right, path=f'{path}1')


s = "Hop hey hou!"

my_way_code_haffman(tree_by_haffman(s))

for i in s:
    print(code_table[i], end=' ')

print()
