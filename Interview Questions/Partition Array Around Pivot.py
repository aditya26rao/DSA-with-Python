def partition(nums, pivot):
    # Better solution :- Time complexity: O(n) ,Space complexity: O(n)
    left = []
    middle = []
    right = []
    
    for num in nums:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            middle.append(num)
        else:
            right.append(num)

    return left + middle + right       
    

nums = [9,12,3,5,14,10,10]
print(partition(nums,10))