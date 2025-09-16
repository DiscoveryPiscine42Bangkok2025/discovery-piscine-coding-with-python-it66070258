text = str(input())
result = ""
for i in text:
    if i == i.lower():
        result += i.upper()
    else:
        result += i.lower()
print(f"{result}")