# Time complexity is O(n) and Space compelxity is O(1)
def amstrongNum(n):
    tempNum = n
    digits = len(str(n))
    amstrong_num = 0
    while n > 0:
        lastDigit = n % 10
        amstrong_num = lastDigit ** digits + amstrong_num
        n //= 10
    return True if amstrong_num == tempNum else False

 
N = 153
print(amstrongNum(N))