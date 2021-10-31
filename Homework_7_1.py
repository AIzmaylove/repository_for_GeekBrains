import os

folder = os.path.join('my_project', 'part_1', '../part_2', '../part_3','../part_4')

if not os.path.exists(folder):
    os.makedirs(folder)

