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
    - holdDie()
    - addToScore()
    - getScore()
    '''

    def __init__(self):
        '''
        creates a player object
        '''
        self.DICE = [Die(), Die(), Die(), Die(), Die(), Die()]
        self.HELD_DICE = []
        self.SCORE = 0

    def rollDice(self):
        '''
        rolls all the die in DICE
        :return: none
        '''
        for die in self.DICE:
            die.rollNum()

    def holdDie(self):
        '''
        user selects die to save
        :return: none
        '''
        print("Select a die to hold ")
        for i in range(len(self.DICE)):
            print(f"{i+1}. {self.DICE[i].getNumber()}")
        DIE = int(input("> ")) - 1
        self.HELD_DICE.append(self.DICE.pop(DIE))

        print("Dice Remaining")
        for die in self.DICE:
            print(die.getNumber())

        print("Held Dice: ")
        for die in self.HELD_DICE:
            print(die.getNumber())

        #ask to gold more dice
        AGAIN = input("Hold More? (y/N)")
        if AGAIN.upper() == "Y":
            return self.holdDie()


    def addScore(self, POINTS_ADDING):
        '''
        adding new points to the player score
        :param POINTS_ADDING: int
        :return: none
        '''
        self.SCORE = self.SCORE + POINTS_ADDING

    def resetDice(self):
        """
        put all dice back in self.DICE
        :return:
        """
        self.DICE = [Die(), Die(), Die(), Die(), Die(), Die()]
        self.HELD_DICE = []
# --- ACCESSORS --- #
    def displayDice(self):
        '''
        print all dice in self.DICE
        :return: none
        '''
        for die in self.DICE:
            print(die.getNumber())

    def displayAllDice(self):
        '''
        print all dice in self.DICE and self.HELD_DICE
        :return:
        '''

        for die in self.DICE:
            print(die.getNumber())

        for die in self.HELD_DICE:
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
    PLAYER1.holdDie()
    PLAYER1.displayDice()
    PLAYER1.addScore(500)
    print(PLAYER1.getScore())