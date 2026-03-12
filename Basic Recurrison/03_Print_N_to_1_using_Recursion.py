def printNums(n,current):
    if current < n:
        return
    
    print(current, end=' ')
    
    printNums(n,current - 1)
    

n = 1 
print(printNums(n,10))