# Programmer: Christine Doan
# Assignment 4, Functions

# Part 1: Statistical Functions
# Write four functions for means

# import
import math

# variables

a = float(input("Insert the first number: "))
b = float(input("Insert the second number: "))
c = float(input("Insert the third number: "))

# functions

def mean (x, y, z):
    result = (x + y + z) / 3
    return result

def geometric_mean(x, y, z):
    gresult = ((a * b * c) **(1/3))
    return gresult

def harmonic_mean(x, y, z):
    hresult = (3 / ((1/x) + (1/y) + (1/z)))
    return hresult

def reciprocal (r):
    return 1.0 / r

# calculations
armean = mean(a, b, c)
gmean = geometric_mean(a, b, c)
hmean = harmonic_mean (a, b, c)

# outputs
print("Arithmetic mean is", (format(armean, '.2f')))
print("Geometric mean is", (format(gmean, '.2f')))
print("Harmonic mean is", (format(hmean, '.2f')))

print("Reciprocal for first number is", (reciprocal(a)))
print("Reciprocal for second number is", (reciprocal(b)))
print("Reciprocal for third number is", (reciprocal(c)))



