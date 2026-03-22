def prefixSum(nums,k):
    prefixSumMap = {}
    maxLen = currentSum = 0
    # looping ovet the N elements
    for i in range(len(nums)):
        currentSum += nums[i] # adding direclty after loopin over ele
        
        if currentSum == k: # checking if currSum == k
            maxLen = max(maxLen, i + 1) # we are updating teh maxLen
            
        rem = currentSum - k
        if rem in prefixSumMap:
            length = i - prefixSumMap[rem]
            maxLen = max(maxLen,length)
            
        if currentSum not in prefixSumMap:
            prefixSumMap[currentSum] = i
            
    return maxLen
    
    
    
    
nums = [10,5,2,7,1,9]
k = 15
print(prefixSum(nums,k))