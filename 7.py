stop = 0
primeCounter = 0
number = 1
print('running')

def isPrime(num):
  y = 'prime'
  for i in range(2,num):
    if (num % i) == 0:
      y = 'not prime'
      break
  return (y)

while stop == 0:
  number += 1
  x = isPrime(number)
  if x == "prime":
    primeCounter += 1
  if primeCounter >= 10001:
    stop = 1
    print (primeCounter, number)