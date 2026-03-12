def basicHashing(n, m):
    # Method 1 :- Brute Force :- TC O(M * N) and SC O(1)
    # hashDict = {}
    # for num in m:
    #     count = 0
    #     for check in n:
    #         if num == check:
    #             count += 1
    #     hashDict[num] = count

    # return hashDict

    # Method 2 :- Optimal Sol :- Which is actually Hashing, prestoring values and assgin it
    # TC O(m + n), SC O(1) or SC O(len(m))

    # Pre-store frequencies based on max element in n
    max_val = max(n) if n else 0
    hashList = [0] * (max_val + 1)  # size depends on n
    hashDict = {}

    # Precompute frequencies // Prestoring the values
    for num in n:
        hashList[num] += 1

    # Fetch results for queries
    for check in m:
        if check < 0 or check > max_val:
            hashDict[check] = 0
        else:
            hashDict[check] = hashList[check]
    return hashDict


n = [1, 2, 1, 3, 2]
m = [1, 3, 4, 2, 10]
print(basicHashing(n, m))
