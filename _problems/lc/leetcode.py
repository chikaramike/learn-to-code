def shuffle_array(nums):
    # Input validation (optional, but good practice if not guaranteed 2n)
    if not isinstance(nums, list) or len(nums) % 2 != 0:
        return "Input must be a list with an even number of elements."

    length = len(nums)
    half = length // 2 # Use integer division //

    left = nums[0:half]   # First half
    right = nums[half:length] # Second half

    shuffled_result = [] # Initialize the list to store the shuffled elements, OUTSIDE the loop

    # The loop should iterate 'half' times, because 'left' and 'right'
    # each contain 'half' elements.
    for i in range(half): # i will go from 0 to half-1
        shuffled_result.append(left[i])  # Add element from the first half
        shuffled_result.append(right[i]) # Add element from the second half

    return shuffled_result

# Your test case:
nums = [1,2,3,4,5,6]
print(f"Original: {nums}")
print(f"Shuffled: {shuffle_array(nums)}") # Expected: [1, 4, 2, 5, 3, 6]

# Another test case:
nums2 = [2,5,1,3,4,7]
print(f"Original: {nums2}")
print(f"Shuffled: {shuffle_array(nums2)}") # Expected: [2, 3, 5, 4, 1, 7]

nums3 = [1, 1, 2, 2]
print(f"Original: {nums3}")
print(f"Shuffled: {shuffle_array(nums3)}") # Expected: [1, 2, 1, 2]
