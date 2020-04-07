#!/usr/bin/python

sum = 0
n = int(input("Enter the amount of number :"))
for i in range(0,n,1):
   temp = int(input())
   sum += temp
sum = sum / n
print(sum)
