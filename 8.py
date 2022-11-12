from itertools import permutations

count = 0

for x in permutations(list("МАТВЕЙ")):
    l = list(x)

    if not (l[0] == "Й" or "АЕ" in "".join(l)):
        count += 1

print(count)
