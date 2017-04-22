import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load('beach_ball.png')
x = 50
y = 50
inx = 10
iny = 10
while True:
    pygame.time.delay(20)
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
    x += inx
    if x > screen.get_width() - 90 or x<0:
        inx = -inx
        x += inx
    y += iny
    if y > screen.get_height() - 90 or y <0:
        iny = -iny
        y += iny
    screen.blit(my_ball,[x,y])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
