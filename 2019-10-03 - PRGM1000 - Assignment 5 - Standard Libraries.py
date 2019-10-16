# -*- coding: utf-8 -*-
#Donald Szeto
#PRGM1000 - Scripting Fundamentals
#Assignment 5 - Standard Libraries
#2019-10-03
#Version 1


"""
Created on Thu Oct  3 14:38:18 2019

@author: net1121
"""

#Import random module
import random

#Create variables and assign result of random number generator.
Dice1 = random.randrange(0, 7, 1)
Dice2 = random.randrange(0, 7, 1)
RollTotal = Dice1 + Dice2

#Print die results and total.
print("You rolled a %d and %d, totalling %d." % (Dice1, Dice2, RollTotal))