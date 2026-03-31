def setMatrixZeroes(nums):
    # Method 1:- Brute Force
    # Time Complexity: O(m ⋅ n ⋅ (m + n)) + O(m ⋅ n) ≈ O(m ⋅ n ⋅ (m + n))
    # SC O(1) in best and O(n) in worst
    # Overall TC O(m*n) and SC O(n)
    # def markRow(i):
    #     for j in range(len(nums)):
    #         if nums[i][j] != 0:
    #             nums[i][j] = -1

    # def markCol(j):
    #     for i in range(len(nums)):
    #         if nums[i][j] != 0:
    #             nums[i][j] = -1

    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if nums[i][j] == 0:
    #             markRow(i)
    #             markCol(j)

    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if nums[i][j] == -1:
    #             nums[i][j] = 0

    # return nums

    # Method 2:- Better Solution
    # TC O(2*m*n) and SC O(n) + O(m)
    # overall TC O(m*n) and SC O(m+n)
    # m = len(nums)
    # n = len(nums[0])

    # row = [0] * m
    # col = [0] * n

    # for i in range(m):
    #     for j in range(n):
    #         if nums[i][j] == 0:
    #             col[j] = 1
    #             row[i] = 1

    # for i in range(m):
    #     for j in range(n):
    #         if row[i] == 1 or col[j] == 1:
    #             nums[i][j] = 0

    # return nums

    # Method 3:- Optimal Sol
    # TC O(m*n) and SC O(1)
    rows = len(nums)
    cols = len(nums[0])
    col0 = 1
    
    # Step 1: Marking
    for i in range(rows):
        for j in range(cols):
            if nums[i][j] == 0:
                nums[i][0] = 0
                if j != 0:
                    nums[0][j] = 0
                else:
                    col0 = 0
    
    # Step 2: Applying marks (start from 1,1)
    for i in range(1, rows):
        for j in range(1, cols):
            if nums[i][j] != 0:
                if nums[0][j] == 0 or nums[i][0] == 0:
                    nums[i][j] = 0
    
    # Step 3: Handle first row
    if nums[0][0] == 0:
        for j in range(cols):
            nums[0][j] = 0
    
    # Step 4: Handle first column
    if col0 == 0:
        for i in range(rows):
            nums[i][0] = 0
    
    return nums



nums = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
print(setMatrixZeroes(nums))
