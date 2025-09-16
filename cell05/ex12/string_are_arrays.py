import sys, re
args = sys.argv[1:]
if len(args) == 1:
    if len(re.findall('z', args[0])) != 0:
        print(f"{'z' * len(re.findall('z', args[0]))}")
    else:
        print(f"none")
else:
    print(f"none")