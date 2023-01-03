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

def draw_grid(l):
    GAMEWINDOW.fill(orange)
    a = 0
    b = 0
    c = 0
    d = 800
    for i in range(50):
        pygame.draw.line(GAMEWINDOW, grey, (a, b), (c, d), 1)
        a += 16
        c += 16

    a = 0
    b = 0
    c = 800
    d = 0
    for i in range(50):
        pygame.draw.line(GAMEWINDOW, grey, (a, b), (c, d), 1)
        b += 16
        d += 16

    for i in l:
        pygame.draw.rect(
            GAMEWINDOW, red, (i[0]*16, abs((49 - i[1])*16), 16, 16))

def draw_line(a, b, color):

    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    y1 = abs(50 - y1)
    y2 = abs(50 - y2)
    pygame.draw.line(GAMEWINDOW, color, (x1*16, y1*16), (x2*16, y2*16), 5)