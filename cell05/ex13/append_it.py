import sys
args = sys.argv[1:]
if len(args) != 0:
    for i in args:
        if i.endswith("ism"):
            continue
        else:
            print(f"{i}ism")
else:
    print(f"none")