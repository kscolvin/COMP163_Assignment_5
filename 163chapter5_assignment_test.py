"""
COMP 163 - Chapter 5 Assignment Test Suite
Automated tests for Loop Mastery assignment

This file contains all automated tests for the four-step loop assignment.
Tests are designed to provide helpful feedback without giving away solutions.
"""

import pytest
import subprocess
import sys
import os
import re
from io import StringIO


# ============================================================================
# Helper Functions
# ============================================================================

def run_python_file(filename, input_data=""):
    """
    Run a Python file with given input and capture output.
    Returns (stdout, stderr, returncode)
    """
    try:
        process = subprocess.run(
            [sys.executable, filename],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=5
        )
        return process.stdout, process.stderr, process.returncode
    except subprocess.TimeoutExpired:
        pytest.fail("Program took too long to run (infinite loop?)")
    except FileNotFoundError:
        pytest.fail(f"Could not find file: {filename}")


def find_student_file():
    """Find the student's Python file in the current directory."""
    # Look for files matching pattern: *_assignment_5.py
    for filename in os.listdir('.'):
        if filename.endswith('_assignment_5.py') and not filename.startswith('test_'):
            return filename
    
    pytest.fail(
        "Could not find your assignment file!\n"
        "Make sure your file is named: [username]_assignment_5.py\n"
        "Example: jsmith_assignment_5.py"
    )


def check_header_and_comments(filename):
    """Check if file has required header and meaningful comments."""
    with open(filename, 'r') as f:
        content = f.read()
    
    # Check for header docstring
    has_header = '"""' in content and 'COMP 163' in content
    
    # Check for comments (at least 10 comment lines)
    comment_lines = [line for line in content.split('\n') if line.strip().startswith('#')]
    has_sufficient_comments = len(comment_lines) >= 10
    
    # Check for section markers
    has_sections = '# ========' in content or '# Step 1' in content
    
    return has_header, has_sufficient_comments, has_sections


# ============================================================================
# Test 0: File Structure and Requirements
# ============================================================================

def test_00_file_exists():
    """Test that the student's Python file exists with correct naming."""
    filename = find_student_file()
    assert filename.endswith('_assignment_5.py'), (
        f"File should be named [username]_assignment_5.py, found: {filename}"
    )


def test_00_header_exists():
    """Test that required header docstring is present."""
    filename = find_student_file()
    has_header, _, _ = check_header_and_comments(filename)
    
    assert has_header, (
        "❌ MISSING REQUIRED HEADER!\n"
        "Your file must start with a docstring containing:\n"
        "- COMP 163 course info\n"
        "- Your name and GitHub username\n"
        "- Assignment description\n"
        "- AI usage statement\n\n"
        "⚠️  Missing header = 0 for entire assignment!\n"
        "See assignment instructions for the required header format."
    )


def test_00_comments_exist():
    """Test that file has sufficient meaningful comments."""
    filename = find_student_file()
    _, has_comments, has_sections = check_header_and_comments(filename)
    
    assert has_comments, (
        "❌ INSUFFICIENT COMMENTS!\n"
        "Your code must have meaningful comments explaining:\n"
        "- Section markers for each step\n"
        "- Logic explanations (WHY, not just WHAT)\n"
        "- Loop type justifications\n\n"
        "⚠️  No meaningful comments = 0 for entire assignment!\n"
        "Found fewer than 10 comment lines. Add more explanatory comments."
    )
    
    assert has_sections, (
        "❌ MISSING SECTION MARKERS!\n"
        "Your code should have clear section comments like:\n"
        "# ========================================\n"
        "# Step 1: Collatz Sequence Generator\n"
        "# ========================================\n\n"
        "This helps organize your code and shows which part does what."
    )


# Note: Advanced concept checking removed - TAs will check manually during grading


# ============================================================================
# Step 1: Collatz Sequence Tests
# ============================================================================

