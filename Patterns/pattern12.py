rows = 4
space = 2*(rows-1)

for i in range(1,rows + 1):
    # numbers
    for j in range(1,i+1):
        print(j,end="")
    
    #spaces
    for j in range(space):
        print(' ',end="")
    
    # numbers 
    for j in range(i,0,-1):
        print(j,end="")
        
    print()
    space -= 2
    
'''
1      1
12    21
123  321
12344321


[numbers,spaces,nunbers]
--> here we can say that spaces are reducing by 2 for every 

'''