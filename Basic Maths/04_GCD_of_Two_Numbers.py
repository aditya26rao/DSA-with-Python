# Time complexity is O(n) and Space compelxity is O(1)
def gcdNumbers(n1,n2):
    gcd = 1
    for i in range(1, min(n1,n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd
    
N1 = 9
N2 = 12
print(gcdNumbers(N1,N2))