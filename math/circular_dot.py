import pygame, sys
import math


pygame.init()
screen = pygame.display.set_mode([640,640])
screen.fill([255,255,255])
pygame.time.delay(50)
screen.fill([255,255,255])
pygame.draw.circle(screen,[255,0,0],[320,320],200,1)
angle = 180
x = 200 * math.sin(angle*math.pi/180)+320
y = 200 * math.cos(angle*math.pi/180)+320
print x, y
pygame.draw.rect(screen,[0,0,0],[x-2,y-2,5,5],0)
pygame.display.flip()
while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
