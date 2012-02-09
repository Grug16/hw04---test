#!/usr/bin/env python
b = "O"
a = "+"
width = int(raw_input("Enter Width: "))
height = int(raw_input("Enter Height: "))
line=""
character = ""
for y in range (1,height+1):
    for x in range (1, width+1):
        if(character==a):
            line +=a
            character = b
        else:
            line +=b
            character = a
    print line
    if(character==a):
        character = b
    else:
        character = a
    line=""
        
