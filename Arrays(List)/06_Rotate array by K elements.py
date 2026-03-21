def reverse(nums,start,end):
    while start < end:
        nums[start],nums[end] = nums[end],nums[start]
        start += 1
        end -= 1
def rotateArray_K_Elements(nums, k, direction):
    # Method 1: Better Solution 
    # Time Complexity (TC): O(n)
    # Space Complexity (SC): O(k) → O(n) in worst case
    
    # n = len(nums)
    # k = k % n
    
    # # base condition
    # if n <= 1 or k % n == 0:
    #     return 
    

    # if direction == "left":
    #     temp = nums[:k]

    #     for i in range(k, n):
    #         nums[i - k] = nums[i]

    #     nums[n - k :] = temp

    # elif direction == "right":

    #     temp = nums[-k:]

    #     for i in range(n - k - 1, -1, -1):
    #         nums[i + k] = nums[i]

    #     nums[:k] = temp

    # return nums
    
    
    # Method 2:
    n = len(nums)
    k = k % n   # Normalize k so it never exceeds array length

# Base condition: if array is empty or no rotation needed
    if n == 0 or k == 0:
        return nums

    if direction == 'left':
        # Step 1: Reverse the first k elements
        reverse(nums, 0, k - 1)
        # Step 2: Reverse the remaining n-k elements
        reverse(nums, k, n - 1)
        # Step 3: Reverse the entire array to complete left rotation
        reverse(nums, 0, n - 1)

    elif direction == 'right':
        # Step 1: Reverse the entire array
        reverse(nums, 0, n - 1)
        # Step 2: Reverse the first k elements (which were originally the last k)
        reverse(nums, 0, k - 1)
        # Step 3: Reverse the remaining n-k elements
        reverse(nums, k, n - 1)

    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
d = int(input("Enter the number of elements to rotate: "))
dir_choice = input("Enter direction (left/right): ").strip().lower()
print(rotateArray_K_Elements(nums, d, dir_choice))
