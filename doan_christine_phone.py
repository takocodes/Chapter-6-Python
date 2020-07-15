# Programmer: Christine Doan
# Prompt: Ask user for number of units used
# Calculate cost for units with 1st plan and 2nd plan
# Output which plan is cheaper

import math

def get_units():
    u = int(input("Enter number of units used: "))
    if u < 0:
        print ("You cannot have negative units.")

def calculation_cost(u):
    bc1 = 9.38
    bc2 = 8.57
    def cost():
        print ("Cost for plan 1: ", bc1)
        print ("Cost for plan 2: ", bc2)
    cost()

get_units()
calculation_cost(get_units)