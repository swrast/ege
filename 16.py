def f(n):
    if n == 1:
        return 1
    if n >= 2:
        return f(n - 1) * n

    raise Exception("n is not >= 2 or == 1")

print(f(6))
