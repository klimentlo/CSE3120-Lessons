# main.py

'''
title: basic farkle game
author: kliment lo
date-created: 2021/10/03
'''

class Main:
    from c_game_engine import Game

    def __init__(self):
        self.MAIN = Main.Game()

    def run(self):
        self.MAIN.run()

if __name__ == "__main__":
    MAIN = Main()
    MAIN.run()