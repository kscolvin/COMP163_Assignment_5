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

its_prime = True
first_divisor = 0

print(f"Checking if {n} is a prime number...")

for divisor in range(2, n):                         # Loop through numbers from 2 to n-1 to check for divisibility
    if n % divisor == 0:                            # If n is divisible by any number in this range, it's not prime
        its_prime = False                           # for loop is appropriate here because we know the number of iterations (n-2)
        first_divisor = divisor
        break

if its_prime:
    print(f"{n} is prime!")                         # If the loop completes without finding a divisor, n is prime
else:
    print(f"{n} is not prime number. It is divisible by {first_divisor}.")

# ========================================


# ========================================
# Step 3: Nested Loops - Multiplication Table

print("\nMultiplication Table (1-10):")             # Print a header for the multiplication table

for row in range(1, 11):                            # Loop through numbers 1 to 10 for the rows of the multiplication table
   
    for col in range(1, 11):                        # Inner loop for columns (1-10) to calculate the product of row and column
        product = row * col
        print(f"{product:4}", end="") 

    print()  

# ========================================


# ========================================
# Step 4: Integration Challenge - Statistics Dashboard


# Part A
numbers = []                                        # Initialize an empty list to store user-entered numbers
total_sum = 0
count = 0

print("=== Statistics Dashboard ===")
print("Enter number. Type '-1' to finish.")

while True:                                         # Loop to continuously accept user input until 'done' is entered
    try:
        val = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if val == -1:
        break

    if val < 0:
        print("Please enter a non-negative integer.")
        continue

numbers.append(val)                                 # Add valid input to the list

total_sum += val                                    # Update the total sum with the new value
count += 1                                          # Increment the count of numbers entered

if minimum is None or val < minimum:                # Update minimum if the current value is smaller
    minimum = val
if maximum is None or val > maximum:                # Update maximum if the current value is larger
    maximum = val


# Part B
print("\n=== Statistics ===")

if count > 0:
    average = total_sum / count

    stats = [f"Count: {count}", f"Sum: {total_sum}", f"Average: {average:.1f}", f"Minimum: {minimum}", f"Maximum: {maximum}"]

    for stat in stats:                              # Loop through the list of statistics and print each one
        print(stat)


# Part C
print("\n=== Bar Chart ===")

for num in numbers:
    print(f"{num:2}: ", end="")

    for _ in range(num):                            # Inner loop to print * corresponding to the value of num
        print("*", end="")
    print()                                      
else:
    print("No numbers were entered.")

# ========================================

