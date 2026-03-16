'''
Given an integer array arr[] of size n, find the inversion count in the array. Two array elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.
'''
# Method 1:- Brute Force :- TC O(n^2) and SC  O(1)
# def countInversion(arr):
#     inv_count = 0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i] > arr[j]:
#                 inv_count += 1       
#     return inv_count  
    
# arr = [4,3,2,1]
# print(countInversion(arr))


# Method 2:- Using Merge Sort 

def mergeArray(arr,low,mid,high):
    result = []
    
    left = low
    right = mid + 1
    invCount = 0
    
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            result.append(arr[left])
            left += 1
        else:
            result.append(arr[right])
            right += 1
            invCount += mid - left + 1 # im only adding inversion count if i < j and arr[i] > arr[j]
        
    while left <= mid:
        result.append(arr[left])
        left += 1

    while right <= high:
        result.append(arr[right])
        right += 1
        
    arr[low:high + 1] = result
    
    return invCount
            
    
def countInversion(arr,low,high):
    if low >= high:
        return 0
    
    invCount = 0
    mid = low + (high - low) // 2
    
    invCount += countInversion(arr,low,mid)
    invCount += countInversion(arr,mid + 1, high)

    invCount += mergeArray(arr,low,mid,high)
    
    return invCount

def inversionCount(arr):
    return countInversion(arr,0,len(arr) - 1)
    
arr = [2,4,1,3,5]
print(inversionCount(arr))