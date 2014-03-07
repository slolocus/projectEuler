#!/usr/bin/python

def checkpal(no):
 print"checking ",no
 lengthofno=len(no)
 areyoueven=False
 if(lengthofno%2==0):
  areyoueven=True
 rmid=lmid=0
 if(areyoueven):
  rmid=len(no)/2
  lmid=rmid
 else:
  rmid=len(no)/2+1 
  lmid=len(no)/2
 
 atest=no[0:lmid]
 t=''
 for i in range(lengthofno-1,rmid-1,-1):
  print " >>>> ",no[i]
  t=t+no[i]
 if atest == t:
  return True
 return False

def dumpvars():
 global a,b,tno
 print "A ",a," b ",b," number ",tno

def execbeh():
 global state,a,b
 if state==0:    # we only care about decrementing a by one
  a=a-1
  if(a<100):
   state=1
   a=999
 elif (state==1): # we only care about decrementing b by one
  b=b-1
  if(b<100):
   done=True
  state=0
 
a=999
b=999
done=False
tno=0
tnos=''
state=0
results=[]
while(not done):
 tno=a*b
 tnos=str(tno)
 print "checking a ",a," b ",b," ",tno
 if checkpal(tnos):
  results.append(tnos)
  print "A ",a," B ",b," number ",tno
 if(a<100 or b<100):
  done=True
  print"lower limits reached"
  dumpvars()
 execbeh()
print "results ",results
intresults=[]
for i in results:
 k=int(i)
 intresults.append(k)

intresults.sort()

print ">>>>>>>>> "
print intresults



