rows = 5

for i in range(rows):
    alpha = 64 + rows - i
    for j in range(i + 1):
        print(chr(alpha), end=" ")
        alpha += 1
    print()

"""
E
D E
C D E
B C D E
A B C D E
"""