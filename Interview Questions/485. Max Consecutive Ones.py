
def findMaxConsecutiveOnes(nums):
    # Optimal SOl:- TC O(n) and SC  O(1)
    count = 0
    maxi = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            maxi = max(maxi,count)
        else:
            count = 0
    return maxi

nums = [1,1,0,1,1,1,0,1,1]
print(findMaxConsecutiveOnes(nums))