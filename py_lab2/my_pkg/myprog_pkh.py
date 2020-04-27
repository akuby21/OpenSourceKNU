#!/usr/bin/python
import my_pkg.binaryToOther as bin
import my_pkg.unionInteger as union
while True:
   sel = int(input("Select menu: 1) conversion 2) union/intersection 3) exit ? "))
   
   if sel == 1:
      num = input("input binary number :")
      print("=> OCT> " + bin.binToOct(num))
      print("=> DEC> " + bin.binToDec(num))
      print("=> HEX> " + bin.binToHex(num))
   elif sel == 2:
      union.func()
   elif sel == 3:
      print("exit the program...")
      break



