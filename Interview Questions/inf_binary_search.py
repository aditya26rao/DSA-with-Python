def binarySearch(arr):
    i, j = 0, len(arr) - 1
    result = -1

    while i <= j:
        mid = i + (j - i) // 2

        if arr[mid] == "inf":
            result = mid
            j = mid - 1   # look left for earlier "inf"
        else:
            i = mid + 1   # look right

    return result

# Example
arr = [20, -30, 10, 5, 7, 0, 29, 'inf', 'inf', 'inf']
print("First 'inf' index:", binarySearch(arr))
