from itertools import permutations


def next_permutation(nums):
    # Method 1:= Brute Force:- TC 𝑂(𝑛! * 𝑛 log 𝑛) and SC O(n! * n)
    # permutation = list(permutations(nums))
    # permutation.sort()
    # for i in range(len(permutation)):
    #     if list(permutation[i]) == nums:
    #         if i == len(permutation) - 1:
    #             return permutation[0]

    #         return list(permutation[i + 1])
        
    # Optimal Solution:
    
    pivot = -1
    n = len(nums)
    for i in range(n-2,-1,-1):
        if nums[i] < nums[i+1]:
            pivot = i
            break
        
    if pivot == -1:
        nums.reverse()
        return nums
    
    for i in range(n-1,pivot,-1):
        if nums[i] > nums[pivot]:
            nums[pivot],nums[i] = nums[i],nums[pivot]
            break
        
    i = pivot + 1
    j = n - 1
    
    while i <= j:
        nums[i],nums[j] = nums[j],nums[i]
        i += 1
        j -= 1
        
    return nums
    

nums = [1, 3, 2]
print(next_permutation(nums))
