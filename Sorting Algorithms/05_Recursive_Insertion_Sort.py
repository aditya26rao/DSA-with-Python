def recursiveInsertionSort(arr, i, n):
    # Base case: if all elements are sorted
    if i == n:
        return arr
    
    key = arr[i]
    j = i - 1
    
    # Move elements greater than key one position ahead
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = key
    
    # Recursive call for next element
    return recursiveInsertionSort(arr, i + 1, n)


arr = [70, 20, 50, 30, 90, 5, 15]
print(recursiveInsertionSort(arr, 1, len(arr)))

# -------------------------------
# Time Complexity (TC):
# Best Case (already sorted): O(n)
# Worst Case (reverse sorted): O(n^2)
# Average Case: O(n^2)
#
# Space Complexity (SC):
# O(n) due to recursion stack depth
# (Iterative version uses O(1) extra space)
# -------------------------------
