def checkAnagrams(str1, str2):
    # Optimal Solution: Using Hash Maps (Dictionaries)
    # Time Complexity: O(n + m)
    #   - O(n) to build frequency dictionary for str1
    #   - O(m) to build frequency dictionary for str2
    #   - O(m) to compare both dictionaries
    #   => Total = O(n + m)
    #
    # Space Complexity: O(m)
    #   - Two dictionaries storing counts of unique characters
    #   - Space grows with number of distinct characters, not constant

    # Step 1: Quick check – if lengths differ, they cannot be anagrams
    if len(str1) != len(str2):
        return False
    
    # Step 2: Build frequency dictionary for str1
    freq1 = {}
    for ch in str1:
        freq1[ch] = freq1.get(ch, 0) + 1           

    # Step 3: Build frequency dictionary for str2
    freq2 = {}
    for ch in str2:
        freq2[ch] = freq2.get(ch, 0) + 1     
    
    # Step 4: Compare both frequency maps
    # If they are identical, the strings are anagrams
    if freq1 == freq2:
        return True
    else:
        return False      

# Example Run
str1, str2 = 'listen', 'slient'
print(checkAnagrams(str1, str2))  # Output: True
