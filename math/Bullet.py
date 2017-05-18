class BulletClass(pygame.sprite.Sprite):
    def __init__(self,image_file,pos,epos, speed = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        '''x = random.randint(-4,4)
        y = random.randint(-4,4)
        self.speed = [x, y]'''
        s = math.sqrt(mox(abs(epos[0]-pos[0])) + mox(abs(epos[1]-pos[1])))/8
        self.speed = speed
        self.speed = [(epos[0]-pos[0]) / s, (epos[1]-pos[1]) / s]
    def move(self):
        self.rect = self.rect.move(self.speed)


def mox(x):
    return x * x