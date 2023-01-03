import pygame
import sys
import time
from pygame.locals import *
from points import rand_points
from distance import distance

pygame.init()

# definindo tamanho da janela da aplicação
GAMEWINDOW = pygame.display.set_mode((1100, 800))

# título da aplicação
pygame.display.set_caption(
    'Par de Pontos mais próximos via Dividir e Conquistar.')

# fonte utilizada na aplicação
obj = pygame.font.Font('freesansbold.ttf', 35)


# descrição RGB das cores utilizadas na aplicação

black = (0, 0, 0)
red = (255, 0, 0)
grey = (169, 169, 169)
orange = (255, 178, 102)
purple = (153, 153, 255)
white = (255, 255, 255)


# inicialização do vetor de pontos utilizados na aplicação
points = []

#
# Caso deseje alterar o número de pontos criados basta aumentar o valor que a função rand_points recebe.

points = rand_points(10)

print("\nVetor de Pontos:", points, "\n")


# Método de criação da malha
def draw_grid(l):
    GAMEWINDOW.fill(orange)
    a = 0
    b = 0
    c = 0
    d = 800
    for i in range(50):
        pygame.draw.line(GAMEWINDOW, black, (a, b), (c, d), 1)
        a += 16
        c += 16

    a = 0
    b = 0
    c = 800
    d = 0
    for i in range(50):
        pygame.draw.line(GAMEWINDOW, black, (a, b), (c, d), 1)
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


# Método para mostrar os pontos (xi, yi) na aplicação

def display_points(l):
    obj = pygame.font.Font('freesansbold.ttf', 20)

    for i in l:
        s = '(' + str(i[0]) + ',' + str(i[1]) + ')'
        surf = obj.render(s, True, black)
        GAMEWINDOW.blit(surf, (i[0]*16 + 16, abs((49 - i[1])*16 + 16)))

# verifica a distância euclidiana entre dois pontos


def points_with_distance(a, b, l1, l2):
    draw_grid(points)
    display_points(points)
    obj1 = pygame.font.Font('freesansbold.ttf', 20)
    s = 'D = ' + str(round(((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5, 2))
    surf = obj1.render(s, True, white)
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


def call_pygame(a, b, l1, l2):
    points_with_distance(a, b, l1, l2)


def terminate():
    pygame.quit()
    sys.exit()


draw_grid(points)
display_points(points)


def call_pygame(a, b, l1, l2):
    points_with_distance(a, b, l1, l2)


def bruteForce(points, n, mid):
    mini = sys.maxsize

    for i in range(n-1):
        for j in range(i+1, n):
            call_pygame(points[i], points[j], mid, -1)

            if (distance(points[i], points[j]) < mini):
                mini = distance(points[i], points[j])
    return mini


def stripClosest(points, n, prevMin, left, right):

    mini = prevMin
    for i in range(n-1):
        for j in range(i+1, n):
            if points[j][1] - points[i][1] > mini:
                break
            call_pygame(points[i], points[j], left, right)

            if (distance(points[i], points[j]) < mini):
                mini = distance(points[i], points[j])
    return mini


def closestPair(x_sorted, y_sorted, n, midpoint):
    if n <= 3:
        return bruteForce(x_sorted, n, midpoint)

    middle = n//2
    midpoint = x_sorted[middle]

    draw_grid(points)
    display_points(points)
    draw_line((midpoint[0], 0), (midpoint[0], 50), purple)
    sleep()

    left_x = x_sorted[: middle]
    right_x = x_sorted[middle:]

    left_y = y_sorted[: middle]
    right_y = y_sorted[middle:]

    dl = closestPair(left_x, left_y, middle, midpoint[0])
    dr = closestPair(right_x, right_y, n-middle, midpoint[0])

    d = min(dl, dr)

    strip = []
    for i in range(n):
        if abs(y_sorted[i][0] - midpoint[0]) < d:
            strip.append(y_sorted[i])

    strip_left = midpoint[0] - d
    strip_right = midpoint[0] + d

    if strip_left < 0:
        strip_left = 0
    if strip_right > 800:
        strip_right = 800

    return stripClosest(strip, len(strip), d, strip_left, strip_right)


if not len(points):
    terminate()


n = len(points)
x_sorted = sorted(points)
y_sorted = sorted(points, key=lambda x: x[1])

minimum = closestPair(x_sorted, y_sorted, n, -1)
print("Menor distância:", minimum)


while 1:
    obj1 = pygame.font.Font('freesansbold.ttf', 20)
    s = 'Menor Distância = ' + str(round(minimum, 2))
    surf = obj1.render(s, True, white)
    GAMEWINDOW.blit(surf, (810, 100))
    sleep()
