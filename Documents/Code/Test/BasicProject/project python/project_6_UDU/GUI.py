import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('QLSV')
running = True
GREEN = (0, 200, 0)
clock = pygame.time.Clock()
RED = (255, 0, 0)

rect_x = 100

while running:		
	clock.tick(60)
	screen.fill(GREEN)

	rect_x += 1
	pygame.draw.rect(screen, RED, (rect_x,150,50,50))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()