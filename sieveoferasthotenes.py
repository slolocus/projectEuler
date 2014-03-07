#!/usr/bin/python
"""
a=[]
remme=[]
results=[]
for i in xrange(1,1001):
 a.append(i)

for i in range(2,1000,2):
 #print">>>> ",i 
 remme.append(i)

for i in range(3,1000,3):
 remme.append(i)

for i in range(5,1000,5):
 remme.append(i)

for i in remme:
 print i
 if i>=1000:
  break
 i=i-1
 a[i]=0

for i in a:
 if i>0:
  print i
  #results.append(i)

"""


""" All this applicable to a range length  """

int initptr=0
int startno=2
boolean done=False
a=[] # this is the working variable
results=[]
remme=[]

def populateList(startno,length):
 for i in range(startno,length):
  a.append(i)

def getLength(no,endno):
 return endno-no+1

def removeArray(pri,rlength):
 """ here we strike off the number from the array to retrieve the result """
 for i in range(pri,rlength,pri):
  remme.append(i)
  
def getUpperLimit(no):
 return no**2


a=[2]
primes=[]
upperLimit=getUpperLimit(a[0])
lenghtofcheck=getLength(a[0],upperLimit)
populateList(a[0],lengthofcheck)
print a

#while(not done):
 

 
