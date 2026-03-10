rows = 5
alpha = 65
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ",end=' ')
    for k in range(2 * i + 1):
        print(chr(alpha),end=' ')
        alpha += 1

    print()


"""
        A
      B C D
    E F G H I
  J K L M N O P
Q R S T U V W X Y    
"""