def checkPrimeNum(n):
    count = 0
    
    # Method 1 BruteForce :- Tc O(n) and Sc O(1)
    # for i in range(1, n + 1):
    #     if n % i == 0:
    #         count += 1
    # return count == 2
    
    # Method 2 Optimal SOl :- TC O(sqrt(N)), SC O(1)
    for i in range(1, int( n ** 0.5) + 1):
        if n % i == 0:
            count += 1
            
            if i != n // i:
                count += 1
    return count == 2
 
n = 2
print(checkPrimeNum(n))