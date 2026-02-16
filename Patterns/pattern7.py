rows = 5

for i in range(rows):
    # Print spaces
    for j in range(rows - i - 1):   # spaces decrease as i increases
        print(' ', end=' ')
    # Print stars
    for k in range(2 * i + 1):      # stars increase in odd numbers
        print('*', end=' ')
    print()


'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
'''
'''
[space,star,space] ->at row 0 :- [4space,1start,4space]
                        row 1 :- [3space,3star,3space]
                        row 2 :- [2space,5star,2space]
                        row 3 :- [1space,7star,1space]
                        row 4 :- [0space,9star,0space]


'''