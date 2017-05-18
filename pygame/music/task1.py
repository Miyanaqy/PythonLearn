import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000)
pygame.mixer.music.load('bg_music.mp3')
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play()

splat = pygame.mixer.Siund('splat.wav')
splat.set_volume(0.50)
splat.play()

run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
pygame.quit()