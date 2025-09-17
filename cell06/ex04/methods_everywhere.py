import sys

agrs = sys.argv[1:]

if len(agrs) < 1:
    print(f"none")
else:
    def shrink(text):
        print(f"{text[:8]}")

    def enlarge(text):
        print(f"{text}{'Z'*(8-len(text))}")

    for i in agrs:
        if len(i) > 8:
            shrink(i)
        elif len(i) < 8:
            enlarge(i)
        else:
            print(f"{i}")
