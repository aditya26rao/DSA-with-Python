rows = 5

for i in range(rows):
    alpha = 64 + rows - i
    for j in range(i + 1):
        print(chr(alpha), end=" ")
    print()

"""
E
D D
C C C
B B B B
A A A A A
"""
