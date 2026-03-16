# Method: Merge Sort + Two Pointer
# Time Complexity (TC): O(n log n)
#   Sorting takes O(n log n)
#   Two pointer traversal takes O(n)
#
# Space Complexity (SC): O(1)
#   Ignoring sorting space


def count_pairs_less_than_target(nums, target):

    # Step 1: Sort the array
    nums.sort()

    left = 0
    right = len(nums) - 1
    count = 0

    # Step 2: Two pointer traversal
    while left < right:

        current_sum = nums[left] + nums[right]

        # If pair sum is less than target
        if current_sum < target:

            # All elements between left and right form valid pairs
            count += (right - left)

            # Move left pointer
            left += 1

        else:
            # Move right pointer
            right -= 1

    return count


nums = [-1,1,2,3,1]
target = 2

print(count_pairs_less_than_target(nums, target))