def findIntersection(arr1, arr2):
    # TC: O(n + m)
    # SC: O(n)

    # hashDict will store the frequency of elements in arr1
    hashDict = {}

    # List to store the intersection elements
    intersectionList = []
    
    # Step 1: Count frequency of each element in arr1
    # TC: O(n)
    for num in arr1:
        # get(num, 0) returns 0 if num is not present
        hashDict[num] = hashDict.get(num, 0) + 1
        
    # Step 2: Traverse arr2 and check if element exists in hashDict
    # TC: O(m)
    for num in arr2:
        # If element exists in arr1 and frequency > 0
        if num in hashDict and hashDict[num] > 0:
            intersectionList.append(num)   # add element to result
            hashDict[num] -= 1             # decrease frequency
            
    # Return intersection list if not empty, otherwise False
    return intersectionList if intersectionList else False
    

arr1, arr2 = [1,2,1,2], [2,2]
print(findIntersection(arr1, arr2))