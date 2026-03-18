def weird_cal(num):
    # Method 1 :- Better Sol,
    # result = [] # because of extra list, we get SC as Same as TC which O(m)
    # while True:
    #     result.append(num)
    #     if num == 1:
    #         break
    #     elif num % 2 == 0:
    #         num = num // 2
    #     else:
    #         num = (num * 3) + 1
            
    # return result
    
    # Method 2:- Optimal SOl, as it takes TC O(m) and Sc O(1)
    while True:
        print(num, end=" ")
        if num == 1:
            break
        elif num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1

num = 3
print(weird_cal(num))