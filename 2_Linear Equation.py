import numpy as np

# Linear Equations in Two Variables
# Equations: a1x + b1y = c1 and a2x + b2y = c2
def solve_two_variable_linear(a1, b1, c1, a2, b2, c2):
    print("\nSolving Linear Equations (Two Variables):")
    print(f"Equation 1: {a1}x + {b1}y = {c1}")
    print(f"Equation 2: {a2}x + {b2}y = {c2}")

    # Matrix representation: AX = B
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])

    # Check if determinant is non-zero
    det = np.linalg.det(A)

    if det != 0:
        solution = np.linalg.solve(A, B)
        x, y = solution
        print(f"Solution: x = {x:.2f}, y = {y:.2f}")
    else:
        print("No unique solution (Determinant is zero)")

# Main Program
print("Enter coefficients for the system of equations:")
print("Equation format: a1x + b1y = c1 and a2x + b2y = c2")

# User input
a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
c1 = float(input("Enter c1: "))

a2 = float(input("Enter a2: "))
b2 = float(input("Enter b2: "))
c2 = float(input("Enter c2: "))

# Solve the system
solve_two_variable_linear(a1, b1, c1, a2, b2, c2)
