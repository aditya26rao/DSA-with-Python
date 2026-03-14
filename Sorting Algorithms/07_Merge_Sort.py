def merge(arr, low, mid, high):
    # -------------------------------
    # Time Complexity (TC):
    # Best Case: O(n log n)
    # Worst Case: O(n log n)
    # Average Case: O(n log n)
    #
    # Space Complexity (SC):
    # O(n) for temporary arrays during merging
    # O(log n) recursion stack depth
    # -------------------------------

    temp = []
    left, right = low, mid + 1

    # Merge two sorted halves
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # Copy remaining elements
    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    # Place merged elements back into original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]
    
    return arr

def mergeSort(arr, low, high):
    # Base case
    if low >= high:
        return

    mid = low + (high - low) // 2

    # Sort left half
    mergeSort(arr, low, mid)
    # Sort right half
    mergeSort(arr, mid + 1, high)
    # Merge both halves
    return merge(arr, low, mid, high)


arr = [3, 1, 2, 4, 1, 5, 2, 6, 4]
low = 0
high = len(arr) - 1
print(mergeSort(arr, low, high))
