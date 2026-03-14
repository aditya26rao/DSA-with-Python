'''
Best Case: O(n²)
Average Case: O(n²)
Worst Case: O(n²)
Space Complexity: O(1) (in-place)

                  No of swaps :- O(n)
                / 
Time Complexity 
                \ No of comparisons :- O(n²)
                
---> Overall its  O(n²)
'''

def selection_sort(arr):
    n = len(arr)  # Number of elements in the array

    # Outer loop runs n times
    # After each iteration, one element is placed at its correct position
    for i in range(n):
        # Assume the current index i has the minimum element
        min_index = i
        # Inner loop finds the minimum element in the unsorted part
        # Range shrinks every time: (n-1), (n-2), ... 1
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the element at index i
        arr[i], arr[min_index] = arr[min_index], arr[i]

    # Return the sorted array
    return arr


# Driver code
arr = [50, 38, 45, 79, 19, 27, 29]
result = selection_sort(arr)
print(f"Selection sort of the array is:- {result}")
