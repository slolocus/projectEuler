#!/usr/bin/python
k=0
b=1
a=0
sum=0
prevsum=0
prevk=0
for i in range(40000):
 k=a+b
 a=b
 b=k
 if(k%2==0 and k<4000000):
  prevsum=sum
  prevk=k
  sum=sum+k
  print "sum ",sum," k ",k

print sum
"""
 if(k>4000000):
  print k
  print sum
  print prevk
  print prevsum
  exit(1)
"""
 
