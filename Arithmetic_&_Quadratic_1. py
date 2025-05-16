import math

# Arithmetic Operations 
def arithmetic_operations(a, b):
    print("Arithmetic Operations:")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b if b != 0 else 'Undefined (division by zero)'}\n")


# Quadratic Equation Solver 
# Equation format: ax^2 + bx + c = 0
def solve_quadratic(a, b, c):
    print("Solving Quadratic Equation:")
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
# Input values
a1 = 10
b1 = 5

# Arithmetic operations
arithmetic_operations(a1, b1)

# Quadratic equation: ax² + bx + c = 0
a2, b2, c2 = 1, -3, 2  # This will give real roots 2 and 1
solve_quadratic(a2, b2, c2)
