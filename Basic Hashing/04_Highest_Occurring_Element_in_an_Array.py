def highestOccuring(arr):
    # Method 1: Brute Force
    # Time Complexity: O(n^2) because for each element we scan the rest of the array
    # Space Complexity: O(n) due to the visited[] array of size n
    n = len(arr)
    visited = [False] * n
    minFreq = float('inf')
    minEle = 0
    maxFreq = 0
    maxEle = 0
    
    for i in range(n):
        if visited[i]:
            continue
        
        count = 1
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1
                
        if count > maxFreq:
            maxFreq = count
            maxEle = arr[i]
        
        if count < minFreq:
            minFreq = count
            minEle = arr[i]
                
    return f"Max Occuring Element is {maxEle} which occurs {maxFreq}, and Min is {minEle} which occurs {minFreq}"
            
    # Method 2: Optimal Solution (using Hash Map)
    # Time Complexity: O(n + m)
    #   - O(n) to build the frequency dictionary
    #   - O(m) to iterate over unique elements (m = number of distinct elements)
    # Space Complexity: O(m) for storing counts of unique elements
    # Note: Not O(1), because dictionary size grows with distinct elements
    
    # hashDict = {}
    # minFreq = float('inf')
    # minEle = 0
    # maxFreq = 0
    # maxEle = 0
    
    # for num in arr:
    #     hashDict[num] = hashDict.get(num, 0) + 1
        
    # for element, count in hashDict.items():
    #     if count > maxFreq:
    #         maxFreq = count
    #         maxEle = element
    #     if count < minFreq:
    #         minFreq = count
    #         minEle = element
    
    # return f"Max Occuring Element is {maxEle} which occurs {maxFreq}, and Min is {minEle} which occurs {minFreq}"
        

arr = [10, 5, 10, 15, 10, 5]
print(highestOccuring(arr))
