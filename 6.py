sumofnumbers=0
totalofsqrednums=0
for n in range (1,101):
  sumofnumbers=sumofnumbers+n
sqrsumofnumbers=sumofnumbers*sumofnumbers
print("The SQRT of the sum of numbers is,",sqrsumofnumbers)

for s in range (1,101):
  totalofsqrednums=totalofsqrednums+(s*s)
print("The total of SQRED NUMS is,",totalofsqrednums)


finalans=sqrsumofnumbers-totalofsqrednums
print(finalans)