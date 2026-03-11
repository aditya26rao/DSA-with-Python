def divisiorsNum(n):
    listDivisiors = []
    
    # Method 1 BruteForce :- TC O(n) and SC O(n)
    # for i in range(1, n + 1):
    #     if n % i == 0:
    #         listDivisiors.append(i)
    # return listDivisiors
    
    import math
    # Method 2 Optimal Sol :- TC O(sqrt(N)), SC O(2*sqrt(N)),
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            listDivisiors.append(i)
            
            if i != n // i:
                listDivisiors.append(n // i)
                
    return sorted(listDivisiors)

n = 36
print(divisiorsNum(n))