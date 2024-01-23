# Here we can also use num1 = int(input("Enter First Number: "))
# But here we "float" due to if user wants to enter a decimal value.....
operation = {"+", "-", "*", "/"}
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
Operation = input("Enter operation (+, -, *, /): ")

if Operation in operation:
    if Operation == '+':
        result = num1 + num2
    elif Operation == '-':
        result = num1 - num2
    elif Operation == '*':
        result = num1 * num2
    elif Operation == '/':
        result = num1 / num2
    else:
        print("Invalid operation entered")
else:
    print("Invalid operation entered")

print(f"The result of the operation is {result}")
