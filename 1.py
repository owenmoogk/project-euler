#Setting Var. to 0
finaln=0

#checking if # is divisible by 5 or 3
for checkingn in range (1,1000):
    if checkingn%3==0 or checkingn%5==0:
        finaln=finaln+checkingn

#printing final number
print(finaln)