def rotateArray_K_Elements(nums, k, direction):
    # Time Complexity (TC): O(n)
    # Space Complexity (SC): O(k) → O(n) in worst case
    n = len(nums)
    k = k % n

    if direction == "left":
        temp = nums[:k]

        for i in range(k, n):
            nums[i - k] = nums[i]

        nums[n - k :] = temp

    elif direction == "right":

        temp = nums[-k:]

        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]

        nums[:k] = temp

    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
d = int(input("Enter the number of elements to rotate: "))
dir_choice = input("Enter direction (left/right): ").strip().lower()
print(rotateArray_K_Elements(nums, d, dir_choice))
