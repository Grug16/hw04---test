#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)
if (n % 2)==0:
    type = "n is Even"
else:
    type = "n is Odd"
    

print "1.", type


# 2. If n is odd, double it
if (n % 2)==0:
    twicen = n * 2
print "2.", twicen


# 3. If n is evenly divisible by 3, add four
if (n % 3)==0:
    n = n + 4
print "3.", n


# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)
if grade >=90:
    letter = "A"
elif grade >=80:
    letter = "B"
elif grade >=70:
    letter = "C"
elif grade >=60:
    letter = "D"
else:
    letter = "F"
print "4.", letter

