#Question 1: 
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

################################################################################

# Question 2
def remove_element(nums, val):
    k = 0  # Variable to track the count of elements not equal to val
    
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    
    return k

# Example usage
nums = [3, 2, 2, 3]
val = 3
k = remove_element(nums, val)
print("Output:", k)
print("Modified nums:", nums[:k])

###############################################################################
# Question 3
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

# Example usage
nums = [1, 3, 5, 6]
target = 5
index = searchInsert(nums, target)
print("Output:", index)

############################################################################
# Question 4


