def moveZeroes(nums):
    # Brute Force (Two Pointer Swap): O(n), O(1), but order not preserved.
    # Use Case 1:- if sort is not need , we can do Two Poninter: TC O(n) and O(1)
    # n = len(nums)
    # left = 0
    # right = n - 1

    # while left < right:
    #     # If left is zero, swap with right
    #     if nums[left] == 0 and nums[right] != 0:
    #         nums[left], nums[right] = nums[right], nums[left]
    #         left += 1
    #         right -= 1
    #     # If left is non-zero, just move forward
    #     elif nums[left] != 0:
    #         left += 1
    #     # If right is zero, just move backward
    #     elif nums[right] == 0:
    #         right -= 1
    #     else:
    #         # If both are non-zero, move both pointers
    #         left += 1
    #         right -= 1

    # return nums
    
    
    # Better Solution (Overwrite Method): O(n), O(1), order preserved 
    # Use Case 2 :- if we need sorted at last ,Time Complexity (TC): O(n) , Space Complexity (SC): O(1) 
    # last_non_zero_found_at = 0
    
    # for i in range(len(nums)):
    #     if nums[i] != 0:
    #         nums[last_non_zero_found_at] = nums[i]
    #         last_non_zero_found_at += 1
            
    # for i in range(last_non_zero_found_at, len(nums)):
    #     nums[i] = 0
    
    # return nums
    
    # Method 3: Brute Force but Order is preserved, TC O(n), SC O(x), x is no_of_zeroz, if worst case SC is O(n)
    # temp = []
    
    # for i in range(len(nums)):
    #     if nums[i] != 0:
    #         temp.append(nums[i])
    
    # for i in range(len(temp)):
    #     nums[i] = temp[i]
    
    # no_zeros = len(temp)
    
    # for i in range(no_zeros,len(nums)):
    #     nums[i] = 0
        
    # return nums
    
    # Method 4:- Optimal Sol :- TC O(n) and SC O(1)
    j = -1
    for i in range(len(nums)): # find first zero, this part is O(x),
        if nums[i] == 0:
            j = i
            break
    for i in range(j+1,len(nums)): # swap subsequent non-zeros forward, this part is O(n - x)
        if nums[i] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            j += 1
    return nums  # overall TC is O(n - x + x) => O(n)
    
nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums)) 
