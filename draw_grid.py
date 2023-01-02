import pygame
from pygame.locals import*

pygame.init()

GAMEWINDOW=pygame.display.set_mode((1300, 800))
pygame.display.set_caption('Par de Pontos mais próximos via Dividir e Conquistar.')
obj=pygame.font.Font('freesansbold.ttf',35)

black=( 0, 255, 0)
red=(255, 0, 0)
grey=(169,169,169)
white = (0, 0, 0)
blue = (0, 0 , 255)


points = []

def draw_grid(l):
    GAMEWINDOW.fill(white)    
    a = 0
    b = 0
    c = 0
    d = 800
    for i in range(50):
        pygame.draw.line(GAMEWINDOW, grey, (a,b), (c,d), 1)
        a+=16
        c+=16
        
    a = 0
    b = 0
    c = 800
    d = 0
    for i in range(50):
        pygame.draw.line(GAMEWINDOW, grey, (a,b), (c,d), 1)
        b+=16
        d+=16
        
    for i in l:    
        pygame.draw.rect(GAMEWINDOW,red,(i[0]*16, abs((49 - i[1])*16), 16, 16))

