def oddSizeRearrange(nums):
    # -------------------------------
    # TC: O(n) + O(min(pos,neg)) + O(leftovers) ≈ 𝑂(𝑛)
    # SC: O(n) (extra arrays for pos/neg + result)
    # -------------------------------
    pos = []
    neg = []

    # Split positives and negatives
    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)

    result = []
    i = j = 0

    # Alternate until one list runs out
    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1

    # Add leftovers (if positives > negatives or vice versa)
    while i < len(pos):
        result.append(pos[i])
        i += 1

    while j < len(neg):
        result.append(neg[j])
        j += 1

    return result


# Example usage
nums = [-1, 2, 3, 4, -3, 1]
print(oddSizeRearrange(nums))  # Output: [2, -1, 3, -3, 4, 1]
