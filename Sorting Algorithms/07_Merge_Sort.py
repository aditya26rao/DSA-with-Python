
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
    
# Method 1 :- From Strvier Sheet Logic
# def merge(arr, low, mid, high): 
#     temp = []
#     left, right = low, mid + 1

#     # Merge two sorted halves
#     while left <= mid and right <= high:
#         if arr[left] <= arr[right]:
#             temp.append(arr[left])
#             left += 1
#         else:
#             temp.append(arr[right])
#             right += 1

#     # Copy remaining elements
#     while left <= mid:
#         temp.append(arr[left])
#         left += 1

#     while right <= high:
#         temp.append(arr[right])
#         right += 1

#     # Place merged elements back into original array
#     arr[low:high+1] = temp
    
#     return arr

# def mergeSort(arr, low, high):
#     # Base case
#     if low >= high:
#         return

#     mid = low + (high - low) // 2

#     # Sort left half
#     mergeSort(arr, low, mid)
#     # Sort right half
#     mergeSort(arr, mid + 1, high)
#     # Merge both halves
#     return merge(arr, low, mid, high)

# arr = [3, 1, 2, 4, 1, 5, 2, 6, 4]
# low = 0
# high = len(arr) - 1
# result = mergeSort(arr, low, high)
# print(result)

# print('----------------------------------------------------------')

# Method 2:- From Code and Debug

# Function to merge two sorted arrays into one sorted array
def merge_array(left, right):
    result = []   # temporary list to store merged result
    i, j = 0, 0   # pointers for left and right arrays
    n, m = len(left), len(right)
    
    # Compare elements from both halves and append the smaller one
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Copy remaining elements from left half (if any)
    while i < n:
        result.append(left[i])
        i += 1
    
    # Copy remaining elements from right half (if any)
    while j < m:
        result.append(right[j])
        j += 1
        
    return result   # return merged sorted array

# Recursive merge sort function
def mergeSort(arr):
    # Base case: if array has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle index to split array
    mid = len(arr) // 2
    
    # Divide array into left and right halves
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)
    
    # Merge sorted halves
    return merge_array(left_half, right_half)


# Driver code
arr = [3, 1, 2, 4, 1, 5, 2, 6, 4]
result = mergeSort(arr)
print(result)

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
