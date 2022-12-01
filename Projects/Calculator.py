num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if operator == "+": # addition
    print(num1 + num2)
elif operator == "/": # divison
    print(num1 / num2)
elif operator == "-": # subtraction
    print(num1 - num2)
elif operator == "*": # multiplication
    print(num1 * num2)
else:
    print("Invaid operator.") # error message if invalid operator entered