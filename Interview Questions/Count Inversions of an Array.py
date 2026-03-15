'''
Given an integer array arr[] of size n, find the inversion count in the array. Two array elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.
'''
def countInversion(arr):
    # Method 1:- Brute Force :- TC O(n^2) and SC  O(1)
    
    inv_count = 0
    
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1
                
    return inv_count  
    
arr = [4,3,2,1]
print(countInversion(arr))