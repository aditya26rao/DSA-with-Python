def twoSum(nums, target):
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    # Create a hashmap (dictionary) to store number -> index
    hashMap = {}
    
    # Traverse the list (runs n times)
    for i, num in enumerate(nums):
        # Find the complement needed to reach target
        diff = target - num
        
        # Check if complement exists in hashmap (O(1) lookup)
        if diff in hashMap:
            # Return indices of complement and current number
            return [hashMap[diff], i]
        
        # Store current number with its index
        hashMap[num] = i


# Example input
nums = [3, 2, 4]
target = 6

# Output
print(twoSum(nums, target))