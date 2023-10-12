# technique.py in c_pokemon (folder)
'''
title: pokemon battle techniques
author: kliment
date-created: 2023-10-12
'''

class Technique:
    '''
    moves that a pokemon can do in battle
    '''

    def __init__(self, NAME, DAMAGE):
        '''

        :param NAME: str
        :param DAMAGE: int
        '''
        self.__NAME = NAME
        self.__DAMAGE = DAMAGE

    # --- MODIFIER METHODS --- #


    # --- ACCESSOR METHODS --- #
    def __str__(self):
        return self.__NAME

    def getDamage(self):
        return self.__DAMAGE

moveSet = {
    "tackle": Technique("Tackle", 60),
    "vine whip": Technique("Vine Whip", 40),
    "ember": Technique("Ember", 40),
    "bubble": Technique("Bubble", 35),
}

if __name__ == "__main__":
    TACKLE = moveSet["tackle"]

    print(TACKLE, TACKLE.getDamage())