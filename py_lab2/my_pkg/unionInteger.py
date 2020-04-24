#!/usr/bin/python
import re

def func():
   lst = input("1st list: ")
   lst1 = set(re.findall("\d+", lst))
   lst = input("2nd list: ")
   lst2 = set(re.findall("\d+", lst))

   print("=> union")
   print(sorted(list(map(int,list(lst1 | lst2)))))
   
   print("=> intersection")
   print(sorted(list(map(int,list(lst1 & lst2)))))
  
