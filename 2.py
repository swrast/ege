bools = [True, False]

print("x y z w")

for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                if (x or y) and (not (y == z)) and (not w):
                    print(int(x), int(y), int(z), int(w))
