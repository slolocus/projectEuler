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
 print "endk ",endk
 k=range(endk,endk+lengthofarr)


# 600851475143
primes=[2,3,5,7]
isdone=False

def incrementprime():
 increk()
 for j in k:
  if testprime(j):
   print "PRIME ",j
   primes.append(j)

def print10001prime():
 print"the 10001st prime" 
 print "length currently ",len(primes)
 print primes[10000]

def remainderof(trem,prime):
 """ going deep """
 global i,primes,done
 print "checking trem ",trem," prime ",prime
 if trem==1:
  done=True 
  return 0
 if trem%prime ==0:
  rem=trem/prime
  factors.append(prime)
  print "this is a factor ",prime
  return rem
 else:
  if i+1 >= len(primes):
   incrementprime()
  i=i+1
  return remainderof(trem,primes[i])

""" prime factors for """
actualend=6008514751430
#actualend=1900
done=False
remainder=0
factors=[]
trem=actualend
i=0
while(not done):
 trem=remainderof(trem,primes[i])
 # only this section is for the 10001st prime question
 if(len(primes)==10001):
  print primes[10000]
  exit(0)
k=0
for i in factors:
 print "factors ",i
 print "multiplication ",i*k
 if i*k !=0:
  k=i*k 
 else:
  k=i
print10001prime()

