data = open("data.txt", "r").read()

print(len(max(data.split("XZZY"), key=len)))
