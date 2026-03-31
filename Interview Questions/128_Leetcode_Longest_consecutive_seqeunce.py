def longestConsecutive(arr):
    #code here
    # TC O(n) and SC O(1) in best or SC O(n) in worst
    n = len(arr)
    
    if n == 0: return 0
    
    hashSet = set(arr)
    longest = 0
    
    
    for item in hashSet:
        if item - 1 not in hashSet:
            count = 1
            x = item
            
            while x + 1 in hashSet:
                x += 1
                count += 1
                
            longest = max(longest,count)
            
            
            
    return longest

nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))