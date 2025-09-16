import sys
args = sys.argv[1:]
text = str(input(f"What was the parameter? "))
if len(args) == 1:
    if args[0] == text:
        print(f"Good job!")
    else:
        print(f"Nope, sorry...")
else:
    print(f"none")