def majorityElement(arr):
    # Method 1: Better Solution using HashMap (Frequency Counting)

    # Time Complexity (TC): O(n)
    # - We traverse the array once to build the frequency map → O(n)
    # - Then we iterate over the hashmap elements → O(m)
    # - Since m ≤ n (number of unique elements cannot exceed n)
    # Total TC = O(n) or we can also say TC = O(m + n) as they added we get a single value 

    # Space Complexity (SC): O(m)
    # - Hashmap stores frequency of each unique element
    # - m = number of distinct elements in the array

    hashDict = {}
    n = len(arr)

    # Step 1: Build frequency dictionary
    for num in arr:
        hashDict[num] = hashDict.get(num, 0) + 1

    # Step 2: Check if any element occurs more than n//2 times
    for ele, count in hashDict.items():
        if count > n // 2:
            return ele

    # Step 3: If no majority element exists
    return -1


# Example
arr = [3, 3, 4, 2, 3, 3, 5]
print(majorityElement(arr))  # Output: 3