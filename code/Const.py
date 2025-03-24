# C
import pygame.constants

COLOR_PINK = (75, 42, 45)
COLOR_WHITE = (255, 255, 255)

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

#E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Player' : 3,
    'Enemy1' : 1,
    'Enemy2' : 2,
    'Enemy3' : 3,
}

ENTITY_HEALTH = {
    'Level1Bg0' : 999,
    'Level1Bg1' : 999,
    'Level1Bg2' : 999,
    'Level1Bg3' : 999,
    'Player' : 300,
    'Enemy1' : 50,
    'Enemy2' : 30,
    'Enemy3' : 20,
}

# W
WIN_WIDTH = 600
WIN_HEIGHT = 338