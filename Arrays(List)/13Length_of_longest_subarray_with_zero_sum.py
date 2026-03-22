def longestSubArray_withZero(nums):
   # Method 1:- using Prefix/Hashmap 
    '''
Time Complexity (O(n)):
You iterate through the array once. Each step involves constant-time operations (hashmap lookup/insert). So overall it’s linear.

Space Complexity (O(n)):
In the worst case, every prefix sum is unique, so the hashmap stores up to n entries. That’s linear extra space.
    '''
    # n = len(nums)
    # hashMap = {}
    
    # maxLen = currentSum = 0

    # for i in range(n):
    #     currentSum += nums[i]
        
    #     if currentSum == 0:
    #         # update my maxLen
    #         maxLen = max(maxLen, i + 1)
            
    #         # checking if my sum in hashMap, updating the maxLen
    #     elif currentSum in hashMap:
    #         maxLen = max(maxLen, i - hashMap[currentSum])
    #     # if not, initializing the currentSum into hashmap
    #     else:
    #         hashMap[currentSum] = i
            
            
    # return maxLen
    
    
    n = len(nums)
    hashMap = {}
    
    maxLen = currentSum = 0

    for i in range(n):
        currentSum += nums[i]
        
        if currentSum == 0:
            # update my maxLen
            maxLen = max(maxLen, i + 1)
            
        else:
            # checking if my sum in hashMap, updating the maxLen
            if currentSum in hashMap:
                length = i - hashMap[currentSum]
                maxLen = max(maxLen, length)
            # if not, initializing the currentSum into hashmap
            else:
                hashMap[currentSum]  = i
            
            
    return maxLen
    

    
nums = [9, -3, 3, -1, 6, -5]
print(longestSubArray_withZero(nums))