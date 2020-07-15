# Programmer: Christine Doan
# Assignment 4, Functions

# Part 2: Write distances in two dimensions.
# Ask user for coordinates of two points
# Calculate Pyth and city block before outputting

# imports
from math import sqrt

# x1, y1 inputs
a = int(input ("Enter first X: "))
b = int(input ("Enter first Y: "))

# x2, y2 inputs
c = int(input ("Enter second X: "))
d = int (input ("Enter second Y: "))

# functions
def distance (x1, y1, x2, y2):
    d = sqrt (((x1 - x2)**2) + ((y1 - y2)**2))
    return d

def block_distance (x1, y1, x2, y2):
    b = (abs(x1 - x2) + (y1 - y2))
    return b

# calculations
disresult = distance(a, b, c, d)
bloresult = block_distance(a, b, c, d)

# outputs
print("The Pythagorean distance is ", (format(disresult, '.2f')))
print("The city block distance is ", (format(bloresult, '.2f')))



