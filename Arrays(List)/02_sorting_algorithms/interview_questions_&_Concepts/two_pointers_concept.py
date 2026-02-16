# TC -> O(n)
# SC -> O(1)

def sortColors(nums):
    # p0 -> pointer for placing 0s (left side)
    # current -> pointer to traverse the array
    # p2 -> pointer for placing 2s (right side)
    p0 = current = 0
    p2 = len(nums) - 1

    # Traverse until current crosses p2
    while current <= p2:
        # If current element is 0
        if nums[current] == 0:
            # Swap current element with p0 position
            nums[current], nums[p0] = nums[p0], nums[current]
            p0 += 1          # move p0 forward
            current += 1     # move current forward

        # If current element is 2
        elif nums[current] == 2:
            # Swap current element with p2 position
            nums[current], nums[p2] = nums[p2], nums[current]
            p2 -= 1          # move p2 backward
            # current is NOT incremented here
            # because swapped value needs to be checked

        # If current element is 1
        else:
            # Just move current pointer
            current += 1

    return nums


nums = [2, 0, 2, 1, 1, 0]
result = sortColors(nums)
print(f"The sorted numbers are:- {result}")