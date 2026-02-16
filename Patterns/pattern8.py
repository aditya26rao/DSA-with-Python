rows = 5

for i in range(rows, 0, -1):   # Loop from 5 down to 1
    # Print spaces
    for j in range(rows - i):
        print(' ', end='')
    # Print stars
    for k in range(2 * i - 1):
        print('*', end='')
    print()

'''
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
'''