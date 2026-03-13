def duplicateElement(arr):
    # Method 1: Better Solution using Hash Map
    # Explanation:
    #   - We use a dictionary (hash map) to count the frequency of each element.
    #   - Then, we collect all elements that occur more than once.
    #
    # Time Complexity: O(n + m)
    #   - O(n) to build the frequency dictionary (iterate over array)
    #   - O(m) to iterate over unique elements in the dictionary
    #   => Total = O(n + m), where n = array length, m = number of distinct elements
    #
    # Space Complexity: O(m)
    #   - Hash map stores counts for each unique element
    #   - Space grows with number of distinct elements
    #
    # Note:
    #   - This is not brute force (which would be O(n^2)).
    #   - It’s not fully optimal either (there are specialized approaches for certain constraints),
    # #     but for general arrays, this is considered the **better solution**.

    hashDict = {}
    duplicateList = []
    
    # Step 1: Build frequency dictionary
    for num in arr:
        hashDict[num] = hashDict.get(num, 0) + 1
    
    # Step 2: Collect elements with frequency > 1
    for ele, count in hashDict.items():
        if count > 1:
            duplicateList.append(ele)
            
    return duplicateList  

arr = [1, 2, 3, 1, 3, 6, 6]
print(duplicateElement(arr))  # Output: [1, 3, 6]
