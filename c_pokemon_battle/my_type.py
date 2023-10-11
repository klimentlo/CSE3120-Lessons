#my_type.py in c_pokemon_battle
'''
title: pokemon type class
author: kliment lo
date-created: 2023/10/11
'''

class Type:

    def __init__(self, NAME, RESIST=None, WEAK=None):
        '''
        Type object ot determine strengths and weakness
        :param NAME: str
        :param RESIST: str
        :param WEAK: str
        '''
        self.__NAME = NAME
        self.__RESIST = RESIST
        self.__WEAK = WEAK

    # MODIFIER METHODS

    # ACCESSOR METHODS
    def __str__(self):
        return self.__NAME

    def getResistance(self):
        return self.__RESIST

    def getWeakness(self):
        return self.__WEAK

GRASS = Type("Grass", "Water", "Fire")
WATER = Type("Water", "Fire", "Grass")
FIRE = Type("Fire", "Grass", "Water")

if __name__ == "__main__":
    NORMAL = Type("Normal")
    print(NORMAL.getWeakness())