def reverseArray(arr):
    # return arr[::-1] #in-built method which TC O(n) and SC O(1)

    # we can also use Two Pointer :- TC O(n) and SC O(1)
    p1 = 0
    p2 = len(arr) - 1

    while p1 < p2:  # checks the points
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1  # goes to right
        p2 -= 1  # goes to left
    return arr

arr = [1, 2, 3, 4, 5]
print(reverseArray(arr))
