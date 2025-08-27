# basic_calculator.py
# CCCS 106 - Week 1 Lab Exercise
# Simple Interactive Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Cannot perform modulus by zero"

def power(a, b):
    return a ** b

def larger(a, b):
    return max(a, b)

def smaller(a, b):
    return min(a, b)

print("=" * 40)
print("BASIC CALCULATOR")
print("=" * 40)

# Get user input
print("Enter two numbers for calculation:")
try:
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    # Perform calculations
    addition = add(num1, num2)
    subtraction = subtract(num1, num2)
    multiplication = multiply(num1, num2)
    division = divide(num1, num2)
    mod = modulus(num1, num2)
    exp = power(num1, num2)

    # Display results
    print("\n" + "=" * 40)
    print("RESULTS:")
    print("=" * 40)
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} * {num2} = {multiplication}")
    print(f"{num1} / {num2} = {division}")
    print(f"{num1} % {num2} = {mod}")
    print(f"{num1} ** {num2} = {exp}")

    # Additional information
    print(f"\nLarger number: {larger(num1, num2)}")
    print(f"Smaller number: {smaller(num1, num2)}")

except ValueError:
    print("Error: Please enter valid numbers only!")
except Exception as e:
    print(f"An error occurred: {e}")

print("\nThank you for using Basic Calculator!")