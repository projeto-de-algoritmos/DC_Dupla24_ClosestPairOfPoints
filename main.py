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


def display_points(l):
    obj = pygame.font.Font('freesansbold.ttf', 20)

    for i in l:
        s = '(' + str(i[0]) + ',' + str(i[1]) + ')'
        surf = obj.render(s, True, black)
        GAMEWINDOW.blit(surf, (i[0]*16 + 16, abs((49 - i[1])*16 + 16)))

def points_with_distance(a, b, l1, l2, l3):
    draw_grid(points)
    display_points(points)
    obj1 = pygame.font.Font('freesansbold.ttf', 20)
    s = 'D = ' + str(round(((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5, 2))
    surf = obj1.render(s, True, red)
    dist_x_coor = (a[0]*16 + b[0]*16)//2
    dist_y_coor = (800 - a[1]*16 + 800 - b[1]*16)//2
    GAMEWINDOW.blit(surf, (dist_x_coor, dist_y_coor))

    draw_line(a, b, (0, 255, 0))
    draw_line((l1, 0), (l1, 50), purple)
    draw_line([l2, 0], [l2, 50], purple)

    sleep()

def sleep():
    t_end = time.time() + 2
    while time.time() < t_end:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

        pygame.display.update()

def call_pygame(a, b, l1, l2, l3):
    points_with_distance(a, b, l1, l2, l3)

def terminate():
    pygame.quit()
    sys.exit()

draw_grid(points)
display_points(points)


############################################################################################################


def call_pygame(a, b, l1, l2, l3):
    points_with_distance(a, b, l1, l2, l3)


def bruteForce(points, n, mid):
    mini = sys.maxsize

    for i in range(n-1):
        for j in range(i+1, n):
            call_pygame(points[i], points[j], mid, -1, -1)

            if (distance(points[i], points[j]) < mini):
                mini = distance(points[i], points[j])
    return mini


