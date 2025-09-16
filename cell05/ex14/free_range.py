import sys
args = sys.argv[1:]
list = []
if len(args) == 2:
    if int(args[0]) <= int(args[1]):
        for i in range(int(args[0]), int(args[1])+1):
            list.append(i)
    else:
        for i in range(int(args[1]), int(args[0])+1):
            list.append(i)
    print(f"{list}")
else:
    print(f"none")