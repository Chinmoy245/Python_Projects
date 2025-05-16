import numpy as np

#  Linear Equations in Two Variables 
# Equations: a1x + b1y = c1 and a2x + b2y = c2
def solve_two_variable_linear(a1, b1, c1, a2, b2, c2):
    print("Solving Linear Equations (Two Variables):")
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
# Example: 2x + 3y = 13 and 3x + 2y = 12
a1, b1, c1 = 2, 3, 13
a2, b2, c2 = 3, 2, 12
solve_two_variable_linear(a1, b1, c1, a2, b2, c2)
