#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?
sum = 0
for x in nums:
    sum += x
print "1.", sum


# 2. Print every even number in nums
print "2. even numbers"
for x in nums:
    if x % 2 == 0:
        print x


#CODE GOES HERE


# 3. Does nums only contain even numbers? 
only_even = True

for x in nums:
    if x % 2 == 0:
        pass
    else:
        only_even = False

#CODE GOES HERE

print "3.",
if only_even:
    print "only even"
else:
    print "some odd"


# 4. Generate a list every odd number less than 100. Hint: use range()
def oddness(x): return x*2 - 1

oddity = map (oddness, range(1,51))
# DEN: yes, I looked up my own functions, because brain does not function.
print "4.", oddity

# 5. [ADVANCED]  Multiply each element in nums by its index
for x in nums:
    nums[nums.index(x)] = x*nums.index(x)
    # DEN: crude solution.  need better
    

print "5.", nums
