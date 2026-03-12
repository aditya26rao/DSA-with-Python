def palindromOrNot(s, index=0):
    
    # return Str == Str[::-1] # in-built method so it has TC and SC is O(1)

    # Method 1: Iterative two-pointer (O(n), O(1))
    # left, right = 0, len(s) - 1
    # while left < right:
    #     if not s[left].isalnum():
    #         left += 1
    #     elif not s[right].isalnum():
    #         right -= 1
    #     elif s[left].lower() != s[right].lower():
    #         return False
    #     else:
    #         left += 1
    #         right -= 1
    # return True

    # Method 2: Recursive (O(n), O(n) due to call stack)
    n = len(s)
    if index >= n // 2:
        return True
    if s[index] != s[n - index - 1]: 
        return False
    return palindromOrNot(s, index + 1)


Str = "ABCDCBA"
print(palindromOrNot(Str))  # Output: True
