def add(x, y):
    """Addition"""
    return x + y

def subtract(x, y):
    """Subtraction"""
    return x - y

def multiply(x, y):
    """multiplication"""
    return x * y

def divide(x, y):
    """Division"""
    if y != 0:
        return x / y
    else:
        return "Error, divide -0-!"

print("Choose transaction:")
print("1. Addition")
print("2. Subtraction")
print("3. multiplication")
print("4. Division")

choice = input("Add number operation (1/2/3/4): ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Incorrect input transaction")

