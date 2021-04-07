#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:21:02 2020

@author: mellis
"""

from dice import Dice
from player import Player
import random


def yahtzee(p1):
    """runs game"""
    name = p1.__repr__()
    turns = 13
    
    print('Welcome to Yahtzee', name + '!')
    print()
    print('\u0333'.join('OPTIONS '))
    print()
    
    for i in range(13):
            print(str(i) + ') ' + str(p1.labels[i]))
            
    print()
    
            
    while turns != 0: 
        d = p1.dice()   
        d = process_reroll(p1, d)
        """pdb.set_trace()"""
        p1.check_all()
        p1.place_mark()
        print('\u0333'.join('PROGRESS '))
        print()
        print(p1.working_list())
        p1.reset_scores()
        leave = input('Would you like to quit, ' + name + '?')
        if leave == 'yes' or leave == 'y' or leave == 'YES' or leave == 'Y' or leave == 'Yes':
            break
        turns -= 1
        
        print()
        print('Turns remaining:', turns)    
    print('Game Complete!')
    p1.is_upper_bonus()
    print('Final Score', p1.final_score)
    
    
    
def process_reroll(p, r):
    """processes the rerolls"""
    num_rerolls = 2
    while(num_rerolls > 0):
        answer = input('Would you like to reroll?')
        if answer == 'yes' or answer == 'y' or answer == 'Yes' or answer == 'YES' or answer == 'Y':
            reroll_dice = input('Dice to reroll (by index number): ')
            r = p.reroll(reroll_dice)
            print(r)
            num_rerolls -= 1
        elif answer == 'no' or answer == 'n' or answer == 'No' or answer == 'NO' or answer == 'N':
            print(p.keep_dice())
            break
        else:
            print('Try again')
    return r 


