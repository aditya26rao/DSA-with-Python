rows = 5

for i in range(rows,0,-1):
    alpha = 65
    for j in range(i):
        print(chr(alpha),end=' ')
        alpha += 1
    print()
    
'''
A B C D E 
A B C D 
A B C
A B
A

'''