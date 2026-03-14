def findKFrequency(arr, k):
    # Better Solution using Hash Map
    # Explanation:
    #   - Build a frequency dictionary for all elements.
    #   - Iterate through the dictionary to find any element with frequency == k.
    #   - Return that element if found, else return -1.
    #
    # Time Complexity: O(n + m)
    #   - O(n) to build frequency dictionary (iterate over array)
    #   - O(m) to iterate over unique elements in dictionary
    #   => Total = O(n + m), where n = array length, m = number of distinct elements
    #
    # Space Complexity: O(m)
    #   - Hash map stores counts for each unique element
    #   - Space grows with number of distinct elements
    #
    # Note:
    #   - This is not brute force (which would be O(n^2)).
    #   - It’s not fully optimal either (there are specialized approaches if constraints are known),
    #     but for general arrays, this is considered the **better solution**.

    hashDict = {}
    
    # Step 1: Build frequency dictionary
    for num in arr:
        hashDict[num] = hashDict.get(num, 0) + 1
        
    # Step 2: Find element with frequency == k
    for ele, count in hashDict.items():
        if count == k:
            return ele
    
    return -1


# Example Run
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
k = 2
print(findKFrequency(arr, k))  # Output: 2
