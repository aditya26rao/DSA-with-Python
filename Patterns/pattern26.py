num = 4
rows = 2 * num - 1

for i in range(rows):
    for j in range(rows):
        top = i
        left = j
        right = rows - j - 1
        bottom = rows - i - 1
        value = num - min(top, left, right, bottom)
        print(value, end=" ")
    print()

"""
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
"""
