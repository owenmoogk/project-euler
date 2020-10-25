finalscounter = 0
biggest = 0
print('calculating')
for n in range(1,1000000):
  checkingn = n
  scounter=0
  while checkingn != 1:
    if checkingn % 2 == 0:
      checkingn = checkingn / 2
      scounter = scounter + 1
    else:
      checkingn = (3*checkingn) + 1
      scounter = scounter + 1
  if scounter > finalscounter:
    finalscounter = scounter
    biggest = n
print(biggest)