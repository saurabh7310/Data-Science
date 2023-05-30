def two_sum(nums, target):
    # Create a dictionary to store the complement of each number and its index
    complement_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in complement_map:
            # Return the indices of the current number and its complement
            return [complement_map[complement], i]
        
        # Add the current number and its index to the dictionary
        complement_map[num] = i
    
    # If no solution is found, return an empty list
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
# Output: [0, 1]