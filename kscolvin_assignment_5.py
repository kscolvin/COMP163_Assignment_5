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
numbers = []
total = 0
count = 0
min_val = None
max_val = None

while True:
    num = int(input("Enter a number: "))
    if num == -1:
        break
    
    numbers.append(num)
    total += num
    count += 1
    
    if min_val is None or num < min_val:
        min_val = num
    if max_val is None or num > max_val:
        max_val = num

average = total / count if count > 0 else 0


# Part B
print("\n=== Statistics ===")
if count > 0:                                       # Check if any numbers were entered to avoid division by zero
    average = total / count                         # Calculate the average
    print(f"Count: {count}")
    print(f"Sum: {total}")
    print(f"Average: {average:.1f}")                
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
else:
    print("No data was entered.")


# Part C
print("=== Bar Chart ===")

for num in numbers:                                # Loop through the list of numbers to print a bar chart
    print(f"{num}: {'*' * num}")                   # Print the number followed by a bar of asterisks corresponding to its value

else:
    print("No data to display.")                    # If no numbers were entered, inform the user that there is no data to display

# ========================================

