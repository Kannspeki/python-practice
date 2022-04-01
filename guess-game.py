#!/usr/bin/env python3

# A simple guess game

import random


def guessgame(gs, nm):
    wrong = 0
    while gs != nm or wrong > 3 or guess != 'q':
        guess = input('Guess a number: (press q to quit) ')
        if guess == 'q':
            print('The number was ', nm)
            return 0
        if nm == gs:
            print('You won!', nm, 'Is the correct number\n')
        if nm != gs: 
            print('Incorrect')
            wrong += 1 
            hint(wrong, nm)


def hint(w,n):
    if w > 3:
        ask = input('Would you like a hint? y/n ')
        if ask == 'y' or ask == 'Y':
            if n % 2 == 0:
                print('try an even number')
            else:
                print('try an odd number')
        exit        



guess = 0
num = random.randint(0, 100)
guessgame(guess, num) 
