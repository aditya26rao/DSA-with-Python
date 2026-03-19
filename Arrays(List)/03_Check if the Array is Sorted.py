def sortedOrNot(nums):
    # Method 1:- Brute Force :- TC O(n^2), SC O(1)
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[j] >= nums[i]:
    #             pass
    #         else:
    #             return False
    # return True
    
    # Method 2:- Optimal Sol :- TC O(n) , SC O(1)
    for i in range(1,len(nums)):
        if nums[i] >= nums[i - 1]:
            pass
        else:
            return False
    return True
    
nums = [1,2,2,3,4]
print(sortedOrNot(nums))