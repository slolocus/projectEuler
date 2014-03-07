#!/usr/bin/python

#k=[2.0,3.0,5.0,7.0,]
actualend=600851475143
lengthofarr=5000
k=range(2,5000)
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
primes=[2,3,5]
isdone=False
while(not isdone):
 for j in k:
  if testprime(j):
   print "PRIME ",j
   primes.append(j)
 #print "JJJJJ ",j
 if j>actualend:
  print"isdone is true ",j
  isdone=True
 increk()
 

for i in primes:
 print "PRIMELIST ",i


if __name__=="__main__":
 print "EXIT "
 exit(0)
