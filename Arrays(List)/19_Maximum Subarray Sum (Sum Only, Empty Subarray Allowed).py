'''
Kadane’s Algorithm – Maximum Subarray Sum (Sum Only, Empty Subarray Allowed)  
→ This returns only the maximum sum and outputs 0 if all numbers are negative.

'''

def maxSubArray(nums):
    # Brute Force :- TC O(n^3), SC O(1)
    # maximum = float('- inf')
    # for i in range(len(nums)):
    #     for j in range(i,len(nums)):
    #         sum = 0
    #         for k in range(i,j):
    #             sum += nums[k]
    #         maximum = max(sum,maximum)
    # return maximum
    
    # Better Sol :- TC O(n^2), SC O(1)
    # maximum = float('-inf') 
    # for i in range(len(nums)):
    #     sum = 0
    #     for j in range(i,len(nums)):
    #         sum += nums[j]
    #         maximum = max(sum,maximum)
        
    # return maximum
    
    # Optimal Solution :- using Kadane's algo
    # TC O(n), SC O(1)
    sum = 0
    maxi = float('-inf')
    
    for i in range(len(nums)):
        sum += nums[i]
        
        if sum > maxi:
            maxi = sum
            
        if sum < 0:
            sum = 0
        
            
    return maxi
        

nums = [2, 3, 5, -2, 7, -4]
print(maxSubArray(nums))