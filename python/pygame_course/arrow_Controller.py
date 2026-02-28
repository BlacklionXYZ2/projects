import pygame, math

pygame.init()

screenWidth, screenHeight = 2 * 640, 2 * 360        
displaySurface = pygame.display.set_mode((screenWidth, screenHeight))
laserList = []

pygame.display.set_caption('test controller')
clock = pygame.time.Clock()
f = False
fire = False

#Rect properties
rectWidth = 50
rectHeight = 50
rect_x, rect_y = 0, 0
rectSpeed = 5
diagMult = rectSpeed / math.sqrt((rectSpeed ** 2) * 2)

#laser 
laserWidth = 10
laserHeight = 25

#loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #movement
    keys = pygame.key.get_pressed()
    if f == True:
        dt = 5 / clock.tick(120)
    f = True
    
    #diagonal
    if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        rect_y -= rectSpeed * diagMult * dt
        rect_x += rectSpeed * diagMult * dt
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        rect_y += rectSpeed * diagMult * dt
        rect_x += rectSpeed * diagMult * dt
    elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        rect_y -= rectSpeed * diagMult * dt
        rect_x -= rectSpeed * diagMult * dt
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        rect_y += rectSpeed * diagMult * dt
        rect_x -= rectSpeed * diagMult * dt
    #linear
    elif keys[pygame.K_UP]:
        rect_y -= rectSpeed * dt
    elif keys[pygame.K_DOWN]:
        rect_y += rectSpeed * dt
    elif keys[pygame.K_LEFT]:
        rect_x -= rectSpeed * dt
    elif keys[pygame.K_RIGHT]:
        rect_x += rectSpeed * dt

    if keys[pygame.K_RSHIFT ]:
        rectSpeed += 0.1 * dt
    
    if keys[pygame.K_RCTRL]:
        rectSpeed -= 0.1 * dt

    #keep rectangle on screen
    if rect_y < 0:
        rect_y += rectSpeed
    elif rect_y > screenHeight - rectHeight:
        rect_y -= rectSpeed

    if rect_x < 0:
        rect_x += rectSpeed
    elif rect_x > screenWidth - rectWidth:
        rect_x -= rectSpeed

    ship = [displaySurface, (255, 255, 255), (round(rect_x), round(rect_y), rectWidth, rectHeight)]

    #fire laser
    if keys[pygame.K_SPACE] and fire == False:
       fire = True
       laserRect = [round(rect_x + (rectWidth / 2) - (laserWidth / 2)), round(rect_y - (rectHeight / 2))]
       laserList.append(laserRect)
    elif keys[pygame.K_SPACE] and fire == True:
        pass
    else:
        fire = False

    #draw rectangle
    displaySurface.fill((0, 0, 0))
    pygame.draw.rect(ship[0], ship[1], ship[2])

    #draw laser
    for x in laserList:
        pygame.draw.rect(displaySurface, (255, 255, 255), (x[0], x[1], laserWidth, laserHeight))
        x[1] -= 1
        if x[1] > screenHeight:
            laserList.remove(x)

    #update screen
    pygame.display.flip()

pygame.quit()