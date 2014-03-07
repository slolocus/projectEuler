#!/usr/bin/python 
import math

def evaleqn(a,b):
 return math.sqrt(a**2+b**2)

def amidone(a,b,c):
 if(a+b+c==1000):
  return True
 return False
 
for a in xrange(1,10000):
 for b in xrange(a,10000):
  c=evaleqn(a,b)
  print "a ",a," b ",b," c ",c
  if(amidone(a,b,c)):
   print "Done ",a," b ",b," c ",c
   print a*b*c
   exit(0)
