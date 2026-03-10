rows = 5

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end=" ")
        
    alpha = 65 
    midpoint = i  # Middle index of the row; letters increase until here, then decrease
    for k in range(2 * i + 1):
        print(chr(alpha), end=" ")
        if k < midpoint:
            alpha += 1
        else:
            alpha -= 1
    print()

"""
      A 
    A B A 
  A B C B A 
A B C D C B A 

"""
