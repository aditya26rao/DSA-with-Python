rows = 5

for i in range(rows):
    alpha = 65
    for j in range(rows - i - 1):
        print(" ",end=' ')
    for k in range(2 * i + 1):
        print(chr(alpha),end=' ')
        alpha += 1

    print()
    

'''
        A 
      A B C 
    A B C D E
  A B C D E F G
A B C D E F G H I
'''

