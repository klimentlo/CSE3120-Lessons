
# d_game_engine.py
"""
title: game engine of battle
author: kliment lo
date-created: 2023-10-02
"""

from b_deck import Deck
from c_player import Player

class Game:
    """
    runs the main program code
    """

    def __init__(self):
        # --- INPUTS
        self.__PLAYER1 = Player(input("Player 1 Name: "))
        self.__PLAYER2 = Player(input("Player 2 Name: "))
        self.__DECK = Deck()
        self.__TABLE = [] # the array that holds the cards that the players play per round
        self.__ROUND = 0
        # --- STATS
        self.__SHOW_TABLE = True #optional to display the table in the results
        self.__SHOW_LONG_BATTLES = True # optional to display battles of 2 or more.

    # --- PROCESSING
    def setup(self):
        self.__DECK.shuffleDeck()
        for i in range(26):
            self.__PLAYER1.takeCard(self.__DECK.drawCard())
            self.__PLAYER2.takeCard(self.__DECK.drawCard())

    def run(self):
        while not (self.__PLAYER1.isHandEmpty() or self.__PLAYER2.isHandEmpty()):
            # Both players reveal a card
            self.__TABLE.append(self.__PLAYER1.giveCard())
            self.__TABLE.append(self.__PLAYER2.giveCard())
            # Test for Battle!
            while self.__TABLE[-2].getCardValue() == self.__TABLE[-1].getCardValue():
                # test if both players have enough cards to battle
                if self.__PLAYER1.getHandSize() > 1 and self.__PLAYER2.getHandSize() > 1:
                    for i in range(2):
                        # both players ante one card and reveal a new card
                        self.__TABLE.append(self.__PLAYER1.giveCard())
                        self.__TABLE.append(self.__PLAYER2.giveCard())
                elif self.__PLAYER1.getHandSize() < 2:
                    # if player 1 does not have enough cards, then player 2 gets all the cards
                    while not self.__PLAYER1.isHandEmpty():
                        # player 1 gives their remaining cards
                        self.__TABLE.append(self.__PLAYER1.giveCard())
                    self.__showStats()
                    for i in range(len(self.__TABLE)):
                        self.__PLAYER2.takeCard(self.__TABLE.pop())
                    break
                else:
                    # if player 2 does not have enough cards, then player 1 gets all the cards
                    while not self.__PLAYER2.isHandEmpty():
                        # player 2 gives their remaining cards
                        self.__TABLE.append(self.__PLAYER2.giveCard())
                    self.__showStats()
                    for i in range(len(self.__TABLE)):
                        self.__PLAYER1.takeCard(self.__TABLE.pop())
                    break
            # Test who wins the round
            if len(self.__TABLE) > 1:
                # the above test is in case one player couldn't battle and the table is already empty.
                self.__showStats()
                if self.__TABLE[-2].getCardValue() > self.__TABLE[-1].getCardValue():
                    for i in range(len(self.__TABLE)):
                        self.__PLAYER1.takeCard(self.__TABLE.pop())
                else:
                    for i in range(len(self.__TABLE)):
                        self.__PLAYER2.takeCard(self.__TABLE.pop())
            self.__ROUND += 1
            if self.__ROUND > 10000:
                break
            # --- OUTPUTS
            print(f"Round {self.__ROUND}: {self.__PLAYER1}: {self.__PLAYER1.getHandSize()}, {self.__PLAYER2}: {self.__PLAYER2.getHandSize()}")
        # displays who wins!
        if self.__PLAYER1.isHandEmpty():
            print(f"{self.__PLAYER2} Wins!")
        elif self.__PLAYER2.isHandEmpty():
            print(f"{self.__PLAYER1} Wins!")
        else:
            print(f"{self.__PLAYER1} and {self.__PLAYER2} are caught in an endless battle that has no winner. ")

    def __showStats(self):
        if self.__SHOW_TABLE:
            print(self.__TABLE)
        elif self.__SHOW_LONG_BATTLES:
            if len(self.__TABLE) > 6:
                print(self.__TABLE)

if __name__ == "__main__":
    GAME = Game()
    GAME.setup()
    GAME.run()