def test_01_collatz_basic():
    """Test Collatz sequence with a simple starting number (13)."""
    filename = find_student_file()
    
    # We'll create a test version that just tests Step 1
    # For a complete assignment, we need to handle multi-step programs
    # For now, assume the student's program does all steps sequentially
    # and we test by examining the full output
    
    # This is a simplified test - in practice, you might want to restructure
    # the assignment so each step is in a separate function or file
    
    # For this test, we'll just check if output contains expected sequence
    stdout, stderr, returncode = run_python_file(filename, "13\n")
    
    # Check for the expected sequence
    expected_numbers = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    
    # Check if all numbers appear in sequence in the output
    found_sequence = all(str(num) in stdout for num in expected_numbers)
    
    assert found_sequence, (
        "❌ test_01_collatz_basic FAILED\n"
        f"Expected output to contain the Collatz sequence starting with 13\n"
        f"Expected sequence: 13 40 20 10 5 16 8 4 2 1\n"
        f"Your output:\n{stdout[:200]}\n\n"
        "Hint: Make sure you're:\n"
        "- Using a while loop to continue until number reaches 1\n"
        "- Printing each number in the sequence\n"
        "- Dividing by 2 when even, multiplying by 3 and adding 1 when odd"
    )
    
    # Check for step count
    assert "9" in stdout or "Steps: 9" in stdout or "steps: 9" in stdout.lower(), (
        "❌ Step count incorrect for Collatz sequence\n"
        f"Expected step count: 9\n"
        "Hint: Make sure you're counting the number of transformations,\n"
        "not counting the starting number as a step."
    )


def test_02_collatz_complex():
    """Test Collatz sequence with a more complex starting number (27)."""
    filename = find_student_file()
    stdout, stderr, returncode = run_python_file(filename, "27\n")
    
    # The sequence for 27 is quite long (111 steps)
    # Just check for some key numbers in the sequence
    key_numbers = [27, 82, 41, 124, 62, 31, 94]
    
    found_numbers = sum(1 for num in key_numbers if str(num) in stdout)
    
    assert found_numbers >= 5, (
        "❌ test_02_collatz_complex FAILED\n"
        f"Expected output to contain the Collatz sequence starting with 27\n"
        f"Should include numbers like: {key_numbers}\n\n"
        "Hint: Make sure your while loop continues until the number reaches 1,\n"
        "and that you're correctly applying the Collatz rules for even/odd numbers."
    )


def test_03_collatz_single_step():
    """Test Collatz sequence with number that needs only one step (2)."""
    filename = find_student_file()
    stdout, stderr, returncode = run_python_file(filename, "2\n")
    
    # Sequence for 2 should be: 2 1 (one step)
    assert "2" in stdout and "1" in stdout, (
        "❌ test_03_collatz_single_step FAILED\n"
        "Expected output to show sequence: 2 1\n\n"
        "Hint: Make sure your loop works correctly for edge cases.\n"
        "Even numbers should be divided by 2."
    )
    
    # Check that step count is 1
    # Look for "1" appearing after "Steps" or "steps"
    step_check = "Steps: 1" in stdout or "steps: 1" in stdout.lower() or "Step: 1" in stdout
    
    assert step_check or stdout.count("1") >= 2, (
        "❌ Step count may be incorrect\n"
        "For starting number 2, there should be exactly 1 step\n"
        "Hint: Count how many times you transform the number, not how many numbers total."
    )


# ============================================================================
# Step 2: Prime Number Tests  
# ============================================================================

def test_04_prime_is_prime_small():
    """Test prime checker with a small prime number (7)."""
    filename = find_student_file()
    
    # Skip Collatz input, provide prime input
    # This assumes the program runs steps sequentially
    # You may need to adjust based on actual implementation
    stdout, stderr, returncode = run_python_file(filename, "13\n7\n")
    
    # Check for prime confirmation
    prime_indicators = ["is prime", "prime!", "Prime"]
    found_prime = any(indicator in stdout for indicator in prime_indicators)
    
    assert found_prime, (
        "❌ test_04_prime_is_prime_small FAILED\n"
        "Expected output to identify 7 as prime\n"
        f"Your output:\n{stdout[:300]}\n\n"
        "Hint: A prime number has no divisors between 2 and (number-1)\n"
        "Make sure you're checking all divisors and outputting the correct message."
    )
    
    # Make sure it doesn't say "not prime"
    assert "not prime" not in stdout.lower() or stdout.lower().count("not prime") == 0, (
        "❌ 7 should be identified as prime, but your output says 'not prime'\n"
        "Hint: Check your divisibility logic - 7 is only divisible by 1 and 7."
    )


