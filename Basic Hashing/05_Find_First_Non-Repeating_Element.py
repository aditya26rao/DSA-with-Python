def findFirstElement(arr):
    # Method 1: Better Solution (Hash Map, but order not guaranteed)
    # Time Complexity: O(n + m)
    # Space Complexity: O(m)
    # Issue: Iterating over hashDict does not preserve array order

    # hashDict = {}

    # for num in arr:
    #     hashDict[num] = hashDict.get(num, 0) + 1

    # for element in hashDict:
    #     if hashDict[element] == 1:
    #         return element
    # return None

    # Method 2: Optimal Solution
    # Step 1: Build frequency dictionary (O(n))
    # Step 2: Iterate over array to preserve order (O(n))
    # Time Complexity: O(n)
    # Space Complexity: O(m)
    # This ensures we return the first non-repeating element in correct order

    # Step 1: Build frequency dictionary
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Step 2: Iterate over array to preserve order
    for num in arr:
        if freq[num] == 1:
            return num

    return None  # if no non-repeating element exists


arr = [4, 5, 1, 2, 0, 4]
print(findFirstElement(arr))
