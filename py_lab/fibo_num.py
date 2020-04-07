#!/usr/bin/python
import sys

n = int(input("fibonacci number:"))
temp1 = temp2 = 1
for i in range(0,n,1):
   if(i<2):
      print(1,end=',')
   else:
      print(temp1+temp2,end=',')
      t=temp2
      temp2 = temp1+temp2
      temp1 = t
print("\nF"+str(i+1)+' = '+str(temp2))
