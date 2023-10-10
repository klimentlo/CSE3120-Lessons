# c_player.py in b_battle
"""
title: player class
author: kliment lo
date-created: 2023-10-02
"""

class Player:
    """
    Player class for the game Battle
    """

    def __init__(self, NAME):
        self.__NAME = NAME
        self.__HAND = []

    # --- MODIFIER --- #
    def takeCard(self, CARD):
        """
        adds a card to the hand
        :param CARD: object - Card
        """
        self.__HAND.append(CARD)

    def giveCard(self):
        """
        take the top card from the hand
        """
        if len(self.__HAND) > 0:
            return self.__HAND.pop(0)

    # --- ACCESSOR --- #
    def __str__(self):
        return self.__NAME

    def isHandEmpty(self):
        if len(self.__HAND) > 0:
            return False
        else:
            return True

    def getHandSize(self):
        return len(self.__HAND)

if __name__ == "__main__":
    from b_deck import Deck

    DECK = Deck()
    DECK.shuffleDeck()

    PLAYER1 = Player("Mr. Zhang")
    PLAYER2 = Player("Mr. Patterson")

    for i in range(26):
        PLAYER1.takeCard(DECK.drawCard())
        PLAYER2.takeCard(DECK.drawCard())

    print(PLAYER1.isHandEmpty())

    TABLE = []
    TABLE.append(PLAYER1.giveCard())
    TABLE.append(PLAYER2.giveCard())
    print(TABLE)