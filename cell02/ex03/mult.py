print(f"Enter the first number:")
number1 = int(input())
print(f"Enter the second number:")
number2 = int(input())
result = number1 * number2
print(f"{number1} x {number2} = {result}")
if result > 0:
    print(f"The result is positive.")
elif result < 0:
    print(f"The result is negative.")
else:
    print(f"The result is positive and negative.")