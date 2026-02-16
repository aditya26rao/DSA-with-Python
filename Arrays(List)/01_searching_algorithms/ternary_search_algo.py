def ternary_search_algo(arr, target):
    """
    -> Ternary Search Algorithm
    -> Works only on a SORTED array
    -> ⏱ Time Complexity
        Best Case: O(1) → element found at mid1 or mid2
        Average Case: O(log₃ n)
        Worst Case: O(log₃ n)
    -> 📦 Space Complexity
        Iterative version (this code): O(1) → constant extra space
        Recursive version: O(log n) → due to recursion stack
    """

    # Left boundary of search space
    i = 0

    # Right boundary of search space
    j = len(arr) - 1

    # Continue searching while search space is valid
    while i <= j:

        # Divide the array into 3 parts
        mid1 = i + (j - i) // 3
        mid2 = j - (j - i) // 3

        # If target is found at mid1
        if arr[mid1] == target:
            return mid1

        # If target is found at mid2
        elif arr[mid2] == target:
            return mid2

        # If target is smaller than value at mid1,
        # then it lies in the first part
        elif arr[mid1] > target:
            j = mid1 - 1

        # If target is greater than value at mid2,
        # then it lies in the third part
        elif arr[mid2] < target:
            i = mid2 + 1

        # Otherwise, target lies in the middle part
        else:
            i = mid1 + 1
            j = mid2 - 1

    # Target not found
    return -1


# ---------------- Driver Code ----------------
# NOTE: Ternary Search works only on a SORTED array

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5

result = ternary_search_algo(arr, target)

print(f"The element found at the index of:- {result}")
