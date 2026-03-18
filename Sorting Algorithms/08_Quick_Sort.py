def partition(arr, low, high):
    # Choose the first element as pivot
    pivot = arr[low]
    i = low
    j = high

    # Rearrange elements around the pivot
    while i < j:
        # Move i forward until we find an element greater than pivot
        while i <= high - 1 and arr[i] <= pivot:
            i += 1
        # Move j backward until we find an element smaller than pivot
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
        # Swap elements if i < j
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[low], arr[j] = arr[j], arr[low]
    return j  # Return pivot index


def quickSort(arr, low, high):
    if low < high:
        # Partition the array and get pivot index
        pivotIndex = partition(arr, low, high)
        # Recursively sort left part
        quickSort(arr, low, pivotIndex - 1)
        # Recursively sort right part
        quickSort(arr, pivotIndex + 1, high)
    
# Driver code
arr = [4, 1, 7, 9, 3]
quickSort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 3, 4, 7, 9]
