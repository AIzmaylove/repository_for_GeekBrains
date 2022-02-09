
# O(N)
def find_min_n(arg):
    result = arg[0]
    for i in arg:
        if i < result:
            result = i
    return result


# O(N^2)
def find_min_n2(arg):
    for i in range(0, len(arg) - 1):
        for j in range(i + 1, len(arg)):
            if arg[j] < arg[i]:
                arg[i], arg[j] = arg[j], arg[i]
    return arg[0]
