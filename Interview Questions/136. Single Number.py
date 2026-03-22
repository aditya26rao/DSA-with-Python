def singleNumber(nums):
    xor = 0

    for num in nums:
        xor = xor ^ num

    return xor

nums = [2,1,1]
print(singleNumber(nums))