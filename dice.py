#!/usr/bin/env python3

# 2022-04-01 simple dice roll

import random

def dice():
    side = random.randint(1, 6)
    if side == 1:
        print("⚀")
    if side == 2:
        print("⚁")
    if side == 3:
        print("⚂")
    if side == 4:
        print("⚃")
    if side == 5:
        print("⚄")
    if side == 6:
        print("⚅")
    exit
      
  
   
dice()


