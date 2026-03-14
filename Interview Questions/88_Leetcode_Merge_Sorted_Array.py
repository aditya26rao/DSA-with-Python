def merge(nums1, m, nums2, n):
    # Method 1:= Better Sol and Good 
    # TC and SC is same O(m+n)
    # result = []
    
    # i,j = 0, 0
    
    # while i < m and j < n:
    #     if nums1[i] <= nums2[j]:
    #         result.append(nums1[i])
    #         i += 1
    #     else:
    #         result.append(nums2[j])
    #         j += 1
            
    # while i < m:
    #     result.append(nums1[i])
    #     i += 1   

    # while j < n:
    #     result.append(nums2[j])
    #     j += 1
        
    # # for i in range(m+n):
    # #     nums1[i] = result[i] 
    
    # nums1[:m+n] = result
        
    # return nums1  
    
    # Method 2:- Optimal Sol : where i get TC O(m+n) and SC as O(1)
    
    p1 = m - 1 # last valid element in nums1
    p2 = n - 1 # end of nums2
    p = m + n - 1 # end of nums1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1  
    
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p -= 1
        p2 -= 1
        
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1,m,nums2,n))
