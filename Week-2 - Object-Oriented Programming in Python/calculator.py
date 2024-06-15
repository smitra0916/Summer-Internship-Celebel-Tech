class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed"
        else:
            return a / b

calculator = Calculator()

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation: \n" \
                "1. Add\n" \
                "2. Subtract\n" \
                "3. Multiply\n" \
                "4. Divide\n" )

# Perform the operation
if operation == "1":
    print(calculator.add(num1, num2))
elif operation == "2":
    print(calculator.subtract(num1, num2))
elif operation == "3":
    print(calculator.multiply(num1, num2))
elif operation == "4":
    print(calculator.divide(num1, num2))
else:
    print("Invalid operation")