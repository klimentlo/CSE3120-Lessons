#a_card.py in b_battle (folder)
'''
title: card class
author: mike zhang
date-created: 2023-10-04
'''

class Card:
    '''
    signle playing card
    '''

    SUITS = {
        1: "Diamonds",
        2: "Clubs",
        3: "Hearts",
        4: "Spades"
    }

    FACES = {
        1: "Ace",
        11: "Jack",
        12: "Queen",
        13: "King"
    }

    def __init__(self, SUITE, VALUE):
        '''
        Constructs a card
        '''
        self.__SUIT = SUITE
        self.__VALUE = VALUE

    # --- MODIFIER --- #

    # --- ACCESSOR -- #
    def getCardValue(self):
        return self.__VALUE

    def getCardSuit(self):
        return self.__SUIT

    def __str__(self): # makes it actualyl print the attribute values instead of the object file name (this is magic variable :o)
        if self.__VALUE > 1 and self.__VALUE < 11:
            return f"{self.__VALUE} of {Card.SUITS[self.__SUIT]}"
        else:
            return f"{Card.FACES[self.__VALUE]} of {Card.SUITS[self.__SUIT]}"

    def __repr__(self):
        return f"<--{self.__str__()}--> "

if __name__ == "__main__":
    CARD = Card(1, 12)
    print(CARD)
    print(CARD.getCardValue(), CARD.getCardSuit())

    DECK = []
    for i in range(1,5): # index 1-4 (for all 4 suites)
        for j in range(1,14): # index 1-14 (for all types of cards Ace to King)
            DECK.append(Card(i,j)) # creates the cards and assigns these values into the attributes of Suite and Value, then appends into a list
    print(DECK[0].getCardValue())
    print(DECK)