def test_05_prime_is_prime_large():
    """Test prime checker with a larger prime number (17)."""
    filename = find_student_file()
    stdout, stderr, returncode = run_python_file(filename, "13\n17\n")
    
    prime_indicators = ["is prime", "prime!", "Prime"]
    found_prime = any(indicator in stdout for indicator in prime_indicators)
    
    assert found_prime, (
        "❌ test_05_prime_is_prime_large FAILED\n"
        "Expected output to identify 17 as prime\n\n"
        "Hint: Test ALL divisors from 2 to 16\n"
        "If none divide evenly, the number is prime."
    )


def test_06_prime_not_prime():
    """Test prime checker with a composite number (15)."""
    filename = find_student_file()
    stdout, stderr, returncode = run_python_file(filename, "13\n15\n")
    
    # Check for "not prime" message
    assert "not prime" in stdout.lower(), (
        "❌ test_06_prime_not_prime FAILED\n"
        "Expected output to identify 15 as NOT prime\n\n"
        "Hint: 15 is divisible by 3 and 5, so it's not prime."
    )
    
    # Check for divisor identification (3 or 5)
    has_divisor = "3" in stdout or "5" in stdout or "divisible" in stdout.lower()
    
    assert has_divisor, (
        "❌ Should show which number 15 is divisible by\n"
        "Expected output to mention divisor (3 or 5)\n\n"
        "Hint: When you find a divisor, include it in your output message.\n"
        "Example: '15 is not prime (divisible by 3)'"
    )


def test_07_prime_not_prime_even():
    """Test prime checker with an even composite number (20)."""
    filename = find_student_file()
    stdout, stderr, returncode = run_python_file(filename, "13\n20\n")
    
    assert "not prime" in stdout.lower(), (
        "❌ test_07_prime_not_prime_even FAILED\n"
        "Expected output to identify 20 as NOT prime\n\n"
        "Hint: Even numbers (except 2) are never prime because they're divisible by 2."
    )
    
    # Should mention divisor 2
    assert "2" in stdout or "divisible" in stdout.lower(), (
        "❌ Should identify 2 as a divisor of 20\n"
        "Hint: When checking divisors starting from 2, you should find 2 divides 20."
    )


# ============================================================================
# Step 3: Multiplication Table Tests
# ============================================================================

def test_08_multiplication_table_structure():
    """Test that multiplication table has correct structure."""
    filename = find_student_file()
    # Provide inputs for previous steps + nothing for mult table
    stdout, stderr, returncode = run_python_file(filename, "13\n17\n")
    
    # Check for title
    assert "Multiplication" in stdout or "multiplication" in stdout, (
        "❌ test_08_multiplication_table_structure FAILED\n"
        "Expected to see 'Multiplication Table' title\n\n"
        "Hint: Print a title before displaying the table."
    )
    
    # Check that output has multiple lines (at least 11: title + header + 10 rows)
    lines = stdout.split('\n')
    table_lines = [line for line in lines if any(str(i) in line for i in range(1, 11))]
    
    assert len(table_lines) >= 10, (
        "❌ Multiplication table doesn't have enough rows\n"
        f"Expected at least 10 rows, found approximately {len(table_lines)}\n\n"
        "Hint: Your outer loop should go from 1 to 10 (inclusive)."
    )


