finaln=0
for n in range (1,100000):
  for i in range (1,n):
    finaln=finaln+i
    if i==n-1:

      x=finaln
      y=(x**.5)
      factorcounter=0

      for i in range (1,y+1):
        if x%i==0:
          if i==x/i:
            factorcounter=factorcounter+1
          else:
            factorcounter=factorcounter+2
      if factorcounter>500:
        print (factorcounter)
        print (finaln)