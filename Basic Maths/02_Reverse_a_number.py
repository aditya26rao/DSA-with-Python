# Time complexity is O(n) and Space compelxity is O(1)
def reverse_num(num):
    rev = 0
    while num > 0: 
        lastDigit = num % 10
        rev = rev * 10 + lastDigit
        num = num // 10
    return rev
    
num = 12345
print(reverse_num(num))