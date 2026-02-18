"""
COMP 163 - Introduction to Programming
Assignment: Chapter 5 - Loop Mastery
Name: Kennedi S Colvin
GitHub Username: kscolvin
Date: Febuary 19 2026
Description: Program that demonstrates understanding of loops and previous concepts.
AI Usage: AI will be used to explain loop concepts and provide code examples, but all code will be written by me. 
"""


# ========================================
# Step 1: Collatz Sequence Generator

n = int(input("Enter a number to begin with: "))    # User input for starting number
steps = 0
max_steps = 1000                                    # Set a maximum step limit to prevent infinite loops
if n <= 0:                                          # Check for valid input      
    print("Please enter a positive integer.")
    exit()

print(f"Sequence starting from {n}: ", end="") 

while n != 1:                                       # While loop because we don't know how many steps it will take to reach 1
    print(n, end=" ")

    if steps >= max_steps:                          # Check if step limit is reached to prevent infinite loops
        print("\nMaximum steps exceeded.")
        break
    
    if n % 2 == 0:                                  # If n is even, divide it by 2
        n = n // 2
    else:                                           # If n is odd, multiply it by 3 and add 1
        n = 3 * n + 1
    
    steps += 1                                      # Increment step count for each iteration
if n == 1:
    print(n)                                        # Print the final value of 1 if reached
    print(f"Total steps taken: {steps}")            # Output the total number of steps taken to reach 1

# ========================================


# ========================================
# Step 2: For Loop - Prime Number Checker

n = int(input("Enter a number: "))

is_prime = True
first_divisor = 0

print(f"Checking if {n} is a prime number...")

def is_prime(n):                                    # Function to check if a number is prime
    if n < 2:
        return False
    for i in range(2, n):                           # Loop through numbers from 2 to n-1 to check for divisibility
        if n % i == 0:
            return False
    return True

if is_prime(n):
    print(f"{n} is a prime number!")                # Output whether the number is prime or not
else:
    print(f"{n} is not a prime number.")            # Output whether the number is prime or not

# ========================================


# ========================================
# Step 3: Nested Loops - Multiplication Table Grid

print("Multiplication Table (1-10):")               # Print header for the multiplication table

print("    ", end="")                               # Print initial spacing for the top row
for col in range(1, 11):                            # Print the top row of numbers
    print(f"{col:4}", end="")
print()                                             # New line after the top row

for row in range(1, 11):                            # Loop through each row
    print(f"{row:4}", end="")                       # Print the row number at the beginning of each row
    
    for col in range(1, 11):                        # Loop through each column in the current row
        product = row * col
        print(f"{product:4}", end="")               # Print the product with spacing
    print()                             
    
# ========================================


# ========================================
# Step 4: Integration Challenge - Statistics Dashboard


# ========================================

