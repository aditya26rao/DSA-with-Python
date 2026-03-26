def findMajorityElement(nums):
    
    # Method 1:- Brute Force :- Tc O(n^2) and SC O(1)
    # n = len(nums)
    
    # for i in range(n):
    #     count = 0
    #     for j in range(n):
    #         if nums[i] == nums[j]:
    #             count += 1
                
    #     if count > (n // 2):
    #         return nums[i]

    # return -1
    
    # Method 2 Better Sol:- using HashMap :- TC O(n+m) and SC O(1)
    # hashMap = {}
    
    # for num in nums:
    #     hashMap[num] = hashMap.get(num,0) + 1
        
    # for key,value in hashMap.items():
    #     if value > (len(nums) // 2):
    #         return key
    # return -1
    
    # Method 3: Boyer-Moore Voting Algorithm
    # TC O(n) and SC O(1)
    
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
            count += 1
        elif candidate == num:
            count += 1
        else:
            count -= 1
            
    if nums.count(candidate) > (len(nums)//2):
        return candidate
    
    return -1
    

        
nums  = [7,0,0,1,7,7,2,7,7]
print(findMajorityElement(nums))