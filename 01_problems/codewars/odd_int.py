# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# [7] should return 7, 
#   because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).]

def find_it(seq):
    counts = {}
    # Phase 1: Build the frequency dictionary
    for num in seq:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
            
    # Phase 2: Look for the odd count
    # .items() lets us look at both the number (key) and its count (value)
    for num, count in counts.items():
        if count % 2 != 0:  # If the count is odd
            print(f'seq: {seq}, odd int: {num}')
            return num      # Return the integer immediately
            
    return None

tests = [
    [0],
    [7],
    [1,1,2],
    [0,1,0,1,0],
    [1,2,2,3,3,3,4,3,3,3,2,2,1]
]

for test in tests:
    find_it(test)