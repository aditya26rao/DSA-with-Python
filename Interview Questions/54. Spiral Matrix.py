def spiralMatrix(matrix):
    # TC O(m*n) and SC O(1) without o/p, without O(m*n)
    # Initialize boundaries
    top, left = 0, 0
    bottom, right = len(matrix) - 1, len(matrix[0]) - 1
    result = []

    while left <= right and top <= bottom:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse from right to left (if still valid)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse from bottom to top (if still valid)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


# Example
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralMatrix(matrix))  # Output: [1,2,3,6,9,8,7,4,5]
