def removeDuplicates(nums):
    # Method 1:- Brute Force 
    # TC: O(n) average, since each lookup/insertion in a set is O(1)
    # SC: O(n) in worst case, when all elements are unique
    # setSet = set()
    # for num in nums:
    #     if num not in setSet:
    #         setSet.add(num)
    
    # Overwrite nums with the set contents
    # Note: sets are unordered, so this may not preserve sorted order
    # nums[:] = setSet
    #return nums
    
    # Method 2:- Optimal Sol with Two Pointer approach:- Tc O(n) and SC O(1)
    # If list is empty, return 0
    if not nums:
        return 0

    i = 0
    # Traverse list starting from second element
    for j in range(1, len(nums)):
        # If current element is different from last unique one
        if nums[j] != nums[i]:
            # Move pointer forward
            i += 1
            # Place the unique element in next position
            nums[i] = nums[j]

    # i is last index of unique element, count = i + 1
    return nums
    
nums = [1,1,2,2,3,3]
print(removeDuplicates(nums))  
