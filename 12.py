data = "9" * 1000

while "999" in data or "888" in data:
    if "888" in data:
        data = data.replace("888", "9", 1)
    else:
        data = data.replace("999", "8", 1)

print(data)
