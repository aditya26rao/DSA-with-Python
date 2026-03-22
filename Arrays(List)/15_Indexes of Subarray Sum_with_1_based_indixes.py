def subarraySum(nums, target):
    # Initialize variables
    currentSum = left = right = 0
    
    # Iterate through the array with right pointer
    while right < len(nums):
        currentSum += nums[right]   # Add current element to window sum
        
        # Shrink window from the left if sum exceeds target
        while left < right and currentSum > target:
            currentSum -= nums[left]
            left += 1
            
        # Check if current window sum equals target
        if currentSum == target:
            return [left + 1, right + 1]  # +1 for 1-based indexing
        
        right += 1   # Expand window to the right
    
    # If no subarray found
    return [-1]


# Example usage
nums = [1, 2, 3, 7, 5]
target = 12
print(subarraySum(nums, target))  # Output: [2, 4]

# -------------------------------
# ⏱ Time Complexity (TC):
# - Each element is visited at most twice (once by 'right', once by 'left').
# - Overall: O(n), where n = length of nums.
#
# 📦 Space Complexity (SC):
# - Only a few variables (currentSum, left, right) are used.
# - No extra data structures proportional to input size.
# - Overall: O(1).
# -------------------------------
