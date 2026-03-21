def union_of_two_sorted_array(nums1,nums2):
    
# Method 1: Brute Force
# TC: O((n1 + n2) * k) because "x not in result" is linear search
# SC: O(n1 + n2)
    # result = []
    
    # for i in range(len(nums1)):
    #     if nums1[i] not in result:
    #         result.append(nums1[i])
            
    # for j in range(len(nums2)):
    #     if nums2[j] not in result:
    #         result.append(nums2[j])
            
    # return result
            
    
# Method 2: Better Solution - Using Set
# TC: O(n1 + n2) average in Python (hash set)
#     O(n1 log n1 + n2 log n2) in theory (BST-based set)
# SC: O(n1 + n2)

    # n1 = len(nums1)
    # n2 = len(nums2)
    # setSet = set()
    # uninon = []
    
    # for i in range(n1): # O(n1logn)
    #     setSet.add(nums1[i])
        
    # for i in range(n2): # O(n2logn)
    #     setSet.add(nums2[i])
        
    # uninon[ : ] = setSet # O(n1 + n2)
    
    # return uninon 
    
    
# Method 3: Better Solution - Using HashMap
# TC: O(n1 + n2)
# SC: O(n1 + n2)

    # hashMap = {}
    
    # for num in nums1:
    #     hashMap[num] = hashMap.get(num,0) + 1
    
    # for num in nums2:
    #     hashMap[num] = hashMap.get(num, 0) + 1
        
    # Uninon = list(hashMap.keys())
    
    # return Uninon
    

# Method 4: Optimal Solution - Two Pointer (for sorted arrays)
# TC: O(n1 + n2)
# SC: O(1) extra (apart from output), with Output by returning it would be SC O(n1 + n2)
    uninon_list = []   # final result list to store union elements
    i = j = 0          # two pointers, one for nums1 and one for nums2

    # Traverse both arrays simultaneously
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            # If nums1[i] is smaller, add it if not already added
            if not uninon_list or uninon_list[-1] != nums1[i]:
                uninon_list.append(nums1[i])
            i += 1
        elif nums2[j] < nums1[i]:
            # If nums2[j] is smaller, add it if not already added
            if not uninon_list or uninon_list[-1] != nums2[j]:
                uninon_list.append(nums2[j])
            j += 1
        else:
            # If both are equal, add one of them (avoid duplicates)
            if not uninon_list or uninon_list[-1] != nums1[i]:
                uninon_list.append(nums1[i])
            i += 1
            j += 1

    # Add remaining elements from nums1 (if any)
    while i < len(nums1):
        if not uninon_list or uninon_list[-1] != nums1[i]:
            uninon_list.append(nums1[i])
        i += 1

    # Add remaining elements from nums2 (if any)
    while j < len(nums2):
        if not uninon_list or uninon_list[-1] != nums2[j]:
            uninon_list.append(nums2[j])
        j += 1

    return uninon_list   # return the union of both arrays


nums1 = [1,1,3,3,4,5]
nums2 = [2,3,4,4,5,6]
print(union_of_two_sorted_array(nums1,nums2))