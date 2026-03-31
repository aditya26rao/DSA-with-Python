def longest_consecutive_array(nums):
    # Method 1:- Brute Force :- 
    # TC O(n^2) and SC O(1)
    # Helper function to check if num exists in arr
    
    # n = len(nums)
    # max_count = 0
    # for i in range(n):
    #     num = nums[i]
    #     count = 1
        
    #     while (num + 1) in nums:
    #         count += 1
    #         num += 1
    #     max_count = max(max_count,count)
        
    # return max_count
    
    
    # Method 2:- Better Solution :- TC O(n log n) and SC O(1)
    # longest = 1
    # currentCount = 0
    # lastSmaller = float('-inf')
    
    # nums.sort()
    
    # for i in range(len(nums)):
    #     if (nums[i] - 1) == lastSmaller:
    #         currentCount += 1
    #         lastSmaller = nums[i]
            
    #     elif nums[i] != lastSmaller:
    #         currentCount = 1
    #         lastSmaller = nums[i]
            
    #     longest = max(longest, currentCount)
    
    # return longest
    
    # Method 3:- Optimal Solution
    # TC O(n + m) and SC O(1) in best, and in worst case SC takes O(n)

    n = len(nums)
    if n == 0:
        return 0
    
    hashSet = set(nums)
    longest = 0
    
    for item in hashSet:
        # Start of a sequence
        if item - 1 not in hashSet:
            count = 1
            x = item
            
            while x + 1 in hashSet:
                x += 1
                count += 1
            
            longest = max(longest, count)
    
    return longest

# Test
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_array(nums))  # Output: 4