def test_09_multiplication_table_calculations():
    """Test that multiplication table has correct calculations."""
    filename = find_student_file()
    stdout, stderr, returncode = run_python_file(filename, "13\n17\n")
    
    # Check for some key products
    key_products = ["100", "81", "64", "49", "36", "25", "16", "9", "4", "1"]
    found_products = sum(1 for product in key_products if product in stdout)
    
    assert found_products >= 8, (
        "❌ test_09_multiplication_table_calculations FAILED\n"
        f"Expected to find key products like: {key_products}\n"
        f"Only found {found_products} of them\n\n"
        "Hint: Make sure you're calculating row × column correctly\n"
        "and displaying all products from 1×1 to 10×10."
    )
    
    # Check for specific row pattern (e.g., row 5)
    # Should contain: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
    row_5_products = ["5", "10", "15", "20", "25", "30", "35", "40", "45", "50"]
    row_5_found = sum(1 for product in row_5_products if product in stdout)
    
    assert row_5_found >= 8, (
        "❌ Row 5 of multiplication table appears incorrect\n"
        "Expected products: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50\n\n"
        "Hint: Each row should show that row number multiplied by columns 1-10."
    )


def test_10_multiplication_table_format():
    """Test that multiplication table has reasonable formatting."""
    filename = find_student_file()
    stdout, stderr, returncode = run_python_file(filename, "13\n17\n")
    
    # Check that numbers are somewhat aligned (look for multiple spaces)
    # This is a loose check since exact formatting varies
    has_spacing = "  " in stdout  # At least double spaces somewhere
    
    assert has_spacing, (
        "❌ test_10_multiplication_table_format FAILED\n"
        "Table should have formatted spacing for alignment\n\n"
        "Hint: Use f-strings with width specifiers like f'{num:4}' to align columns.\n"
        "Example: print(f'{product:4}', end='') for each product."
    )


# ============================================================================
# Step 4: Statistics Dashboard Tests
# ============================================================================

def test_11_statistics_data_collection():
    """Test that statistics dashboard collects data correctly."""
    filename = find_student_file()
    # Provide inputs: Collatz(13), Prime(17), MultTable(none), Stats(5,12,8,15,3,-1)
    stdout, stderr, returncode = run_python_file(filename, "13\n17\n5\n12\n8\n15\n3\n-1\n")
    
    # Check for statistics section
    assert "Statistics" in stdout or "statistics" in stdout or "STATISTICS" in stdout, (
        "❌ test_11_statistics_data_collection FAILED\n"
        "Expected to see 'Statistics' section in output\n\n"
        "Hint: Add a header like '=== Statistics ===' before displaying stats."
    )
    
    # Check for count
    assert "Count" in stdout or "count" in stdout or "5" in stdout, (
        "❌ Should display count of numbers entered\n"
        "Expected count: 5\n\n"
        "Hint: Track how many numbers were entered (not counting the -1)."
    )


def test_12_statistics_calculations():
    """Test that statistics dashboard calculates correctly."""
    filename = find_student_file()
    stdout, stderr, returncode = run_python_file(filename, "13\n17\n5\n12\n8\n15\n3\n-1\n")
    
    # For inputs 5, 12, 8, 15, 3:
    # Count: 5
    # Sum: 43
    # Average: 8.6
    # Min: 3
    # Max: 15
    
    # Check for sum
    assert "43" in stdout, (
        "❌ test_12_statistics_calculations FAILED\n"
        "Expected sum: 43 (for numbers 5, 12, 8, 15, 3)\n\n"
        "Hint: Add up all the numbers as you collect them with your while loop."
    )
    
    # Check for average (8.6)
    assert "8.6" in stdout or "8.60" in stdout, (
        "❌ Average calculation incorrect\n"
        "Expected average: 8.6\n\n"
        "Hint: Average = sum / count\n"
        "Format to 1 decimal place using f'{average:.1f}'"
    )
    
    # Check for min
    assert "Minimum" in stdout or "Min" in stdout or "min" in stdout, (
        "❌ Should display minimum value\n"
        "Hint: Track the smallest number entered."
    )
    
    # Check for max
    assert "Maximum" in stdout or "Max" in stdout or "max" in stdout, (
        "❌ Should display maximum value\n"
        "Hint: Track the largest number entered."
    )


