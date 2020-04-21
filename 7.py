primenumc=1

for num in range (0,10000000000): 
  for i in range(2,num):  
    if num % i == 0:
      break
    else:
      if i+1==num:
        primenumc=primenumc+1
        print(primenumc)
        print(num)