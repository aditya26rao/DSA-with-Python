def fibonacciNumber(num):
    # Method 1:-  Better Sol :- TC O(n) and SC O(1)
    # a, b = 0, 1
    
    # for i in range(num + 1):
    #     print(a, end=' ')
    #     a, b = b, a + b
    
    # Method 2:- Optimal Sol :- TC O(2^n) and SC O(n)
    if num <= 1:
        return num
        
    return fibonacciNumber(num - 1) + fibonacciNumber(num - 2)
    

num = 6
print(fibonacciNumber(num))  
