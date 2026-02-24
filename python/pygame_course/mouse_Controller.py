import pygame, math

pygame.init()

screenWidth, screenHeight = 640, 360
displaySurface = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption('test controller')
clock = pygame.time.Clock()

#Rect properties
rectWidth = 50
rectHeight = 50
rect_x, rect_y = 0, 0
rectSpeed = 5
diagMult = 0.625

#loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # if event.type == pygame.MOUSEMOTION:
        #     rect_x = (list(event.pos))[0] - (rectWidth // 2)
        #     rect_y = (list(event.pos))[1] - (rectHeight // 2)

    rect_x, rect_y = pygame.mouse.get_pos()[0] - rectWidth // 2, pygame.mouse.get_pos()[1] - rectHeight // 2

    #draw rectangle
    # clock.tick(120)
    displaySurface.fill((0, 0, 0))
    pygame.draw.rect(displaySurface, (255, 255, 255), (rect_x, rect_y, rectWidth, rectHeight))

    #update screen
    pygame.display.flip()

pygame.quit()