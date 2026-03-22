def ongestSubarrayDivK(arr, k):
    """
    Time Complexity: O(n)
    - Single pass through the array
    - Hashmap lookup/insert is O(1) average

    Space Complexity: O(min(n, k))
    - Hashmap stores at most k remainders
    """

    hashMap = {}   # remainder -> earliest index
    maxLen = currentSum = 0

    for i in range(len(arr)):
        currentSum += arr[i]

        # Case 1: subarray from start (0...i)
        if currentSum % k == 0:
            maxLen = max(maxLen, i + 1)

        # Normalize remainder (important for negatives)
        rem = currentSum % k
        if rem < 0:
            rem += k

        # Case 2: subarray ending at i
        if rem in hashMap:
            length = i - hashMap[rem]
            maxLen = max(maxLen, length)
        else:
            # store earliest occurrence of this remainder
            hashMap[rem] = i
        
arr = [1,2,-2]
k = 2
print(ongestSubarrayDivK(arr,k))