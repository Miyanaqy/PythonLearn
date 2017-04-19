import pygame, sys
import math
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
poltPoints = []
for x in range(640):
    y = int(math.sin(x/640.0 * 4 * math.pi)*200 + 240)
    poltPoints.append([x,y])
pygame.draw.lines(screen,[0,0,0],False,poltPoints,1)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
