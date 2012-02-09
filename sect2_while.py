#!/usr/bin/env python
from hwtools import *

print "Section 2:  Loops"
print "-----------------------------"

# 1. Keep getting a number from the input (num) until it is a multiple of 3.
num = raw_input("Please enter a number divisble by 3: ")
num = int(num)
while (num % 3)!=0 or num<=0:
    num = raw_input ("Try again.  Enter a number divisible by 3, you rebel: ")
    num = int(num)



print "1.", num

# 2. Countdown from the given number to 0 by threes. 
#    Example:
#      12...
#      9...
#      6...
#      3...
#      0

print "2. Countdown from", num
print num
while (num > 0):
    num -= 3
    print num
print "Blastoff"

    
#CODE GOES HERE


# 3. [ADVANCED] Get another num.  If num is a multiple of 3, countdown 
#    by threes.  If it is not a multiple of 3 but is even, countdown by 
#    twos.  Otherwise, just countdown by ones.
num = raw_input("Please enter a positive number. ")
num = int(num)
while num<=0:
    num = raw_input ("Try again.  Enter a number divisible by 3, you rebel: ")
    num = int(num)
print num
if (num % 3) == 0:
    countdown = 3
elif (num % 2) == 0:
    countdown = 2
else:
    countdown = 1
    
while (num > 0):
    num -= countdown
    print num
print "Failure to launch.  Billions of tax dollars are burned up, along with the astronauts."


# num = int(raw_input("3. Countdown from: "))

