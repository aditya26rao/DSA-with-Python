def reverse(nums,start,end):
    while start < end:
        nums[start],nums[end] = nums[end],nums[start]
        start += 1
        end -= 1

def rotate(nums, k):
    
    n = len(nums)
    k = k % n
    
    # Better Sol:- TC O(n) and SC O(k)
    # if n <= 1 or k == 0:
    #     return

    # temp = nums[-k:]

    # for i in range(n - k - 1, -1, -1):
    #     nums[i+k] = nums[i]

    # nums[:k] = temp
    
    # Optimal Sol:- TC O(n) and SC O(1)
    if n == 0 or k == 0:
        return nums
    
    reverse(nums,0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k , n - 1)
    
    return nums
    

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate(nums,k))