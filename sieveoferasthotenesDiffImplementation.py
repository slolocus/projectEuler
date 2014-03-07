#!/usr/bin/python

def populateList(startno,length):
 for i in range(startno,length):
  print "i ",i
  a.append(i)

def getLength(no,endno):
 return endno-no+1

def removeArray(startno,endlimit,division):
 """ here we strike off the number from the array to retrieve the result """
 for i in range(startno,endlimit,division):
  i=i-startno
  remme.append(i)
  
def getUpperLimit(no):
 return (no**2)+1

def shiftPrimes(var,rmov):
 for i in rmov:
  var[i]=0

startno=2
initptr=0
done=False
a=[] # this is the working variable
results=[]
remme=[]
primes=[2]
upperLimit=getUpperLimit(startno)
lengthofcheck=getLength(startno,upperLimit)
print lengthofcheck
populateList(startno,upperLimit)


print a

while(not done):
 for div in primes:
  removeArray(startno,upperLimit,div)
 shiftPrimes(a,remme)
 
 done=True 
print "working var a ",a
print "remme ",remme
