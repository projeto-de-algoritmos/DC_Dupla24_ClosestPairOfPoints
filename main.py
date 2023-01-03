import pygame
import sys
import random
import time
import os
from pygame.locals import *
from points import rand_points
from distance import distance

pygame.init()

GAMEWINDOW = pygame.display.set_mode((1100, 800))
pygame.display.set_caption(
    'Par de Pontos mais próximos via Dividir e Conquistar.')
obj = pygame.font.Font('freesansbold.ttf', 35)

black = (0, 0, 0)
red = (255, 0, 0)
grey = (169, 169, 169)
orange = (255, 178, 102)
purple = (153, 153, 255)


points = []

points = rand_points(10)


