def countFrequency(s, queries):
    # Optimal Solution for Character Hashing
    # --------------------------------------
    # Time Complexity (TC): O(n + m)
    #   -> O(n) to traverse the string (n = len(s))
    #   -> O(m) to answer queries (m = len(queries))
    #
    # Space Complexity (SC): O(1)
    #   -> Fixed-size hashList of 26 for lowercase letters
    #   -> Independent of input size, constant space
    #
    # This is the optimal solution because the alphabet size is constant (26).
    # --------------------------------------

    # generate the hashList
    hashList = [0] * 26
    hashDict = {}

    # prestoring the values in hashList
    for ch in s:
        ascii_value = ord(ch)
        index = ascii_value - ord('a')
        hashList[index] += 1

    # matching the hashList for queries
    for q in queries:
        ascii_value = ord(q)
        index = ascii_value - ord('a')
        hashDict[q] = hashList[index]

    return hashDict


s = 'azyxyyzaaaa'
queries = ['d', 'a', 'y', 'x']
print(countFrequency(s, queries))
