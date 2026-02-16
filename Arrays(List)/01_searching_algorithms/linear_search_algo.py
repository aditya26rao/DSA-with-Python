def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [20, 40, 70, 10, 12, 11, 29, 75, 46]
x = int(input("Enter the element you want to search:- "))
result = linear_search(arr, x)
print(f"The element found at the index of:- {result}")
