import sys, re
args = sys.argv[1:]
if len(args) == 2:
    find = args[0]
    text = args[1]
    total = len(re.findall(find, text))
    if total == 0:
        print(f"none")
    else:
        print(f"{total}")
else:
    print(f"none")