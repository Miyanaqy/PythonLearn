import pygame, sys , random
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,image_file,location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

pygame.init()
size = width, height = (640, 480)
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
pygame.display.flip()
img_file = 'beach_ball.png'
balls = []
for row in range(3):
    for column in range(3):
        speed = [random.choice([-2,2]), random.choice([-2,2])]
        location = [column * 180 + 10 , row * 180 + 10]
        ball = MyBallClass(img_file, location, speed)
        balls.append(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.time.delay(20)
    screen.fill([255,255,255])
    for ball in balls:
        ball.move()
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    
