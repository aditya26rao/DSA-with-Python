def printNums(current,n):
    if current > n: # base condition
        return
    print(current, end=' ') # print first
    printNums(current + 1, n) # recursion call
    
n = 10
print(printNums(1,n))