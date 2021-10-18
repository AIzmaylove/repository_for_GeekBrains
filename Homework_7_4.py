import os

folder = r'C:\Users\user\PycharmProjects\GeekBrains'

size_threshold = 100
size_threshold_2 = 1000
size_threshold_3 = 10000

my_dirs = {item
          for item in os.listdir(folder)
          if os.stat(os.path.join(folder, item)).st_size > size_threshold}
my_dirs_2 = {item
          for item in os.listdir(folder)
          if os.stat(os.path.join(folder, item)).st_size > size_threshold_2}
my_dirs_3 = {item
          for item in os.listdir(folder)
          if os.stat(os.path.join(folder, item)).st_size > size_threshold_3}

result = {keys: values for keys, values in ((size_threshold, len(my_dirs)), \
                                            (size_threshold_2,len(my_dirs_2)), \
                                            (size_threshold_3, len(my_dirs_3)))}
print(result)