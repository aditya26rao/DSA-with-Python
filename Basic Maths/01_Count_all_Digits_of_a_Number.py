def count_num(num):
    count = 0
    # Method 1 :- Time complexity O(n) and Space complexity is O(1)
    # while num > 0:
    #     num = num // 10 # removes the last digit and counting the count
    #     count += 1
    # return count
    
    # Method 2 :- Time Complexity O(n) and Space complexity is O(n)
    for n in str(num):
        count += 1
    return f"No of the counts are: {count}"

num = 12345
print(count_num(num))


