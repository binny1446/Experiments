def two_sum(nums, target): # Akash
    """ # Akash
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. # Akash
    You may assume that each input would have exactly one solution, and you may not use the same element twice. # Akash
    You can return the answer in any order. # Akash
    """ # Akash
    num_map = {} # Akash
    for i, num in enumerate(nums): # Akash
        complement = target - num # Akash
        if complement in num_map: # Akash
            return [num_map[complement], i] # Akash
        num_map[num] = i # Akash
    return [] # Akash

# Test cases # Akash
if __name__ == "__main__": # Akash
    print(f"Test 1: {two_sum([2, 7, 11, 15], 9)}") # Expected: [0, 1] # Akash
    print(f"Test 2: {two_sum([3, 2, 4], 6)}")     # Expected: [1, 2] # Akash
    print(f"Test 3: {two_sum([3, 3], 6)}")       # Expected: [0, 1] # Akash
