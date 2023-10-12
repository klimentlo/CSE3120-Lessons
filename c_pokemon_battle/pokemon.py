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
        self.__HP -= DAMAGE
        if self.__HP < 0:
            HP = 0


    # ACCESSOR METHODS (Getter Methods)
    def __str__(self):
        return self.__NAME

    def chooseTechnique(self):
        '''
        provide a menu for the trainer to select a move
        :return:
        '''
        print(f"Select a move for {self.__NAME}")
        for i in range(len(self.__TECHNIQUES)):
            print(f"{i + 1}. {self.__TECHNIQUES[i]}")
        CHOICE = int(input("> "))
        CHOICE -= 1
        return CHOICE

    def calcDamage(self, MOVE_SELECTED,ENEMY_POKEMON_TYPE):
        '''
        calculate the damage of the pokemon's move
        :param MOVE_SELECTED: int - > index for the selected move
        :param ENEMY_POKEMON_TYPE:  str
        :return:
        '''
        MOVE_DAMAGE = self.__TECHNIQUES[MOVE_SELECTED].getDamage()
        if ENEMY_POKEMON_TYPE == self.__TYPE.getResistance():
            MOVE_DAMAGE = MOVE_DAMAGE // 2
        elif ENEMY_POKEMON_TYPE == self.__TYPE.getWeakness():
            MOVE_DAMAGE = MOVE_DAMAGE * 2
        return MOVE_DAMAGE

    def getType(self):
        return str(self.__TYPE)

    def getTechniqueName(self, INDEX):
        '''
        returns the name of the technique at index INDEX
        :param INDEX: int
        :return: str
        '''
        return str(self.__TECHNIQUES[INDEX])

    def getHP(self):
        return self.__HP

    def isFainted(self):
        if self.__HP == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    from my_type import GRASS, FIRE, WATER
    from technique import moveSet
    SPRIG = Pokemon("Sprigatito", 25, GRASS)
    SPRIG.addTechnique(moveSet["vine whip"])
    SPRIG.addTechnique(moveSet["tackle"])
    MOVE = SPRIG.chooseTechnique()
    DAMAGE = SPRIG.calcDamage(MOVE, str(FIRE))
    print(MOVE, DAMAGE)