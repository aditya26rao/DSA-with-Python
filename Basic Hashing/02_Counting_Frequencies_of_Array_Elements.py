def countFrequency(arr, n):
    # -------------------------------
    # Method 1: Array Hashing (Better / Brute Force)
    # TC: O(n + max(arr)) 
    #   -> O(n) to traverse arr + O(max(arr)) to build dictionary from hash list
    # SC: O(max(arr) + Unique)
    #   -> O(max(arr)) for hash list + O(U) for dictionary of unique elements
    # This is only optimal when max(arr) is small.
    #
    # max_len = max(arr) if arr else 0 
    # hastList = [0] * (max_len + 1)
    # hashDict = {}
    # for num in arr:
    #     hastList[num] += 1
    # for i in range(len(hastList)):
    #     if hastList[i] > 0:
    #         hashDict[i] = hastList[i]
    # return hashDict
    # -------------------------------

    # -------------------------------
    # Method 2: Dictionary Hashing (Optimal in Python)
    # TC: O(n) average
    #   -> Single pass through arr, dictionary insertions are O(1) average
    # SC: O(Unique)
    #   -> Only stores unique elements
    # This is the optimal solution in Python, especially when arr contains large values.
    # -------------------------------
    freqDict = {}
    for i in range(n):
        freqDict[arr[i]] = freqDict.get(arr[i], 0) + 1

    for key, value in freqDict.items():
        print(key, value)

arr = [10, 5, 10, 15, 10, 5]
print(countFrequency(arr, len(arr)))
