import math

primesummation=0

for num in range (1,2000000,2): 
    for i in range(2,num,2):
        if num % i == 0:
            break
        else:
          if i+1==num:
            primesummation=primesummation+num
            print(num)
            print (primesummation)