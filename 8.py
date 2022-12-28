from itertools import product

s = ["М", "Т", "Р"]
i = 0

for x in product("МЕТРО", repeat=4):
    l = list(x)

    if (l[0] in s) and not (l[3] in s):
        i += 1

print(i)
