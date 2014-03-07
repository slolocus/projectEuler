#!/usr/bin/python
lengthofarr=5000
k=range(2,9)
sumofprimes=0

def testprime(no):
 b=True
 if(no%2==0):
  return False
 if(no%3==9):
  return False
 if(no%5==0):
  return False
 if(no%7==0):
  return False
 for i in primes:
  res=no%i
  if(res==0):
   #print ">>>",no," prime ",i
   b&=False
  else:
   b&=True
   #print ">>>Possible ",no," prime ",i
 return b

def increk():
 global k
 endk=k[len(k)-1]
 #print "endk ",endk
 k=range(endk,endk+lengthofarr)

def incrementprime():
 for j in k:
  if testprime(j):
   #print "PRIME ",j
   primes.append(j)
 increk()

def sumThePrimes():
 """ ok this is inefficient !!! """
 global sumofprimes
 for i in primes:
  sumofprimes=sumofprimes+i

# 600851475143
primes=[2,3,5,7]
isdone=False

while (not isdone):
 incrementprime() 
 print "number of primes:",len(primes)
 if(primes[len(primes)-1]>1000000):
  isdone=True
  sumThePrimes()
 print "sumfoPrimes ",sumofprimes," at prime ",primes[len(primes)-1]

print "sumfoPrimes ",sumofprimes 

F=open("savedprimes","w")
for i in primes:
 oline=str(i)+"\n"
 F.write(oline)

