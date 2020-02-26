#! /usr/bin/env python3
row = int (input ("Enter the number of rows:"))
n = row
while n >=0:
    x = "*"*n
    y = " "*(row - n)
    z = " "*10
    print (y+x+x)
    n -=1
