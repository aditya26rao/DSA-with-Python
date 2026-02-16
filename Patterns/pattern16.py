rows = 5

alpha = 65

for i in range(1,rows + 1):
    for j in range(1, i + 1):
        print(chr(alpha),end= " ")
    alpha += 1
    print()

'''
A
B B
C C C
D D D D
E E E E E

'''