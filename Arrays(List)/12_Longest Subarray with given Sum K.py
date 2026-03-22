def longestSubArray(nums,k):
    # Method 1:- Brute Force :- TC O(n^3) and SC O(1)
    # maxLength = 0
    # for startIndex in range(len(nums)):
    #     for endIndex in range(startIndex,len(nums)):
    #         currentSum = 0
    #         for i in range(startIndex, endIndex + 1):
    #             currentSum += nums[i]
                
    #         if currentSum == k:
    #             maxLength = max(maxLength, endIndex - startIndex + 1)
                
    # return maxLength
    
    # Method 2:- Brute froce but Tc O(n^2) and SC O(1)
    
    # maxLenght = 0
    # for i in range(len(nums)):
    #     currentSum = 0
    #     for j in range(i,len(nums)):
    #         currentSum = currentSum + nums[j]
            
    #         if currentSum == k:
    #             maxLenght = max(maxLenght, j - i + 1)
            
    # return maxLenght
    
    # Method 3:- using  a PrefixSum:- this optimal when we have -ve and + ve in an array
    # TC o(n) and SC O(n)
    # prefixSum = {}
    # maxLen = currSum = 0
    
    # for i in range(len(nums)):
    #     currSum += nums[i]
        
    #     # Subarray from start
    #     if currSum == k:
    #         maxLen = max(maxLen,i + 1)
            
    #     # subarray ending at i
    #     rem = currSum - k
    #     if rem in prefixSum:
    #         lenght = i - prefixSum[rem]
    #         maxLen = max(maxLen,lenght)
            
    #     # store earliest occurence of currSum
    #     if currSum not in prefixSum:
    #         prefixSum[currSum] = i
            
    # return maxLen
            
    # Method 4: using Two Pointers:- TC O(n) and SC O(1), it an optimal sol when we have +ve and 0 in an array
    # and in worst case TC O(2n) => O(n) outer while and O(n) is inner while +> O( n + n ) => O(2n)
    left = right = maxLen = 0
    currSum = 0
    
    while right < len(nums):
        currSum += nums[right]
        
        while left <= right and currSum > k:
            currSum -= nums[left]
            left += 1
            
        if currSum == k:
            maxLen = max(maxLen, right - left + 1)
        
        right += 1
    
    return maxLen
    
nums = [10,5,2,7,1,9]
k = 15
print(longestSubArray(nums,k))