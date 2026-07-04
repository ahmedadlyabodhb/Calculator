print("=== AI Calculator v1.0 by Ahmed ===")
num1 = float(input("Enter first number: "))
op = input("Enter operation + - * / : ")
num2 = float(input("Enter second number: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

print("Result =", result)