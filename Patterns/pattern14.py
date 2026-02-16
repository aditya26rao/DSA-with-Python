rows = 5

for i in range(1,rows + 1):
    alpha = 65 # for every loop it is setting alpha has 65
    for j in range(1, i + 1):
        print(chr(alpha),end= " ")
        alpha += 1
    print()



'''
A 
A B 
A B C
A B C D
A B C D E

'''