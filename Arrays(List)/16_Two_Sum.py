def twoSum(nums, target):
    # Method 1:- Better SOl using HashMap
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    # Create a hashmap (dictionary) to store number -> index
    # hashMap = {}
    
    # # Traverse the list (runs n times)
    # for i, num in enumerate(nums):
    #     # Find the complement needed to reach target
    #     diff = target - num
        
    #     # Check if complement exists in hashmap (O(1) lookup)
    #     if diff in hashMap:
    #         # Return indices of complement and current number
    #         return [hashMap[diff], i]
        
    #     # Store current number with its index
    #     hashMap[num] = i
    
    
    # Method 2:- Optmial Sol using Two pointer
    # TC :- O(n) + O(nlogn) => O(nlogn)
    # TC O(n * logn), SC O(1)
    
    left = 0
    right = len(nums) - 1
    
    nums.sort()
    
    while left < right:
        if nums[left] + nums[right] == target:
            return [left,right]
        
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
            
    return -1
    

# Example input
nums = [3, 2, 4]
target = 6

# Output
print(twoSum(nums, target))