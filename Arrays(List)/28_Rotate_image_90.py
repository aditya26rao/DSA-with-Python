def rotateMatrix(matrix):
    # Method 1:- Brute Force :- TC O(n^2) and SC O(n^2)
    # rows = len(matrix)
    # cols = len(matrix[0])
    
    # result = [[0] * rows for _ in range(cols)]
    
    # for i in range(rows):
    #     for j in range(cols):
    #         result[j][rows - i - 1] = matrix[i][j]
 
    # return result


    # Method 2 :- Optimal Solution
    # TC O(n^2) and SC O(1)
    n = len(matrix)
    
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
    
    return matrix
    
matrix =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(rotateMatrix(matrix))