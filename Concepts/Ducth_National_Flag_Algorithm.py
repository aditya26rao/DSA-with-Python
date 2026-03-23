# Method: Dutch National Flag Algorithm (Optimal)
# Time Complexity (TC): O(n)  -> single pass through the array
# Space Complexity (SC): O(1) -> in-place, only pointers used

def dutchNationalFlag(nums):
    low = 0
    high = len(nums) - 1
    mid = 0
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        else:  # nums[mid] == 1
            mid += 1
            
    return nums

nums = [2, 0, 2, 1, 1, 0]
result = dutchNationalFlag(nums)
print(f"The sorted numbers are:- {result}")
