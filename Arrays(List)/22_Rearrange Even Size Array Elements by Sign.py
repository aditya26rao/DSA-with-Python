def rearrangeArrayElements(arr):
    # -------------------------------
    # Method 1: Brute Force
    # TC: O(n + n/2) ≈ O(n)
    # SC: O(n + n/2) ≈ O(n)
    # -------------------------------
    # n = len(arr)
    # pos_arr = []
    # neg_arr = []
    #
    # for i in range(n):
    #     if arr[i] > 0:
    #         pos_arr.append(arr[i])
    #     else:
    #         neg_arr.append(arr[i])
    #
    # for i in range(n // 2):
    #     arr[2 * i] = pos_arr[i]
    #     arr[2 * i + 1] = neg_arr[i]
    #
    # return arr

    # -------------------------------
    # Method 2: Optimal Solution (In-place style using index tracking)
    # TC: O(n)
    # SC: O(n) (result array)
    # -------------------------------
    
    n = len(arr)
    result = [0] * n
    pos = 0  # even indices for positives
    neg = 1  # odd indices for negatives

    for num in arr:
        if num > 0:
            result[pos] = num
            pos += 2
        else:
            result[neg] = num
            neg += 2

    return result


# Example usage
arr = [1, 2, -4, -5]
print(rearrangeArrayElements(arr))  # Output: [1, -4, 2, -5]
