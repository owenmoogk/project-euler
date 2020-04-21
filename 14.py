scounter=0
finalscounter=0
scounter = 0
finalscounter = 0

for n in range(2, 1000000):
    #n stores og num
    checkingn = n
    #checkingn is the number being manipulated
    while checkingn != 1:
        if checkingn % 2 == 0:
            checkingn = checkingn / 2
            scounter = scounter + 1
        if checkingn % 2 != 0:
            checkingn = 3 * checkingn + 1
            scounter = scounter + 1
    if scounter > finalscounter:
        finalscounter = scounter
        print(n)
