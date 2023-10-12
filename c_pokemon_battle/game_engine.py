#game_engine.py in c_pokemon_battle (folder)
'''
title: runs the pokemon battle
author: kliment lo
date-created: 2023-10-12
'''

from pokemon import Pokemon
from technique import moveSet
from my_type import GRASS, WATER
from random import randrange

class Game:

    def __init__(self):
        self.__ATTACKING_PKMN = Pokemon("Quaxly", 150, WATER)
        self.__DEFENDING_PKMN = Pokemon("Sprigatito", 150, GRASS)

    def setup(self):
        self.__ATTACKING_PKMN.addTechnique(moveSet["bubble"])
        self.__ATTACKING_PKMN.addTechnique(moveSet["tackle"])
        self.__DEFENDING_PKMN.addTechnique(moveSet["vine whip"])
        self.__DEFENDING_PKMN.addTechnique(moveSet["tackle"])

    def run(self):
        while not self.__ATTACKING_PKMN.isFainted() and not self.__DEFENDING_PKMN.isFainted():
            ATTACKING_MOVE = self.__ATTACKING_PKMN.chooseTechnique()
            DEFENDING_MOVE = self.__DEFENDING_PKMN.chooseTechnique()
            ATTACKING_DAMAGE = self.__ATTACKING_PKMN.calcDamage(ATTACKING_MOVE, self.__DEFENDING_PKMN.getType())
            DEFENDING_DAMAGE = self.__DEFENDING_PKMN.calcDamage(DEFENDING_MOVE, self.__ATTACKING_PKMN.getType())
            if randrange(2) == 1:
                print(f"{self.__ATTACKING_PKMN} uses {self.__ATTACKING_PKMN.getTechniqueName(ATTACKING_MOVE)}")
                self.__DEFENDING_PKMN.takeDamage(ATTACKING_DAMAGE)
                if not self.__DEFENDING_PKMN.isFainted()
                    print(f"{self.__DEFENDING_PKMN} uses {self.__DEFENDING_PKMN.getTechniqueName(DEFENDING_MOVE)}")
                    self.__ATTACKING_PKMN.takeDamage(DEFENDING_DAMAGE)
                else:
                    print()
            else:
                print(f"{self.__DEFENDING_PKMN} uses {self.__DEFENDING_PKMN.getTechniqueName(DEFENDING_MOVE)}")
                self.__ATTACKING_PKMN.takeDamage(DEFENDING_DAMAGE)
                print(f"{self.__ATTACKING_PKMN} uses {self.__ATTACKING_PKMN.getTechniqueName(ATTACKING_MOVE)}")
                self.__DEFENDING_PKMN.takeDamage(ATTACKING_DAMAGE)
            print(f"{self.__ATTACKING_PKMN} HP remaining: {self.__ATTACKING_PKMN.getHP()}")
            print(f"{self.__DEFENDING_PKMN} HP remaining: {self.__DEFENDING_PKMN.getHP()}")

if __name__ == "__main__":
    GAME = Game()
    GAME.setup()
    GAME.run()