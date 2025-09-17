import sys

def downcase_it(args = sys.argv[1:]):
    if len(args) == 0:
        print(f"none")
    else:
        for i in args:
            print(f"{i.lower()}")

downcase_it()