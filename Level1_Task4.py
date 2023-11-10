#Create a Python program that acts as a basiccalculator. It should prompt the user to enter two numbers and an operator (+, -,*, /,%), and then display the result of the operation.

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:  # Check for division by zero
            return num1 / num2
        else:
            return "Error: Division by zero"
    elif operator == '%':
        return num1 % num2
    else:
        return "Error: Invalid operator"

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /, %): ")

# Perform the calculation and display the result
result = calculate(num1, num2, operator)
print(f"Result: {result}")






