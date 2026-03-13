# def groupAnagrams(arr):
#     # Method 1:= Approach Better Sol / Brute Force: HashMap + Sorted String Key
#     # Words that are anagrams will have the same sorted characters.
#     # Example: "eat", "tea", "ate" -> sorted -> "aet"

#     groupMap = {}  # Dictionary to store groups of anagrams

#     # Traverse all words in the array
#     for word in arr:
#         # Generate key by sorting characters of the word
#         # TC of sorting each word = O(K log K)
#         key = ''.join(sorted(word))
        
#         # If this key is not present in hashmap, create new group
#         if key not in groupMap:
#             groupMap[key] = []
            
#         # Add the word to its corresponding anagram group
#         groupMap[key].append(word)

#     # Return grouped anagrams
#     return list(groupMap.values())


# # Input
# arr = ["eat","tea","tan","ate","nat","bat"]

# # Function call
# print(groupAnagrams(arr))


# # Time Complexity (TC): O(N * K log K)
# # N = number of words in the list
# # K = maximum length of a word
# # Reason: we sort each word which takes K log K time

# # Space Complexity (SC): O(N * K)
# # Reason: storing all words inside hashmap groups


def groupAnagrams(arr):
    # Method 2 := Optimal Approach: HashMap + Character Frequency Key
    # Instead of sorting, we count characters (26 letters)
    # TC is O(N * K), SC is O(N * K)
    groupMap = {}

    for word in arr:
        # Create frequency array for 26 lowercase letters
        freq = [0] * 26
        
        # Count characters
        for ch in word:
            ascii_value = ord(ch)
            index = ascii_value - ord('a')
            freq[index] += 1
        
        # Convert list to tuple so it can be used as dictionary key
        key = tuple(freq)

        # Create new group if key not present
        if key not in groupMap:
            groupMap[key] = []

        # Append word to its anagram group
        groupMap[key].append(word)

    return list(groupMap.values())


arr = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(arr))