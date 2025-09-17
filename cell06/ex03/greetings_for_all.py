def greetings(text = ""):
    if type(text) != str:
        print(f"Error! It was not a name.")
    elif text == "":
        print(f"Hello, noble stranger.")
    else:
        print(f"Hello, {text}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)