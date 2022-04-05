#!/usr/bin/env python3

import random

def rockpaper():
    rps = ['R', 'S', 'P']
    hand = random.choices(rps)
    cp = str(hand).replace('[', '').replace(']' ,'')
    cp = "".join(hand)
    #print(cp)
    player_hand = input('(R)ock, (P)aper, (S)cissor ')
    if player_hand not in rps:
        exit

    if player_hand == cp:
        print('Draw')
    else:
        if player_hand == 'R' and cp == 'S':
            print('You win! 🪨 beats Scissor')
        if player_hand == 'R' and cp != 'S':
            print('You lose! 🗊  Beats Rock')

        if player_hand == 'S' and cp == 'P':
            print('You win! ✀  beats Paper')
        if player_hand == 'S' and cp != 'P':
            print('You lose! 🪨 Beats Scissor')

        if player_hand == 'P' and cp == 'R':
            print('You win! 🗊  beats Rock')
        if player_hand == 'P' and cp != 'R':
            print('You lose! ✀  Beats Paper')
           


rockpaper()    

