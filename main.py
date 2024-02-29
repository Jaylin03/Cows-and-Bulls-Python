'''
Goal: Create a program that will play the “cows and bulls” game with the user.
The game works like this:
  - Randomly generate a 4-digit number.
  - Ask the user to guess a 4-digit number.
    - For every digit that the user guessed correctly in the correct place, they have a “cow”.
    - For every digit the user guessed correctly in the wrong place is a “bull.”
  - Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
  - Once the user guesses the correct number, the game is over.
  - Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
'''

import random

def newNubmer():
  comp_num = random.randint (1000 , 10000)
  comp_num = str(comp_num)
  return comp_num

def bullCount(bull):
  bull = bull + 1
  return bull

def cowCount(cow):
  cow = cow + 1
  return cow

def guessCount(guess):
  guess = guess + 1
  return guess

def bullSearch(comp_num , user_num , bull):
  for x in range (len(user_num)):
    for z in range (len(comp_num)):
      if (user_num[x] == comp_num[z]):
        bullCount(bull)

def cowSearch(comp_num , user_num):
  cow = False
  for x in range (len(user_num)):
    if (user_num[x] == comp_num[x]):
      cowCount(cow)

################################################################
cow = 0
bull = 0
guess = 0

comp_num = newNubmer()
user_num = input("Enter a number: ")
  
while (comp_num != user_num):
  cow = cowSearch(comp_num , user_num)
  bull = bullSearch(comp_num , user_num , bull)
  guess = guessCount(guess)
  print (str(cow) + " cows, " + str(bull) + " bulls")
  
if (comp_num == user_num):
  print ("Correct!")