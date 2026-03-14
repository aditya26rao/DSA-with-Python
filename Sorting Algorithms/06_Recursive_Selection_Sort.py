def recursiveSelectionSort(arr, i, n):
    # Base case: when only one element is left
    if i == n - 1:
        return arr

    # Find the minimum element in the unsorted part
    minIndex = i
    for j in range(i + 1, n):
        if arr[j] < arr[minIndex]:
            minIndex = j

    # Swap the found minimum with the first element of unsorted part
    arr[i], arr[minIndex] = arr[minIndex], arr[i]

    # Recursive call for the rest of the array
    return recursiveSelectionSort(arr, i + 1, n)


arr = [50, 38, 45, 79, 19, 27, 29]
result = recursiveSelectionSort(arr, 0, len(arr))
print(f"Selection sort of the array is:- {result}")

# -------------------------------
# Time Complexity (TC):
# Best Case: O(n^2)   -> Selection sort always scans the unsorted part
# Worst Case: O(n^2)  -> Same as best case, comparisons are fixed
# Average Case: O(n^2)
#
# Space Complexity (SC):
# O(n) due to recursion stack depth
# (Iterative version uses O(1) extra space)
#
# Note: Selection sort is NOT stable, but it minimizes swaps (only O(n)).
# -------------------------------
