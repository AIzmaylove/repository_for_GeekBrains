
result = []

with open("find_logs.txt") as f:
    for i in f:
        result.append((i.split(" ")[0],i.split(" ")[5],i.split(" ")[6]))


print(result)