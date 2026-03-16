# Method 1: Better Solution (Two Pointer Technique)
# Time Complexity: O(n + m)
#   We traverse both arrays once using two pointers.
#
# Space Complexity: O(1)
#   No extra space is used except the result array.


def intersection_of_two_array(nums1, nums2):

    # List to store intersection elements
    result = []

    # Initialize two pointers for nums1 and nums2
    i, j = 0, 0
    
    # Traverse both arrays until one pointer reaches the end
    while i < len(nums1) and j < len(nums2):
        
        # Case 1: If both elements are equal
        # We found a common element
        if nums1[i] == nums2[j]:

            # Avoid adding duplicates to the result
            # Since arrays are sorted, duplicates appear consecutively
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])

            # Move both pointers forward
            i += 1
            j += 1
            
        # Case 2: If element in nums1 is smaller
        # Move pointer i to reach a larger element
        elif nums1[i] < nums2[j]:
            i += 1
            
        # Case 3: If element in nums2 is smaller
        # Move pointer j forward
        else:
            j += 1
            
    # Return the intersection array
    return result


# Input arrays (sorted)
nums1 = [1,2,2,3]
nums2 = [2,2,4]

# Function call
print(intersection_of_two_array(nums1, nums2))