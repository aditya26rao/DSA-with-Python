# Question:
# Given an array where all finite numbers come first and all "inf" values
# appear consecutively at the end, find the index of the FIRST occurrence
# of "inf" using Binary Search.

def binarySearch(arr, i, j):
    mid = i + (j - i) // 2
    while i <= j:
        if arr[mid] != "inf": # if notarr[mid] not equal to "inf", then go right , as we know all the "inf" are at right
            return binarySearch(arr, mid + 1, j) # updating the i = mid+1 , and calling recursive func again
        elif arr[mid] == "inf": # if arr[mid] == 'inf' 
            if arr[mid - 1] != "inf": # we may have 'inf' not only at frist, even later, so check teh previous value is 'inf' or not, if not return mid
                return mid
            elif arr[mid] == "inf": # if previous value is 'inf' then we have to go backward, so j = mid - 1
                return binarySearch(arr, i, mid - 1)
    return -1

arr = [20,-30,10,5,7,0,29,'inf','inf','inf','inf','inf','inf','inf','inf','inf','inf','inf','inf','inf','inf','inf','inf','inf','inf','inf','inf']
i = 0
j = len(arr) - 1
result = binarySearch(arr, i, j)
print("Searching the first infintiy index:- ", result)
