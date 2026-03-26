"""
Kadane’s Algorithm – Maximum Subarray Sum with Subarray Tracking (Non-Empty Subarray)  
→ This returns both the maximum sum and the actual subarray, correctly handling all-negative cases.
    
"""
def maxSubArray(nums):
    maxi = float("-inf")
    sum = 0
    start = 0
    ans_start = -1
    ans_end = -1

    for i in range(len(nums)):
        if sum == 0:
            start = i

        sum += nums[i]

        if sum > maxi:
            maxi = sum
            ans_start = start
            ans_end = i

        if sum < 0:
            sum = 0

    return maxi, nums[ans_start:ans_end + 1]


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
