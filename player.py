#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:47:45 2020

@author: mellis
"""

from dice import Dice

class Player(Dice):
    
    def __init__(self):
        """initializes player"""
        self.name = ''
        self.marker = '--'
        self.upper_score = 0
        self.upper_bonus = 0
        self.final_score = 0
        self.labels = [
                'ONES','TWOS','THREES','FOURS','FIVES','SIXES',
                '3 OF A KIND', '4 OF A KIND', 
                'FULL HOUSE','SMALL STRAIGHT', 'LARGE STRAIGHT', 'CHANCE',
                'YAHTZEE',
                ]
        self.answer = ''
        self.rolls = []
        
        super().__init__()
        
    def __repr__(self):
        """returns input of player name"""
        s = ''
        self.name = str(input('What is your name?:'))
        s += self.name
        return s
        
    def working_list(self):
        self.rolls.append(self.answer) 
        return self.rolls
    
    def is_open(self, index):
        i = int(index)
        char = self.labels[i]
        occur = sum(char in s for s in self.rolls) 
        if occur == 1: 
            return False
        else:
            return True
          
    def is_upper_bonus(self):
        if self.upper_score >= 63: 
            self.final_score += 35
            print('Upper bonus acheived! +35')
        else: 
            self.final_score += 0
            
    def place_mark(self):
        place = input('Where do you want this? (Write number from list)')
        if place == '0' and self.is_open(place) == True:
            if self.score1 > 0: 
                self.upper_score += self.score1
                self.final_score += self.score1
                self.answer = place + ') ' + self.labels[0] + self.marker + str(self.score1) 
            else: 
                self.answer = place + ') ' + self.labels[0] + self.marker + '0' 
        elif place == '1' and self.is_open(place) == True:
            if self.score2 > 0: 
                self.upper_score += self.score2
                self.final_score += self.score2
                self.answer = place + ') ' + self.labels[1] + self.marker + str(self.score2)
            else: 
                self.answer = place + ') ' + self.labels[1] + self.marker + '0' 
        elif place == '2' and self.is_open(place) == True: 
            if self.score3 > 0: 
                self.upper_score += self.score3
                self.final_score += self.score3
                self.answer = place + ') ' + self.labels[2] + self.marker + str(self.score3)
            else: 
                self.answer = place + ') ' + self.labels[2] + self.marker + '0'
        elif place == '3' and self.is_open(place) == True: 
            if self.score4 > 0: 
                self.upper_score += self.score4
                self.final_score += self.score4
                self.answer = place  + ') ' + self.labels[3] + self.marker + str(self.score4)
            else: 
                self.answer = place + ') ' + str(self.labels[3]) + self.marker + '0' 
        elif place == '4' and self.is_open(place) == True: 
            if self.score5 > 0: 
                self.upper_score += self.score5
                self.final_score += self.score5
                self.answer = place + ') ' + self.labels[4] + self.marker + str(self.score5)
            else: 
                self.answer = place + ') ' + self.labels[4] + self.marker + '0'
        elif place == '5' and self.is_open(place) == True: 
            if self.score6 > 0: 
                self.upper_score += self.score6
                self.final_score += self.score6
                self.answer = place + ') ' + self.labels[5] + self.marker + str(self.score6) 
            else: 
                self.answer = place + ') ' + self.labels[5] + self.marker + '0'
        elif place == '6' and self.is_open(place) == True: 
            if self.three_score > 0: 
                self.final_score += self.three_score
                self.answer = place + ') ' + self.labels[6] + self.marker + str(self.three_score)
            else: 
                self.answer = place + ') ' + self.labels[6] + self.marker + '0' 
        elif place == '7' and self.is_open(place) == True: 
            if self.four_score > 0: 
                self.final_score += self.four_score
                self.answer = place + ') ' + self.labels[7] + self.marker + str(self.four_score)
            else: 
                self.answer = place + ') ' + self.labels[7] + self.marker + '0'
        elif place == '8' and self.is_open(place) == True: 
            if self.f_house == 25: 
                self.final_score += self.f_house
                self.answer = place + ') ' + self.labels[8] + self.marker + str(self.f_house) 
            else: 
                self.answer = place + ') ' + self.labels[8] + self.marker + '0'
        elif place == '9' and self.is_open(place) == True: 
            if self.sm_straight == 30: 
                self.final_score += self.sm_straight
                self.answer = place + ') ' + self.labels[9] + self.marker + str(self.sm_straight) 
            else: 
                self.answer = place + ') ' + self.labels[9] + self.marker + '0' 
        elif place == '10' and self.is_open(place) == True: 
            if self.l_straight == 40: 
                self.final_score += self.l_straight
                self.answer = place + ') ' + self.labels[10] + self.marker + str(self.l_straight) 
            else: 
                self.answer = place + ') ' + self.labels[10] + self.marker + '0' 
        elif place == '11' and self.is_open(place) == True: 
            if self.chance_score > 0: 
                self.final_score += self.chance_score
                self.answer = place + ') ' + self.labels[11] + self.marker + str(self.chance_score) 
            else: 
                self.answer = place + ') ' + str(self.labels[11]) + self.marker + '0' 
        elif place == '12' and self.is_open(place) == True: 
            if self.yahtzee == 50: 
                self.final_score += self.yahtzee
                self.answer = place + ') ' + str(self.labels[12]) + self.marker + str(self.yahtzee)
            else: 
                self.answer = place + ') ' + self.labels[12] + self.marker + '0' 
        else: 
            print('Invalid Index') 
            self.place_mark()
      

    