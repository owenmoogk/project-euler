for c in range (0,1000):
  for b in range (0,c):
    for a in range (0,b):
      if a+b+c==1000:
        if a*a+b*b==c*c:
          print (a,b,c)
          print(a*b*c)