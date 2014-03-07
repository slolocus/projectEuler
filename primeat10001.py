#!/usr/bin/python
lengthofarr=5000
k=range(2,9)

def testprime(no):
 b=True
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

# 600851475143
primes=[2,3,5,7]
isdone=False

while (not isdone):
 incrementprime() 
 print "number of primes:",len(primes)
 if(len(primes)>10000):
  isdone=True

print primes[10000]

