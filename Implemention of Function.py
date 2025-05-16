# Function to add two numbers
def add(a, b):
    return a + b

# Function to find the square of a number
def square(n):
    return n * n

# Function to check if a number is even or odd
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#  Main Program 
print("Function Implementation Example:\n")

# Using add function
x, y = 10, 5
print(f"Addition of {x} and {y} is: {add(x, y)}")

# Using square function
num = 6
print(f"Square of {num} is: {square(num)}")

# Using is_even function
check_num = 13
if is_even(check_num):
    print(f"{check_num} is Even")
else:
    print(f"{check_num} is Odd")
