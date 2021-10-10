n = int(input('Число: '))
nums = (num for num in range(1, n + 1, 2))

print(*nums)
