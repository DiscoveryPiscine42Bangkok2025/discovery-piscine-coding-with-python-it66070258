import sys
args = sys.argv[1:]
if len(args) != 0:
    print(f"parameters: {len(args)}")
    for i in range(0, len(args)):
        print(f"{args[i]}: {len(args[i])}")
else:
    print(f"none")