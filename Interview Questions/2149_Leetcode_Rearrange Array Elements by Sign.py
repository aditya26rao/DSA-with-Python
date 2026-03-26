def rearrangeArrayElements(arr):
    # Optimal Solution (In-place style using index tracking)
    # TC: O(n)
    # SC: O(n) (result arr
    
    n = len(arr)
    
    result = [0] * n
    pos = 0
    neg = 1
    
    for i in range(n):
        if arr[i] > 0:
            result[pos] = arr[i]
            pos += 2
        else:
            result[neg] = arr[i]
            neg += 2
            
    return result


arr = [1, 2, -4, -5]
print(rearrangeArrayElements(arr))
