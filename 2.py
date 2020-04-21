prevnum=1
currnum=1
checkingn=0
trn=0
while checkingn<4000000:
  prevnum=currnum
  currnum=checkingn
  if checkingn%2==0:
    trn=trn+checkingn
    print (trn)
  checkingn=prevnum+currnum