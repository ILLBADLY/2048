from constants import *
from app import App_2048

import pygame
from pygame.locals import *
from random import choice

pygame.init()
pygame.font.init()

if __name__ == '__main__':
    app = App_2048()
    app.main_menu()