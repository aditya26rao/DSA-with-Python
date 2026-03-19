def rotateOneByLeft(nums):
    # Method 1:- Brute Force Sol, TC O(n), SC O(n)
    # n = len(nums)
    # temp = [0] * n
    
    # for i in range(n):
    #     temp[i - 1] = nums[i]
        
    # temp[n - 1] = nums[0]
    
    # nums[:] = temp
    
    # return nums
    
    # Method 2:- Optimal Sol, TC O(n), SC O(1)
    n = len(nums)
    temp = nums[0]
    for i in range(1,n):
        nums[i - 1]  = nums[i]
        
    nums[n-1] = temp
    
    return nums
    
nums = [1, 2, 3, 4, 5] 
print(rotateOneByLeft(nums)) 