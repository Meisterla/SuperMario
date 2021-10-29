# 入口

import pygame
from source import tools
from source import setup
from source.states import main_menu


def main():
    game = tools.Game()
    state = main_menu.MainMenu()
    game.run(state)


if __name__ == '__main__':
    main()