def test_13_statistics_min_max_values():
    """Test that min and max are calculated correctly."""
    filename = find_student_file()
    stdout, stderr, returncode = run_python_file(filename, "13\n17\n5\n12\n8\n15\n3\n-1\n")
    
    # Min should be 3, Max should be 15
    # Find these in the statistics section
    stats_section = stdout[stdout.lower().find("statistics"):]
    
    assert "3" in stats_section, (
        "❌ Minimum value incorrect\n"
        "Expected minimum: 3 (from numbers 5, 12, 8, 15, 3)\n\n"
        "Hint: Initialize min to the first number, then compare each new number."
    )
    
    assert "15" in stats_section, (
        "❌ Maximum value incorrect\n"
        "Expected maximum: 15 (from numbers 5, 12, 8, 15, 3)\n\n"
        "Hint: Initialize max to the first number, then compare each new number."
    )


def test_14_statistics_bar_chart():
    """Test that bar chart displays correctly."""
    filename = find_student_file()
    stdout, stderr, returncode = run_python_file(filename, "13\n17\n5\n12\n8\n15\n3\n-1\n")
    
    # Check for bar chart section
    assert "Bar Chart" in stdout or "bar chart" in stdout or "Chart" in stdout or "*" in stdout, (
        "❌ test_14_statistics_bar_chart FAILED\n"
        "Expected to see bar chart section\n\n"
        "Hint: Add a header like '=== Bar Chart ===' and use asterisks (*) to draw bars."
    )
    
    # Check for asterisks (used to draw bars)
    assert "*" in stdout, (
        "❌ Bar chart should use asterisks (*) to represent values\n\n"
        "Hint: For each number, print that many asterisks.\n"
        "Example: For number 5, print '*****'"
    )
    
    # Count asterisks - should have 5+12+8+15+3 = 43 total asterisks
    asterisk_count = stdout.count("*")
    
    assert 40 <= asterisk_count <= 50, (
        f"❌ Bar chart has incorrect number of asterisks\n"
        f"Expected approximately 43 asterisks (5+12+8+15+3)\n"
        f"Found: {asterisk_count}\n\n"
        "Hint: Use a nested loop - outer loop for each number,\n"
        "inner loop to print asterisks equal to that number's value."
    )


def test_15_statistics_multiple_loop_types():
    """Test that statistics dashboard uses all three loop types appropriately."""
    filename = find_student_file()
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Check for while loop (data collection)
    has_while = "while" in content.lower()
    assert has_while, (
        "❌ Step 4 should use a while loop for data collection\n\n"
        "Hint: Use 'while' to keep collecting numbers until user enters -1."
    )
    
    # Check for for loop  
    has_for = "for " in content.lower()
    assert has_for, (
        "❌ Step 4 should use for loops\n\n"
        "Hint: Use 'for' loops to iterate through collected numbers for calculations\n"
        "and to print the bar chart."
    )
    
    # This test just ensures both loop types are present somewhere in the code
    # The actual logic is tested in other tests


def test_16_statistics_integration():
    """Integration test with different data set."""
    filename = find_student_file()
    # Test with: 10, 20, 30, 40, 50
    # Sum: 150, Count: 5, Avg: 30.0, Min: 10, Max: 50
    stdout, stderr, returncode = run_python_file(filename, "13\n17\n10\n20\n30\n40\n50\n-1\n")
    
    # Check calculations
    checks = {
        "150": "sum",
        "30.0": "average",
        "10": "minimum",
        "50": "maximum",
        "5": "count"
    }
    
    stats_section = stdout[stdout.lower().find("statistics"):] if "statistics" in stdout.lower() else stdout
    
    missing = []
    for value, name in checks.items():
        if value not in stats_section:
            missing.append(f"{name} ({value})")
    
    assert len(missing) == 0, (
        f"❌ test_16_statistics_integration FAILED\n"
        f"Missing or incorrect values: {', '.join(missing)}\n"
        f"For inputs 10, 20, 30, 40, 50:\n"
        f"Expected - Count: 5, Sum: 150, Average: 30.0, Min: 10, Max: 50\n\n"
        "Hint: Double-check your calculation logic and formatting."
    )


# ============================================================================
# Run all tests
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
