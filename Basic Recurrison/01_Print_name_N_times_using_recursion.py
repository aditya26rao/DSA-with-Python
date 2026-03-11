def print_Ntimes(name, n, count=0):
    if count == n:   # base case
        return
    print(name)      # print first
    print_Ntimes(name, n, count + 1)  # recursive call

    
n,name,count = 3, 'aditya',0
print(print_Ntimes(name,n,count))