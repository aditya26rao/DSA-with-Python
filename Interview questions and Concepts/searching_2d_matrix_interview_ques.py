# Binary Search in a 2D sorted matrix by treating it as a flattened array
# Solution - Time Complexity is O(logmn), Space complexiyt O(logmn) as we are using recursion stack
# def binarySearch_2d(arr, i, j, x, rows, cols):
#     # Base condition: if search space becomes invalid, element is not present
#     if i > j:
#         return False
#     # Find the middle index of the flattened array
#     mid = i + (j - i) // 2
#     # Convert the flattened mid index into 2D matrix indices
#     # row index = mid // number of columns
#     # column index = mid % number of columns
#     r = mid // cols
#     c = mid % cols
#     # If the element at (r, c) is the target, return True
#     if arr[r][c] == x:
#         return True
#     # If current element is greater than target,
#     # then the target must be in the left half
#     elif arr[r][c] > x:
#         return binarySearch_2d(arr, i, mid - 1, x, rows, cols)
#     # If current element is smaller than target,
#     # then the target must be in the right half
#     else:
#         return binarySearch_2d(arr, mid + 1, j, x, rows, cols)


# # Given 2D matrix where each row is sorted
# # and the first element of each row is greater than
# # the last element of the previous row
# arr = [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 60]
# ]
# x = 5  # element to search
# rows = len(arr)        # number of rows
# cols = len(arr[0])     # number of columns
# # Search space is from 0 to (rows * cols - 1)
# i = 0
# j = rows * cols - 1
# result = binarySearch_2d(arr, i, j, x, rows, cols)
# print(result)

print('-------------------------------------------------------------------------------------------------------')

## Using Brute Force Approach :-
# def search_2d(arr,x):
#     for row in range(len(arr)):
#         for col in range(len(arr)):
#             if arr[row][col] == x:
#                 return True

#     return False
# arr = [
#     [1,3,5,7],
#     [10,11,16,20],
#     [23,30,34,60]
# ]
# x = 5
# result = search_2d(arr,x)
# print(result)

print('-------------------------------------------------------------------------------------------------------')


# Binary Search on a Sorted 2D Matrix (Iterative Approach)
# The matrix is treated as a flattened sorted 1D array
# Solution - Time Complexity is O(logmn), Space complexiyt O(1)
def sortSearch_matrix(arr, target):
    # Number of rows in the matrix
    m = len(arr)
    if m == 0:
        return False
    # Number of columns in the matrix
    n = len(arr[0])
    # Binary search boundaries on flattened array
    left, right = 0, m * n - 1
    
    while left <= right:
        # Find mid index of the flattened array
        mid = left + (right - left) // 2
        # Convert flattened index to 2D matrix indices
        mid_element = arr[mid // n][mid % n]
        # Check if target is found
        if target == mid_element:
            return True
        # If mid element is greater than target, search left half
        elif mid_element > target:
            right = mid - 1
        # If mid element is smaller than target, search right half
        else:
            left = mid + 1

    # Target not found
    return False


arr = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

target = 30
result = sortSearch_matrix(arr, target)
print(result)
