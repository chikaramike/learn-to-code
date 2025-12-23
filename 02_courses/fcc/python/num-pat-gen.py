# Build a Number Pattern Generator

#You should define a function named number_pattern that takes a single parameter n (representing a positive integer).

#number_pattern should use a for loop.

#number_pattern(n) should return a string with all the integers starting from 1 up to n (included) separated by a space. For example, number_pattern(4) should return the string 1 2 3 4.

#If the argument passed to the function is not an integer value, the function should return Argument must be an integer value..

#If the argument passed to the function is less than 1, the function should return Argument must be an integer greater than 0..


        

def number_pattern(n):
    """
    Generates a string of numbers from 1 to n, separated by spaces.

    Args:
        n: A positive integer.

    Returns:
        A string containing numbers from 1 to n separated by spaces,
        or an error message if the input is invalid.
    """
    # 1. Input validation: Check if n is an integer
    if not isinstance(n, int):
        return "Argument must be an integer value."

    # 2. Input validation: Check if n is greater than 0
    if n < 1:
        return "Argument must be an integer greater than 0."

    # 3. Core logic: Use a for loop to build the string
    numbers = []
    for i in range(1, n + 1):  # Loop from 1 up to n (inclusive)
        numbers.append(str(i))  # Convert each number to string and add to list

    # 4. Join the list of strings with a space
    return " ".join(numbers)

# --- Test cases ---
print(f"number_pattern(4): {number_pattern(4)}")  # Expected: 1 2 3 4
print(f"number_pattern(1): {number_pattern(1)}")  # Expected: 1
print(f"number_pattern(10): {number_pattern(10)}") # Expected: 1 2 3 4 5 6 7 8 9 10
print(f"number_pattern(0): {number_pattern(0)}")  # Expected: Argument must be an integer greater than 0.
print(f"number_pattern(-5): {number_pattern(-5)}") # Expected: Argument must be an integer greater than 0.
print(f"number_pattern(3.14): {number_pattern(3.14)}") # Expected: Argument must be an integer value.
print(f"number_pattern('hello'): {number_pattern('hello')}") # Expected: Argument must be an integer value.
