def secondLargestElement(nums):
    # Method 1:- Brute Force :- TC O(n logn), SC O(1)
    # nums.sort()
    # largest = nums[-1]
    # second_largest = 0
    # for i in range(len(nums) - 2, -1 , -1):
    #     if nums[i] != largest:
    #         second_largest = nums[i]
    #         break
    # return second_largest if second_largest else -1
    
    
    # Method 2 :- Better Sol :- TC :- O(n + n) => O(2n), SC O(1)
    # if len(nums) < 2:
    #     return -1  # Not enough elements
    
    # largestEle = nums[0]
    # secondLargestEle = float('-inf')
    
    # # Find largest element
    # for i in range(1, len(nums)):
    #     if nums[i] > largestEle:
    #         largestEle = nums[i]
    
    # # Find second largest element
    # for i in range(len(nums)):
    #     if nums[i] > secondLargestEle and nums[i] != largestEle:
    #         secondLargestEle = nums[i]
    
    # # Handle case where all elements are equal
    # return secondLargestEle if secondLargestEle != float('-inf') else -1
    
    
    # Method 3:- Optimal Sol :- TC  O(n) and SC O(1)
    if len(nums) < 2:
        return -1  # Not enough elements
    
    largest = second_largest = float('-inf')
    
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest if second_largest != float('-inf') else -1


nums = [1,2,4,7,7,5]
print(secondLargestElement(nums))