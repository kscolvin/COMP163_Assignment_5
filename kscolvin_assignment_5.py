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

print(f"Sequence starting from {n}: ", end="") 

while n != 1:                                       # While loop because we don't know how many steps it will take to reach 1

    print(n, end=" ")
    steps += 1

    if n % 2 == 0:                                  # If n is even, divide it by 2
        n = n // 2
    else:                                           # If n is odd, multiply it by 3 and add 1
        n = 3 * n + 1

steps += 1                                          # Increment step count for each iteration
print(f"Total steps taken: {steps}")                # Output the total number of steps taken to reach 1

# ========================================

# ========================================
# Step 2: For Loop - Prime Number Checker


# ========================================

# ========================================
# Step 3: Nested Loops - Multiplication Table Grid


# ========================================

# ========================================
# Step 4: Integration Challenge - Statistics Dashboard


# ========================================