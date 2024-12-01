def total(number):
    sum1 = 0
    tich = 1
    no_zero = False
    
    for i in range(len(number)):
        if i % 2 == 0:
            sum1 += int(number[i])
        else:
            if int(number[i]) != 0 :
                tich *= int(number[i])
                no_zero = True
                
    if not no_zero:
        tich = 0
        
    sum_tich = str(sum1) + " " + str(tich)                
    return sum_tich    

for t in range(int(input())):
    number = input()
    
    print(total(number))    


