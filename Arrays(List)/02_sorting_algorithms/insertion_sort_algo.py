def insertion_sort(arr):
    # Traverse the array from the second element (index 1)
    # because the first element is already considered sorted
    for i in range(1, len(arr)):   
        # Store the current element to be placed at correct position
        key = arr[i]   
        # j points to the last element of the sorted part
        j = i - 1
        # Shift elements of the sorted part that are greater than key
        # to one position ahead to make space for key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]   # shift element to the right
            j = j - 1             # move left
        
        # Place key at its correct sorted position
        arr[j + 1] = key
    
    # Return the sorted array
    return arr


# Driver code
arr = [75, 90, 100, 95, 85, 50, 100, 110, 7]
result = insertion_sort(arr)
print(f"Insertion sort of the array is:- {result}")
