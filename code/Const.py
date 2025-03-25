# C
import pygame.constants

COLOR_PINK = (75, 42, 45)
COLOR_WHITE = (255, 255, 255)
COLOR_ORANGE = (255, 128, 0)
COLOR_GREEN = (0, 150, 0)
COLOR_ROSA = (230, 0, 160)

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
    'Player' : 3,
    'Enemy1' : 1,
    'Enemy2' : 1,
    'Enemy3' : 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 0,
    'Level1Bg2' : 0,
    'Level1Bg3' : 0,
    'Player' : 1,
    'Enemy1' : 1,
    'Enemy2' : 1,
    'Enemy3' : 1,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Player' : 0,
    'Enemy1' : 1,
    'Enemy2' : 1,
    'Enemy3' : 1,
}

# W
WIN_WIDTH = 600
WIN_HEIGHT = 338