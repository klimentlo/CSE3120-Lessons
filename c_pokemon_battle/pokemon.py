#pokemon.py in c_pokemon_battle (folder)
'''
title: pokemon class
author: kliment lo
date-created: 2023/10/11
'''

class Pokemon:
    def __init__(self, NAME, HP, TYPE, LEVEL=5):
        '''
        Pokemon
        :param NAME: str
        :param HP: int
        :param TYPE: obj
        :param LEVEL: int
        '''
        self.__NAME = NAME
        self.__HP = HP
        self.__TYPE = TYPE
        self.__LEVEL = LEVEL
        self.__TECHNIQUES = []

    # MODIFIER METHODS (Setter Methods)
    def addTechnique(self, TECNIQUE):
        if len(self.__TECHNIQUES) < 4:
            self.__TECHNIQUES.append(TECNIQUE)

    def takeDamage(self, DAMAGE):
        self.__HP -=
    # ACCESSOR METHODS (Getter Methods)
    def __str__(self):
        return self.__NAME

if __name__ == "__main__":
    from my_type import GRASS
    SPRIG = Pokemon("Sprigatito", 25, GRASS)
    print(SPRIG)