rows = 5

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
    

spaces = 2
for i in range(rows - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    for k in range(spaces):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    spaces += 2
    print()

    """
    
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
    """