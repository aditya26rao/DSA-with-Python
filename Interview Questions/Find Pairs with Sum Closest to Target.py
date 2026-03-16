# Method: Sort + Two Pointer Technique
# Time Complexity (TC): O(n log n)
#   Sorting the array takes O(n log n)
#   Two pointer traversal takes O(n)
#
# Space Complexity (SC): O(1)
#   No extra space used except a few variables


def findPair_of_Sum(nums, target):

    # Step 1: Sort the array
    # Sorting helps us use the two-pointer technique efficiently
    nums.sort()
    
    # Initialize two pointers
    left = 0                      # pointer at the start
    right = len(nums) - 1         # pointer at the end
    
    # Variable to store minimum difference between target and pair sum
    min_diff = float('inf')
    
    # Variable to store the closest pair
    closest_pair = None
    
    # Traverse until both pointers meet
    while left < right:
        
        # Calculate sum of current pair
        current_sum = nums[left] + nums[right]
        
        # Calculate difference from target
        diff = abs(target - current_sum)
        
        # Update minimum difference and pair if a closer sum is found
        if diff < min_diff:
            min_diff = diff
            closest_pair = (nums[left], nums[right])
            
        # If current sum is smaller than target
        # move left pointer forward to increase sum
        if current_sum < target:
            left += 1
            
        # If current sum is greater than or equal to target
        # move right pointer backward to decrease sum
        else:
            right -= 1
            
    # Return minimum difference and the closest pair
    return min_diff, closest_pair
    

# Example input
nums = [10, 22, 28, 29, 30, 40]
target = 54

# Function call
print(findPair_of_Sum(nums, target))