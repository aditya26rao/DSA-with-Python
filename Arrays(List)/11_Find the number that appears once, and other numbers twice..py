def numberApearsOnce(nums):
    # Method 1:- Brute Force:- TC (O^2) and SC O(1)
    # for i in range(len(nums)):
    #     count = 0
    #     for j in range(len(nums)):
    #         if nums[i] == nums[j]:
    #             count += 1
                
    #     if count == 1:
    #         return nums[i]
        
    # return -1
    
    # Method 2:- using HashMap TC O(m + n) and SC O(n)
    
    # hashMap = {}
    
    # for num in nums:
    #     hashMap[num] = hashMap.get(num,0) + 1
        
    # for k,v in hashMap.items():
    #     if v == 1:
    #         return k
    
    # Method 3:- Optimal Sol:- using XOR
    
    xor = 0
    
    for num in nums:
        xor = xor ^ num
        
    return xor
    
    
nums = [4,1,2,1,2]
print(numberApearsOnce(nums))