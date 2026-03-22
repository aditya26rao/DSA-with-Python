
def findMaxConsecutiveOnes(nums):
    # Brute Force :- O(n^2) adn SC O(1)
    # maxi = 0
    # for i in range(len(nums)):
    #     count = 0
    #     for j in range(i,len(nums)):
    #         if nums[j] == 1:
    #             count += 1
    #             maxi = max(maxi,count)
    #         else:
    #             break
    # return maxi
    
    # Method 2:- using hashList; TC O(n) and Sc O(n)
    counts = []
    count = 0
    
    for num in nums:
        if num == 1:
            count += 1
        else:
            counts.append(count)
            count = 0
    
    counts.append(count) # this add the final streak
    return max(counts)
                
    # # Optimal SOl:- TC O(n) and SC  O(1)
    # count = 0
    # maxi = 0

    # for i in range(len(nums)):
    #     if nums[i] == 1:
    #         count += 1
    #         maxi = max(maxi,count)
    #     else:
    #         count = 0
    # return maxi

nums = [1,1,0,1,1,1,0,1,1]
print(findMaxConsecutiveOnes(nums))