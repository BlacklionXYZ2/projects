import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1920,1080
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption('Meteor shooter')
clock = pygame.time.Clock()

testSurface = pygame.Surface((400, 100))
testFill = pygame.Surface((0, 0))

xPos = 800
yPos = 500

while True:

	# 1. input -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	clock.tick(60)

	# 2. updates 
	testFill.fill((0, 0, 0))
	display_surface.blit(testFill, (0, 0))
	yPos -= 1
	testSurface.fill((255, 0, 0))
	display_surface.blit(testSurface, (xPos, yPos))

	# 3. show the frame to the player / update the display surface
	pygame.display.update()