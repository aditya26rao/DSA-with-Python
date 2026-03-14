def recursiveBubbleSort(arr , n):
    # Optimal Sol:- recurrsion 
    # Time Complexity: O(N2) for the worst and average cases and O(N) for the best case. Here, N = size of the array.
    # Space Complexity: O(N) auxiliary stack space.

    if n == 1:
        return arr
    
    swapped = False
    
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j],arr[j + 1] = arr[j + 1],arr[j]
            swapped = True
            
    if not swapped:
        return arr
    
    return recursiveBubbleSort(arr, n - 1)
    
    
    
arr = [70, 20, 50, 30, 90, 5, 15] 
print(recursiveBubbleSort(arr, len(arr)))