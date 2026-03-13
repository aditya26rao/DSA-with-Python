# from collections import Counter

# # Approach 2 - Dictionary based data structure
# # TC :- O(n)
# # SC :- O(n)
# def majorityElement(nums):
#     n = len(nums)

#     # Count frequency of each element
#     counts = Counter(nums)
#     print(counts)

#     # Return the key with maximum frequency
#     return max(counts.keys(), key=counts.get)


# # Driver code
# nums = [2, 2, 1, 1, 1, 2, 2]
# result = majorityElement(nums)
# print(f"The Majority Element is:- {result}")


# Approach 3 - Boyer Moore Voting Algorithm
# TC :- O(n)
# SC :- O(1)

def findCandidate(nums):
    count = 0
    candidate = None

    # First pass: find a potential candidate
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    return candidate


def isMajority(nums, candidate):
    count = 0
    n = len(nums)

    # Second pass: verify if candidate is actually majority
    for i in range(n):
        if nums[i] == candidate:
            count += 1

    # Majority element must appear more than n/2 times
    if count > n / 2:
        return 1
    else:
        return 0


def majorityElement(nums):
    # Step 1: Find candidate
    cand = findCandidate(nums)

    # Step 2: Verify candidate
    if isMajority(nums, cand):
        print("Majority Element in an array is", cand)
    else:
        print("No Majority element exists in an array")


# Driver code
# nums = [2, 2, 1, 1, 1, 2, 2]
nums = [2, 2, 7, 3, 4]
majorityElement(nums)