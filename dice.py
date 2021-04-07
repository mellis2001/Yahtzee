#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 15:00:18 2020

@author: mellis
"""


import random

class Dice:
    def __init__(self):
        """initializes two lists and rolls"""
        self.current = []
        self.reroll_dice = []
       
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0
        self.score4 = 0
        self.score5 = 0
        self.score6 = 0
        self.three_score = 0
        self.four_score = 0
        self.f_house = 0
        self.sm_straight = 0
        self.l_straight = 0
        self.yahtzee = 0
        self.chance_score = 0
        
    def dice(self):
        """rolls dice"""
        dice = [random.randint(1,6) for i in range(5)]
        self.current = sorted(dice)
        print(self.current)
        return self.current

    
    def reroll(self, reroll_dice):
        """rerolls the dice""" 
        for i in range(len(self.current)):
            if str(i) in reroll_dice: 
                self.current[i] = random.randint(1,6)
        self.current = sorted(self.current)
        return self.current 
    
    
    def keep_dice(self):
        """keeps current dice""" 
        return self.current 
    
    """now for the rolls part for the dice"""
    
    def ones(self):
        """counts 1s"""
        for i in range(len(self.current)):
            if self.current[i] == 1:
                self.score1 += 1
        if self.score1 > 0:
            return True, self.score1
        else:
            return False, 0
    
    def twos(self): 
        """count 2s"""
        for i in range(len(self.current)):
            if self.current[i] == 2:
                self.score2 += 2
        if self.score2 > 0:
            return True, self.score2
        else:
            return False, 0
    
    def threes(self):
        """count 3s"""
        for i in range(len(self.current)):
            if self.current[i] == 3:
                self.score3 += 3
        if self.score3 > 0:
            return True, self.score3
        else:
            return False, 0
    
    def fours(self):
        """count 4s"""
        for i in range(len(self.current)):
            if self.current[i] == 4:
                self.score4 += 4 
        if self.score4 > 0:
            return True, self.score4
        else:
            return False, 0
    
    def fives(self):
        """count 5s"""
        for i in range(len(self.current)):
            if self.current[i] == 5:
                self.score5 += 5
        if self.score5 > 0:
            return True, self.score5
        else:
            return False, 0
    
    def sixes(self):
        """cound 6s"""
        for i in range(len(self.current)):
            if self.current[i] == 6:
                self.score6 += 6
        if self.score6 > 0:
            return True, self.score6
        else:
            return False, 0
    
    def three_kind(self):
        """counts to see if there is 3 of the same number --- needs fixing"""
        if self.current[0] == self.current[2] or self.current[1] == self.current[3] or\
        self.current[2] == self.current[4]: 
            self.three_score += 3 * self.current[2]
            return True, self.three_score
        else:
            return False, 0 
        
    def four_kind(self): 
        """counts to see if 4 of the same number"""
        if self.current[0] == self.current[3] or self.current[1] == self.current[4]:
            self.four_score += 4 * self.current[2]
            return True, self.four_score
        else:
            return False, 0
        
    def full_house(self):
        """ counts to see a full house""" 
        if self.current[0] == self.current[2] and\
        self.current[3] == self.current[4] or\
        self.current[0] == self.current[1] and self.current[2] == self.current[4]:
            self.f_house = 25
            return True, self.f_house
        else:
            return False, 0
    
    def small(self):
        """counts to see small straight"""
        if 1 in self.current and 2 in self.current and 3 in self.current and\
        4 in self.current or 2 in self.current and 3 in self.current and\
        4 in self.current and 5 in self.current or 3 in self.current and\
        4 in self.current and 5 in self.current and 6 in self.current: 
            self.sm_straight = 30
            return True, self.sm_straight 
        else:
            return False, 0

    def large(self):
        """counts to see large straight"""
        if 1 in self.current and 2 in self.current and 3 in self.current and\
        4 in self.current and 5 in self.current or 2 in self.current and\
        3 in self.current and 4 in self.current and 5 in self.current and\
        6 in self.current: 
            self.l_straight = 40
            return True, self.l_straight
        else: 
            return False, 0
        
    def chance(self):
        """counts chance the sum of whole list"""
        self.chance_score = sum(self.current)
        return True, self.chance_score
    
    def yahtzee_roll(self):
        """counts yahtzee (all the same number)"""
        if self.current[0] == self.current[4]:
            self.yahtzee = 50
            return True, self.yahtzee 
        else: 
            return False, 0
        
    def reset_scores(self):
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0
        self.score4 = 0
        self.score5 = 0
        self.score6 = 0
        self.three_score = 0
        self.four_score = 0
        self.f_house = 0
        self.sm_straight = 0
        self.l_straight = 0
        self.yahtzee = 0
        self.chance_score = 0
    
    def check_all(self):
        """prints if valid"""
        print('Can do ones?:' , self.ones())
        print('Can do twos?:', self.twos())
        print('Can do threes?:' , self.threes())
        print('Can do fours?:' , self.fours())
        print('Can do fives?:', self.fives())
        print('Can do sixes?:', self.sixes())
        print('Three of a kind?:', self.three_kind())
        print('Four of a kind?:', self.four_kind())
        print('Full House?:', self.full_house())
        print('Small Straight?:' , self.small())
        print('Large Straight?:' , self.large())
        print('Chance?:', self.chance())
        print('Yahtzee?:' , self.yahtzee_roll())
     
    