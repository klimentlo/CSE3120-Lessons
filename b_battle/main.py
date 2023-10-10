# main.py
"""
title: Battle
author: Mike Zhang
date-created: 2023-10-03
"""

class Main:
    from d_game_engine import Game

    def __init__(self):
        self.__GAME = Main.Game()
        self.__GAME.setup()
        self.__GAME.run()

if __name__ == "__main__":
    Main()