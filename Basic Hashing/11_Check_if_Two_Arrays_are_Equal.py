def checkTwoArray(arr1, arr2):
    # Method 1:- Better Solution using Hash Maps
    # Explanation:
    #   - First check if lengths are equal. If not, arrays cannot be equal.
    #   - Build frequency dictionaries for both arrays.
    #   - Compare the two dictionaries. If identical, arrays are equal (order doesn’t matter).
    #
    # Time Complexity: O(n + m)
    #   - O(n) to build frequency dictionary for arr1
    #   - O(m) to build frequency dictionary for arr2
    #   - O(m) to compare both dictionaries
    #   => Total = O(n + m), where n = len(arr1), m = len(arr2)
    #
    # Space Complexity: O(m)
    #   - Hash maps store counts for each unique element
    #   - Space grows with number of distinct elements
    #
    # Note:
    #   - This is not brute force (which would be O(n^2)).
    #   - It’s not fully optimal either (sorting both arrays would also give O(n log n) with O(1) extra space).
    #   - For general arrays, this hashing approach is considered the **better solution**.

    if len(arr1) != len(arr2):
        return False
    
    freq1 = {}
    freq2 = {}
    
    for num in arr1:
        freq1[num] = freq1.get(num, 0) + 1
    
    for num in arr2:
        freq2[num] = freq2.get(num, 0) + 1
    
    if freq1 == freq2:
        return True
    
    return False

# Example Run
arr1, arr2 = [1, 2, 3], [3, 2, 1]
print(checkTwoArray(arr1, arr2))  # Output: True
