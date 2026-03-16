# Method: Two Pointer Approach
# Time Complexity (TC): O(n)
#   We traverse the array once
#
# Space Complexity (SC): O(n)
#   Result array of size n


def sortedSquares(nums):

    n = len(nums)

    # Result array
    result = [0] * n

    # Two pointers
    left = 0
    right = n - 1

    # Position to fill in result
    pos = n - 1

    while left <= right:

        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2

        # Place larger square at current position
        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1

        pos -= 1

    return result


nums = [-4,-1,0,3,10]
print(sortedSquares(nums))