def nextPermutation(nums):
    pivot = -1
    n = len(nums)
    # to find pivot element
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break

    if pivot == -1:
        nums.reverse()
        return nums
    # if i > pivot , swap immediate element
    for i in range(n - 1, pivot, -1):
        if nums[i] > nums[pivot]:
            nums[i], nums[pivot] = nums[pivot], nums[i]
            break

    i = pivot + 1
    j = n - 1

    while i <= j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    return nums


nums = [1, 3, 2]
print(nextPermutation(nums))
