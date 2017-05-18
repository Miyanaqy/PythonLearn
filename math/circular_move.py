import pygame, sys, math

pygame.init()
screen = pygame.display.set_mode([640,640])
angle = 0
screen.fill([255,255,255])
while True:
    pygame.time.delay(10)
    angle += 1
    x = 200 * math.sin(angle * math.pi / 180) + 320
    y = 200 * math.cos(angle * math.pi / 180) + 320
    pygame.draw.rect(screen,[0,0,0],[x,y,5,5],0)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()