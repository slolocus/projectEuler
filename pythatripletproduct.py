#!/usr/bin/python
import math

def evalfunc(a,b): 
 """ returns the C part of the equation """
 c=a**2+b**2
 return math.sqrt(c)

def areyoudone(a,b,c):
 if(a+b+c==1000):
  return True
 return False

done=False
k=a=b=c=0
while(not done):
 b=a+1
 c=b+1
 while(b<c):
  c=evalfunc(a,b)
  print "evaluating a ",a," b ",b," c ",c
  done=areyoudone(a,b,c)
  b=b+1
print "a ",a," b ",b," c ",c


def checkwithinrange(a,b,c):
 """a<b<c ... use the upper and lower as a clamp on b. Then raise a+1, then lower c-1"""
 for i in range(a,c):
  c=
  

