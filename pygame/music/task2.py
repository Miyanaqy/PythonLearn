import pygame

pygame.init()
pygame.mixer.init()

pygame.display.set_mode([640,480])
pygame.time.delay(1000)

pygame.mixer.music.load('bg_music.mp3')
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play()

splay = pygame.mixer.Sound('splay.wav')
splay.set_volume(0.50)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	if not pygame.mixer.music.get_busy():
		splay.play()
		pygame.time.delay(1000)
		running = False
pygame.quit()