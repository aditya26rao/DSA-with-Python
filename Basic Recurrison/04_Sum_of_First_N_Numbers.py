def sumOfNumbers(num):
    if num == 1 or num == 0:
        return num
    
    # return num * (num + 1)//2 # TC and SC is O(1)
    
    return num + sumOfNumbers(num - 1) # TC and SC is O(n)

num = 6
print(sumOfNumbers(num))
