#!/usr/bin/env python
answer = "?"

cakecount = 3
while (answer != "death"):
    answer = raw_input("cake or death?  ")
    if (answer == "cake"):
        if (cakecount>0):
            print "Very well.  Here is your cake."
            cakecount -= 1
        else:
            print "We're all out cake.  Pick something else."
    else:
        print "That's not one of the provided options, rebel.  Try again."

print "\nDeath it is, then.  Your spine is electrocuted and injected with foul alchemy.  It rises as a homunculus and while still attached to your brain, unhinges itself from your waste, peels like a banana, and gouges your eyes out with the pointed ends.  Next, it slithers into your mouth and all the way through your digestive track, bony protrusions shredding everything it contacts.  Finally they constrict around your throat until your are beheaded. \n\n   Vivid enough?  -David"
        