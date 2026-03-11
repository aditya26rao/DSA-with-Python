# Time Complexity is O(n) and Space Complexity is O(1)

def palindrome_num(num):
    tempNum  = num
    palindromeNum = 0
    while tempNum > 0:
        lastDigit = tempNum % 10
        palindromeNum = palindromeNum * 10 + lastDigit
        tempNum //= 10
    return True if palindromeNum == num else False 
num = 4554
print(palindrome_num(num))
