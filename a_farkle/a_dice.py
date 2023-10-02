#a_dice.py in a_farkle (folder)

'''
title: dice class
author: kliment lo
date-created: 2023/10/02
'''

class Die:
    '''
    Create a die to roll for random numbers

    :attributes:
    - DIE_MAX_NUMBER
    - DIE_NUMBER

    :methods:
    - rollNum()
    - getNum()
    '''

    from random import randint

    def __init__(self):
        '''
        constructs the die object
        '''
        self.DIE_MAX_NUMBER = 6
        self.DIE_NUMBER = None

    def rollNum(self):
        '''
        updates DIE_NUMBER with a new number
        :return: None
        '''
        self.DIE_NUMBER = Die.randint(1, self.DIE_MAX_NUMBER)

    def getNumber(self):
        '''
        returns the number the dice rolled
        :return: (int)
        '''
        return self.DIE_NUMBER

if __name__ == "__main__":
    DIE_1 = Die()
    DIE_2 = Die()
    DIE_1.rollNum()
    DIE_2.rollNum()
    print(DIE_1.getNumber(), DIE_2.getNumber())

    DICE = []
    for i in range(6):
        DICE.append(Die())
    print(DICE)
    for i in range(len(DICE)):
        DICE[i].rollNum()
    for die in DICE:
        print(die.getNumber())
    for i in range(len(DICE)):
        print(f"Die {i + 1}. {DICE[i].getNumber()}")