# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 08:02:06 2019

@author: net1121
"""

#Donald Szeto
#PRGM1000 - Scripting Fundamentals
#Assignment 9 - Iterations
#2019-10-15
#Version 1

#Import random module
import random

#Create variables and assign result of random number generator.
Dice1 = random.randrange(0, 7, 1)
Dice2 = random.randrange(0, 7, 1)

#Calculate roll total
RollTotal = Dice1 + Dice2
Game = True
AttemptsLeft = 3
CorrectGuess = False

#Loop guessing game
while Game and AttemptsLeft >= 1:
    print("You have %d attempts left." % (AttemptsLeft))
    #Get an input from the user with error/exception handling.
    try:
        UserGuess = int(input("Guess a number from 1 to 12: "))
        AttemptsLeft -= 1
        #Out of range scenario
        if UserGuess not in range(0, 13):
            print("Hey, I said a number from 1 to 12!")
            break
            
        #Outcome scenarios.
        elif RollTotal == UserGuess:
            print("Yes, %d! You got it!" % (RollTotal))
            CorrectGuess = True
            Game = False
        elif RollTotal > UserGuess:
            print("You guessed %d. Too low!" % (UserGuess))
        elif RollTotal < UserGuess:
            print("You guessed %d. Too high!" % (UserGuess))
    
    #Invalid integer entered.
    except:
        print("Sorry, it doesn't look like you entered a valid number. \
Please try again.")

if AttemptsLeft == 0 and CorrectGuess == False:
    print("Sorry, it looks like you ran out of attempts. \
The answer was %d." % (RollTotal))