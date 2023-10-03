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
        while self.PLAYER1.getScore() < 10000 and self.PLAYER2.getScore() < 10000:
            # --- PLAYER 1 --- #
            print("Player 1's Turn")
            TURN = 0
            while TURN < 3:
                self.PLAYER1.rollDice()
                self.PLAYER1.holdDie()
                TURN += 1
            self.PLAYER1.displayAllDice()
            TEMP_POINTS = int(input("Player 1 Points: "))
            self.PLAYER1.addScore(TEMP_POINTS)
            self.PLAYER1.resetDice()
            # --- PLAYER 2 --- #
            print("Player 2's Turn")
            TURN = 0
            while TURN < 3:
                self.PLAYER2.rollDice()
                self.PLAYER2.holdDie()
                TURN += 1
            self.PLAYER2.displayAllDice()
            TEMP_POINTS = int(input("Player 2 Points: "))
            self.PLAYER2.addScore(TEMP_POINTS)
            self.PLAYER2.resetDice()
        if self.PLAYER1.getScore() >= 10000:
            print("Player 1 Wins!")
            print(f"""
Final scores:
Player 1: {self.PLAYER1.getScore()}
Player 2: {self.PLAYER2.getScore()}""")
        else:
            print("Player 2 Wins!!!")
            print(f"""Final scores:
Player 1: {self.PLAYER1.getScore()}
Player 2: {self.PLAYER2.getScore()}""")

if __name__ == "__main__":
    game = Game()
    game.run()
