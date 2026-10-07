"""Find the integer that appears an odd number of times.

Given a list of integers, exactly one integer appears an odd number of times.
Return that integer.

Examples:
    [7] -> 7
    [0] -> 0
    [1, 1, 2] -> 2
    [0, 1, 0, 1, 0] -> 0
    [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1] -> 4
"""


def find_it(seq):
    counts = {}
    # Phase 1: build the frequency dictionary
    for num in seq:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Phase 2: return the integer whose count is odd
    for num, count in counts.items():
        if count % 2 != 0:
            return num

    return None
