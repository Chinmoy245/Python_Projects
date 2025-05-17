import math

# Perform selected Arithmetic Operation 
def arithmetic_operations(a, b, operation):
    print("\nArithmetic Operation:")
    if operation == '1':
        print(f"Addition: {a} + {b} = {a + b}")
    elif operation == '2':
        print(f"Subtraction: {a} - {b} = {a - b}")
    elif operation == '3':
        print(f"Multiplication: {a} * {b} = {a * b}")
    elif operation == '4':
        if b != 0:
            print(f"Division: {a} / {b} = {a / b}")
        else:
            print("Division: Undefined (division by zero)")
    else:
        print("Invalid operation choice!")

# Quadratic Equation Solver 
# Equation format: ax^2 + bx + c = 0
def solve_quadratic(a, b, c):
    print("\nSolving Quadratic Equation:")
    print(f"Equation: {a}x² + {b}x + {c} = 0")

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Two real roots: {root1:.2f} and {root2:.2f}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"One real root: {root:.2f}")
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-discriminant) / (2*a)
        print(f"Two complex roots: {real_part:.2f} + {imag_part:.2f}i and {real_part:.2f} - {imag_part:.2f}i")

# Main Code

# Arithmetic operation input
print("Arithmetic Operations Menu:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Choose an operation (1-4): ")

a1 = float(input("Enter first number (a): "))
b1 = float(input("Enter second number (b): "))

arithmetic_operations(a1, b1, choice)
# Quadratic equation input
print("\nEnter coefficients for quadratic equation ax² + bx + c = 0:")
a2 = float(input("Enter coefficient a: "))
b2 = float(input("Enter coefficient b: "))
c2 = float(input("Enter coefficient c: "))

solve_quadratic(a2, b2, c2)
