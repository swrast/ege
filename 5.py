def f(n):
    num = bin(n)[2:]
    return int(num + ("1" if num.count("1") > num.count("0") else "0"), 2)

for x in range(0, 100):
    r = f(x)

    if r > 80:
        print(r)
