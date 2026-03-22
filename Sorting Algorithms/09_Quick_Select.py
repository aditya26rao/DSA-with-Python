def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while i <= high - 1 and arr[i] <= pivot:
            i += 1
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quickSelect(arr, low, high, k):
    target = len(arr) - k  # kth largest index
    while low <= high:
        pivotIndex = partition(arr, low, high)

        if pivotIndex == target:
            return arr[pivotIndex]
        elif pivotIndex > target:
            #high = pivotIndex - 1
            return quickSelect(arr, low, pivotIndex - 1, k)
        else:
            #low = pivotIndex + 1
            return quickSelect(arr, pivotIndex + 1, high, k)


arr = [4, 1, 7, 9, 3]
k = 2
print(quickSelect(arr, 0, len(arr) - 1, k))  # should print 7
