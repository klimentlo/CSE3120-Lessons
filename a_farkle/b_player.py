#b_player.py in farkle (folder)

'''
title: player class for farkle
author: kliment lo
date-created: 2023/10/02
'''

from a_dice import Die

class Player:
    '''
    The player for the game Farkle

    :attributes:
    - DICE
    - SCORE

    :behaviors:
    - rollDice()
    - holdDice()
    - addToScore()
    - getScore()
    '''

    def __init__(self):
        '''
        creates a player object
        '''
        self.DICE = [Die(), Die(), Die(), Die(), Die(), Die()]
        self.SCORE = 0

    def rollDice(self):
        '''
        rolls all the die in DICE
        :return: none
        '''
        for die in self.DICE:
            die.rollNum()

    def addScore(self, POINTS_ADDING):
        '''
        adding new points to the player score
        :param POINTS_ADDING: int
        :return: none
        '''
        self.SCORE = self.SCORE + POINTS_ADDING
# --- ACCESSORS --- #
    def displayDice(self):
        '''
        print all dice in self.DICE
        :return: none
        '''
        for die in self.DICE:
            print(die.getNumber())

    def getScore(self):
        '''
        return the score to the rest of the program
        :return: int
        '''
        return self.SCORE
if __name__ == "__main__":
    PLAYER1 = Player()
    PLAYER1.rollDice()
    PLAYER1.displayDice()
    PLAYER1.addScore(500)
    print(PLAYER1.getScore())