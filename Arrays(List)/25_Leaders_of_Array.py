def leaders_of_array(nums):
    # Method 1:- Brute Force 
    # TC O(n^2) and SC O(n) at worst case, and SC O(1) in best
    # result = []
    # for i in range(len(nums)):
    #     leader = True
    #     for j in range(i+1,len(nums)):
    #         if nums[j] > nums[i]:
    #             leader = False
    #             break
            
    #     if leader:
    #         result.append(nums[i])
            
    # return result
    
    
    # Optimal Solution
    # TC O(n) and SC O(n)
    result = []
    maxi = float('-inf')
    for i in range(len(nums)-1,-1,-1):
        if nums[i] >= maxi:
            result.append(nums[i])
            maxi = nums[i]
        else:
            maxi = max(maxi,nums[i])
            
    return result[::-1]

nums = [10,22,12,3,0,6]
print(leaders_of_array(nums))