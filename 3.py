res: list[int] = []

for x in range(10, 1001):
    num = x - int(bin(x)[3:], 2)

    if num not in res:
        res.append(num)

print(len(res))
