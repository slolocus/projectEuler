#!/usr/bin/python

done=False
k=1
candi=1
while ( not done):
 good=True
 #print "testing ",candi
 for i in range(1,21):
  if(candi%i==0):
   good&=True
   #print "\t>> divisible by ",i
  else:
   good&=False
   break
 
 if(good):
  print candi
  done=True
 else:
  candi=candi+1
   
