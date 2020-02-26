#! /usr/bin/env python3
sticks = 21

print ("There are 21 sticks,you can take 1-4 number of sticks at a time")
print ("Whoever will take the lask stick will loose")

while True:
    print ("Sticks left",sticks)
    if sticks ==1:
        print ("You took the lask stick,you loose")
        break
    sticks_1 = int (input ("Take sticks(1-4)"))
    if sticks_1 >=5 or sticks_1 <=0:
        print("Wrong choice")
        continue
    print ("Computer took:",(5-sticks_1),"\n")
    sticks -=5


