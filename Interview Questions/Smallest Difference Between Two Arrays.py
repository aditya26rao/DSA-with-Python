def smallestDifference(arr1,arr2):
    # Method 1:- Better Solution
    # TC is O(m+n)
    # SC is O(1)
    
    arr1.sort()
    arr2.sort()
    min_diff = float('inf')
    i,j = 0, 0
    pair = () 
    
    while i < len(arr1) and j < len(arr2):
        diff = abs(arr1[i] - arr2[j]) # calculting a diff 
        if diff < min_diff:
            min_diff = diff
            pair = (arr1[i],arr2[j]) # making a pair
        
        # Moving pointer of the smaller value
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return min_diff,pair
            

arr1 = [1, 3, 15, 11, 2]
arr2 = [23, 127, 235, 19, 8]
print(smallestDifference(arr1,arr2))