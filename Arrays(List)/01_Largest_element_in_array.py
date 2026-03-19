def largestElement(nums):
    # Method 1:- Brute Force :- TC O(nlogn), SC O(1)
    # nums.sort()
    # return nums[-1]

    # Method 2:- Optiaml Sol :- TC O(n) and SC O(1)
    maxElement = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > maxElement:
            maxElement = nums[i]

    return maxElement


nums = [2, 5, 1, 3, 0]
print(largestElement(nums))
