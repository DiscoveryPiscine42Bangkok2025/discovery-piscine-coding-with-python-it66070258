list = [2, 8, 9, 48, 8, 22,-12, 2]
new = set()
for i in list:
    if i+2 > 5:
        new.add(i+2)
print(f"Original array: {list}")
print(f"New array: {new}")