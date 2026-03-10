rows = 5

spaces = 0
for i in range(rows):
    for j in range(rows - i):
        print("*", end=" ")
    for k in range(spaces):
        print(" ", end=" ")
    for j in range(rows - i):
        print("*", end=" ")
    spaces += 2
    print()

spaces = 2 * rows - 2
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    for k in range(spaces):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    spaces -= 2
    print()


'''

* * * * * * * * * * 
* * * *     * * * * 
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *

'''