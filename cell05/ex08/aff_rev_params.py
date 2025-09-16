import sys
args = sys.argv[1:]
if len(args) > 2:
    for i in range(1, len(args)+1):
        print(f"{args[-i]}")
else:
    print(f"none")