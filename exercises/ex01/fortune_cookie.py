"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730313954"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says... ")

a: int = randint(1, 50)
if a < 25:
    if a < 13:
        print("You were born to stand out.")
    else:
        print("Kindness is the sunshine in which virtue grows.")   
else:
    if a < 37:
        print("A smile is your personal welcome mat.")     
    else:
        print("Adventure can be real happiness.")
         

print("Now, go spread positive vibes!")
