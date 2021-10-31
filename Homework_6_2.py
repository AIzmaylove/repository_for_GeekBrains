result = dict()

with open("find_logs.txt") as f:
    for i in f:
        addr = i.split(" ")[0]
        if addr not in result:
            result[addr] = 1
        else:
            result[addr] += 1

print(result)
result_addr = ""
max = 0

for addr in result:
    if result[addr] > max:
        result_addr = addr
        max = result[addr]


print(result_addr)

