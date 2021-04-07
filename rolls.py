#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 23:35:18 2020

@author: mellis
"""

from dice import Dice


class Rolls(Dice):
    def _init_(self,final_roll):
        """initilizes rolls"""
        self.final_roll = self.current
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0
        self.score4 = 0
        self.score5 = 0
        self.score6 = 0
        self.three_score = 0
        self.four_score = 0
        self.f_house = 25
        self.sm_straight = 30
        self.l_straight = 40
        self.yahtzee = 50
        self.chance = 0
        self.score_upper = 0
        self.upper_bonus = 35
        self.final = 0
        self.sorted = final_roll.sort()
        
        super().__init__()
        
    def ones(self,dice):
        """counts 1s"""
        for i in range(len(self.sorted)):
            if self.sorted[i] == 1:
                self.score1 += 1
        self.score_upper += self.score1
        self.final += self.score1
        if self.score1 > 0:
            return True
        else:
            return False
    
    def twos(self,dice): 
        """count 2s"""
        for i in range(len(self.sorted)):
            if self.sorted[i] == 2:
                self.score2 += 2
        self.score_upper += self.score2
        self.final += self.score2
        if self.score2 > 0:
            return True
        else:
            return False
    
    def threes(self,dice):
        """count 3s"""
        for i in range(len(self.sorted)):
            if self.sorted[i] == 3:
                self.score3 += 3
        self.score_upper += self.score3
        self.final += self.score3        
        if self.score3 > 0:
            return True
        else:
            return False
    
    def fours(self,dice):
        """count 4s"""
        for i in range(len(self.sorted)):
            if self.sorted[i] == 4:
                self.score4 += 4 
        self.score_upper += self.score4
        self.final += self.score4        
        if self.score4 > 0:
            return True
        else:
            return False
    
    def fives(self,dice):
        """count 5s"""
        for i in range(len(self.sorted)):
            if self.sorted[i] == 5:
                self.score5 += 5
        self.score_upper += self.score5
        self.final += self.score5
        if self.score5 > 0:
            return True
        else:
            return False
    
    def sixes(self,dice):
        """cound 6s"""
        for i in range(len(self.sorted)):
            if self.sorted[i] == 6:
                self.score6 += 6
        self.score_upper += self.score6
        self.final += self.score6
        if self.score6 > 0:
            return True
        else:
            return False
    
    def upper_bonus(self):
        """adds bonuses"""
        if self.score_upper >= 63:
            self.score_upper += self.upper_bonus
            self.final += self.upper_bonus
        else: 
            self.score_upper += 0
            self.final += 0
            
    def three_kind(self,dice):
        """counts to see if there is 3 of the same number"""
        if self.sorted[0] == self.sorted[2] and self.sorted[1] == self.sorted[3] or\
        self.sorted[2] == self.sorted[4]: 
            self.three_score += 3 * self.sorted[2]
            self.final += self.three_score
            return True 
        else:
            return False 
        
    def four_kind(self,dice): 
        """counts to see if 4 of the same number"""
        if self.sorted[0] == self.sorted[3] or self.sorted[1] == self.sorted[4]:
            self.four_score += 4 * self.sorted[2]
            self.final += self.four_score
            return True 
        else:
            return False
        
    def full_house(self,dice):
        """ counts to see a full house"""
        if self.sorted[0] == self.sorted[2] or self.sorted[0] == self.sorted[1] and\
        self.sorted[2] == self.sorted[4] or self.sorted[3] == self.sorted[4]:
            self.final += self.f_house 
            return True
        else:
            return False
    
    def small(self,dice):
        """counts to see small straight"""
        if self.sorted[0] == 1 or self.sorted[0] == 2 or self.sorted[0] == 3 and\
        self.sorted[4] == 4 or self.sorted[4] == 5 or self.sorted[4] == 6:
            self.final += self.sm_straight
            return True 
        else:
            return False

    def large(self,dice):
        """counts to see large straight"""
        if self.sorted[0] == 1 and self.sorted[1] == 2 and self.sorted[2] == 3 and\
        self.sorted[3] == 4 and self.sorted[4] == 5 or self.sorted[0] == 2 and\
        self.sorted[1] == 3 and self.sorted[2] == 4 and self.sorted[3] == 5 and\
        self.sorted[4] == 6: 
            self.final += self.l_straight
            return True
        else: 
            return False
    
    def yahtzee_roll(self,dice):
        """counts yahtzee (all the same number)"""
        if self.sorted[0] == self.sorted[5]: 
            self.final += self.yahtzee
            return True 
        else: 
            return False
    
    def check_all(self,dice):
        """prints if valid"""
        print('Can do ones?:' , self.ones(dice))
        print('Can do twos?:', self.twos(dice))
        print('Can do threes?:' , self.threes(dice))
        print('Can do fours?:' , self.fours(dice))
        print('Can do fives?:', self.fives(dice))
        print('Can do sixes?:', self.sixes(dice))
        print('Three of a kind?:', self.three_kind(dice))
        print('Four of a kind?:', self.four_kind(dice))
        print('Full House?:', self.full_house(dice))
        print('Small Straight?:' , self.small(dice))
        print('Large Straight?:' , self.large(dice))
        print('Yahtzee?:' , self.yahtzee_roll(dice))
        
            
                
    