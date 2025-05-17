# Function to add two numbers
def add(a, b):
    return a + b

# Function to find the square of a number
def square(n):
    return n * n

# Function to check if a number is even or odd
def is_even(n):
    return n % 2 == 0

# Main Program 
print("Function Implementation Example:\n")

# Using add function with user input
x = int(input("Enter first number for addition: "))
y = int(input("Enter second number for addition: "))
print(f"Addition of {x} and {y} is: {add(x, y)}\n")

# Using square function with user input
num = int(input("Enter a number to find its square: "))
print(f"Square of {num} is: {square(num)}\n")

# Using is_even function with user input
check_num = int(input("Enter a number to check even or odd: "))
if is_even(check_num):
    print(f"{check_num} is Even")
else:
    print(f"{check_num} is Odd")
