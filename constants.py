import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1000, 650
CAPTION = '2048'

TOP, LEFT = 125, 160
BLOCK_WIDTH, BLOCK_HEIGHT = 100, 100
GAP = 9

MAIN_MENU_FONT = pygame.font.SysFont('Tahoma', 45)
TITLE_FONT = pygame.font.SysFont('Tahoma', 75)
BLOCK_FONT = pygame.font.SysFont('Tahoma', 25)
STATS_FONT = pygame.font.SysFont('Tahoma', 40)
GAME_OVER_FONT = pygame.font.SysFont('Tahoma', 45)

BLACK = '#000000'
WHITE = '#ffffff'
BLUE =  '#0000ff'
RED =   '#ff0000'

BG_COLOR = '#bbada0'

COLOR_MAP = {
    0:     ('#CCC0B4', None),
    2:     ('#eee4da', '#776e65'),
    4:     ('#ede0c8', '#776e65'),
    8:     ('#f2b179', '#f9f6f2'),
    16:    ('#f59563', '#f9f6f2'),
    32:    ('#f67c5f', '#f9f6f2'),
    64:    ('#f65e3b', '#f9f6f2'),
    128:   ('#edcf72', '#f9f6f2'),
    256:   ('#edcc61', '#f9f6f2'),
    512:   ('#edc850', '#f9f6f2'),
    1024:  ('#edc53f', '#f9f6f2'),
    2048:  ('#edc22e', '#f9f6f2'),
    4096:  ('#eee4da', '#776e65'),
    8192:  ('#edc22e', '#f9f6f2'),
    16384: ('#f2b179', '#776e65'),
    32768: ('#f59563', '#776e65'),
    65536: ('#f67c5f', '#f9f6f2')
}