arr = [2, 1, 8, 9, 12, 15, 11, 19]

## Random Access in Array
print(arr[4])

"""
Time Complexity:
----------------
O(1) → Direct access using index

Space Complexity:
-----------------
O(1)
"""

print("-----------------------------------------------------------")


## Search for an element and return its index if present, else -1
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


print(
    f"Searching element is present at the index :- "
    f"{linear_search(arr, target=int(input('Enter the number:- ')))}"
)

"""
Time Complexity:
----------------
Best Case    : O(1) → If element found at index 0
Worst Case   : O(n) → If element is at last index or not present
Average Case : O(n) → If element is found in between

Overall Time Complexity: O(n)

Space Complexity:
-----------------
O(1) → Only constant extra variables (i, target)
"""

print("-----------------------------------------------------------")


# Insert an element 5 at index 2
arr.insert(2, 5)  # insert(index, value)
print(arr)

"""
Time Complexity:
----------------
O(n) → Elements after index 2 need to be shifted

Space Complexity:
-----------------
O(1) → In-place operation
"""

print("-----------------------------------------------------------")


# Remove an element 8 from the array
arr.remove(8)  # remove(value)
print(arr)

"""
Time Complexity:
----------------
O(n)
- O(n) to search the element
- O(n) to shift elements after removal

Overall: O(n)

Space Complexity:
-----------------
O(1)
"""

print("-----------------------------------------------------------")


# Count the frequency of an element present inside the array
print(arr.count(2))

"""
Time Complexity:
----------------
O(n) → Entire array is scanned to count occurrences

Space Complexity:
-----------------
O(1)
"""

print("-----------------------------------------------------------")


# Delete an element by providing index
arr.pop(4)  # pop(index)
print(arr)

"""
Time Complexity:
----------------
O(n) → Elements after removed index are shifted
(Note: pop() without index is O(1))

Space Complexity:
-----------------
O(1)
"""

print("-----------------------------------------------------------")


# Sort the array
arr.sort()  # Ascending order
print(arr)

"""
Time Complexity:
----------------
O(n log n) → Python uses Timsort

Space Complexity:
-----------------
O(1) → sort() works in-place
"""

arr.sort(reverse=True)  # Descending order
print(arr)

"""
Time Complexity:
----------------
O(n log n)

Space Complexity:
-----------------
O(1)
"""

print("-----------------------------------------------------------")


# Extract the index of an element
print(arr.index(11))  # index(value)

"""
Time Complexity:
----------------
O(n) → List is scanned until element is found

Space Complexity:
-----------------
O(1)
"""

print("-----------------------------------------------------------")


# Extend the original array with multiple elements
arr.extend([2, 5, 6, 7])
print(arr)

"""
Time Complexity:
----------------
O(k) → k is the number of elements added

Space Complexity:
-----------------
O(1) → In-place modification
"""

print("-----------------------------------------------------------")


# Reverse the entire list
arr.reverse()
print(arr)

"""
Time Complexity:
----------------
O(n) → Entire list is reversed

Space Complexity:
-----------------
O(1) → In-place reversal
"""
