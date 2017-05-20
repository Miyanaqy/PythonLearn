import pygame, sys, math

pygame.init()
screen = pygame.display.set_mode([640,640])
angle =90
print angle
juli = 1

x,y = 0,0
screen.fill([255,255,255])
while True:
    pygame.time.delay(10)
    screen.fill([255,255,255])
    x = juli * math.sin(angle * math.pi / 180) + x
    y = juli * math.cos(angle * math.pi / 180) *10
    print x ,y
    pygame.draw.rect(screen,[0,0,0],[x,y,5,5],0)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()