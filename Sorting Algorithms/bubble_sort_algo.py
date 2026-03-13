'''
✔️ Compares adjacent elements
✔️ Largest element bubbles to the end each pass
✔️ Time Complexity: O(n²)
✔️ Space Complexity: O(1) (in-place sort)
'''

def bubble_sort(arr):
    n = len(arr)          # Get the number of elements in the array
    # Outer loop for number of passes
    # After each pass, the largest element moves to the end
    for i in range(n):
        # Inner loop for comparing adjacent elements
        # n - i - 1 because the last i elements are already sorted
        swapped = False
        for j in range(n - i - 1):
            # If current element is greater than the next element
            # then swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        if not swapped:
            break # No swaps means array is already sorted

    # Return the sorted array
    return arr


# ---------------- Driver Code ----------------
arr = [70, 20, 50, 30, 90, 5, 15]  # Unsorted array
result = bubble_sort(arr)         # Call bubble sort function
print(f"Bubble sort of the array is:-{result}")                     # Print sorted array
