# Implementation of Binary Search
def binarySearch(arr, i, j, x):
    while i <= j:
        mid = i + (j - i) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            # recursion :- calling the func again with the diff set of algo
            return binarySearch(arr, mid + 1, j, x)
            # without using a recursion, we can directly update here
            # i = mid + 1
        else:
            return binarySearch(arr, i, mid - 1, x)
            # j = mid - 1
    # searching element not found then return -1
    return -1

# Driver code
arr = [2, 5, 10, 14, 18, 22, 27, 35, 40, 59]
arr.sort()
x = int(input("Enter any number:- "))
i = 0
j = len(arr) - 1
# Function Call
result = binarySearch(arr, i, j, x)
print("Searching element is present at the index", result)

''' 
Time complexity :- O(logn)
Space complexity :- O(1) as we only used "mid" variable
T(n) = T(n/2) + c, which is equal to O(logn) as per Master's Theorem
'''