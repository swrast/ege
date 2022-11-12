for x in range(45000000, 50000001):
    count = 0

    for k in filter(lambda v: v % 2 == 1, range(x)):
        if x % k == 0:
            count += 1

    if count == 5:
        print(x)

