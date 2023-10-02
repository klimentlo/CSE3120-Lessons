#c_game_engine.py in a_farkle (folder)

'''
title: game engine class for farkle
author: kliment lo
date-created: 2023/10/02
'''

from b_player import Player

class Game:
    '''
    structures the turns for the game and identifies the win conditions
    '''

    def __init__(self):
        self.PLAYER1 = Player()
        self.PLAYER2 = Player()

    def setup(self):
        '''
        where data needs to be modified before the start of the game loop
        :return: none
        '''

    def run(self):
        '''
        the main program loop
        :return:
        '''
        while self.PLAYER1.getScore() < 10000 and self.PLAYER1.getScore() < 10000:
            # --- PLAYER 1 --- #
            print("Player 1's Turn")
            TURN = 0
            while TURN < 3:
                self.PLAYER1.rollDice()
                self.PLAYER1.holdDice()
                TURN += 1

            # --- PLAYER 2 --- #