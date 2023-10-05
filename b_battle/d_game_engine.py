#d_game_engine.py
'''
title: game engine of battle
author: kliment lo
date-created: 2023/10/05
'''

from b_deck import Deck
from c_player import Player

class Game:
    '''
    runs the main program code
    '''
    def __init__(self):
        self.__PLAYER1 = Player(input("Player 1 Name: ")) # Player creates name attribute and Hand attribute (__NAME and __HAND([]))
        self.__PLAYER2 = Player(input("Player 2 Name: "))
        self.__DECK = Deck()

    def setup(self):
        self.__DECK.shuffleDeck()
        for i in range(26):
            self.__PLAYER1.takeCard(self.__DECK.drawCard())
            self.__PLAYER2.takeCard(self.__DECK.drawCard())

    def run(self):
        ROUNDS = 0
        while len(self.PLAYER__HAND.checkWin()) < 56 and len(self.__PLAYER2) < 56: #when a player do
            ROUNDS += 1
            pass

    def checkWin(self):
        if self.

if __name__ == "__main__":
    GAME = Game() # Current Attributes of GAME: (__PLAYER1(__NAME,__HAND) ) (__PLAYER2(__NAME,__HAND)) (__DECK(52 long array))
    GAME.setup()
    GAME.run()



