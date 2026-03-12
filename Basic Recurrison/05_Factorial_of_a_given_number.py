def factorialNumber(num):
    # for this TC and Sc is O(n)
    if num == 0:
        return 1
    
    return num * factorialNumber(num - 1)
    
    
num = 5
print(factorialNumber(num))