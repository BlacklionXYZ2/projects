import pygame, random

pygame.init()

screenWidth, screenHeight = 640, 360        
displaySurface = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

class player:
    x, y = 0, 0
    width, height = 10, 10
    direction = [1, 1]
    speed = 1
    rect = [displaySurface, (255, 0, 0), (x, y, width, height)]
    score = 0

class fruit:
    width, height = 15, 15
    x, y = random.randint(0, screenWidth - width), random.randint(0, screenHeight - height)
    rect = [displaySurface, (255, 255, 255), (x, y, width, height)]

# def checkFruit():
#     playerRange = [(player.x, player.y), (player.x - player.width, player.y), (player.x - player.width, player.y - player.height), (player.x, player.y - player.height)]
#     fruitRange = [[int(fruit.x) - fruit.width, int(fruit.x)], [int(fruit.y) - fruit.height, int(fruit.y)]]
#     for x in playerRange:
#         if x in (range(fruitRange[0][0])):
#             return True
#         else:
#             return False

def score():
    global player, fruit
    player.score += 1
    fruit.x, fruit.y = random.randint(0, screenWidth - fruit.width), random.randint(0, screenHeight - fruit.height)
    # print(player.score, (fruit.x, fruit.y), (player.x, player.y))

def checkFruit():
    playerCoords = {'bottom_right':(player.x, player.y), 
                    'top_right': (player.x, player.y - player.height),
                    'top_left': (player.x - player.width, player.y - player.height),
                    'bottom_left': (player.x - player.width, player.y)}
    fruitRange = { 'x_range': {
                        'left_side': int(fruit.x) - fruit.width,
                        'right_side': int(fruit.x)},
                   'y_range': {
                        'top': int(fruit.y) - fruit.height,
                        'bottom': int(fruit.y)}}
    
    if int(playerCoords['bottom_right'][0]) in list(range(fruitRange['x_range']['left_side'], fruitRange['x_range']['right_side'])):
        if int(playerCoords['bottom_right'][1]) in list(range(fruitRange['y_range']['top'], fruitRange['y_range']['bottom'])):
            print((int(playerCoords['bottom_right'][0]) - int(fruitRange['x_range']['right_side']), int(playerCoords['bottom_right'][1]) - int(fruitRange['y_range']['bottom'])))
            print('bottom right')
            score()
    elif int(playerCoords['top_right'][0]) in list(range(fruitRange['x_range']['left_side'], fruitRange['x_range']['right_side'])):
        if int(playerCoords['top_right'][1]) in list(range(fruitRange['y_range']['top'], fruitRange['y_range']['bottom'])):
            print((int(playerCoords['top_right'][0]) - int(fruitRange['x_range']['right_side']), int(playerCoords['top_right'][1]) - int(fruitRange['y_range']['top'])))
            print('top right')
            score()
    elif int(playerCoords['top_left'][0]) in list(range(fruitRange['x_range']['left_side'], fruitRange['x_range']['right_side'])):
        if int(playerCoords['top_left'][1]) in list(range(fruitRange['y_range']['top'], fruitRange['y_range']['bottom'])):
            print((int(playerCoords['top_left'][0]) - int(fruitRange['x_range']['left_side']), int(playerCoords['top_left'][1]) - int(fruitRange['y_range']['top'])))
            print('top left')
            score()
    elif int(playerCoords['bottom_left'][0]) in list(range(fruitRange['x_range']['left_side'], fruitRange['x_range']['right_side'])):
        if int(playerCoords['bottom_left'][1]) in list(range(fruitRange['y_range']['top'], fruitRange['y_range']['bottom'])):
            print((int(playerCoords['bottom_left'][0]) - int(fruitRange['x_range']['left_side']), int(playerCoords['bottom_left'][1]) - int(fruitRange['x_range']['bottom'])))
            print('bottom left')
            score()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    dt = 5 / clock.tick(120)

    if keys[pygame.K_UP]:
        player.direction = [-1, 1]
    elif keys[pygame.K_RIGHT]:
        player.direction = [1, 0]
    elif keys[pygame.K_DOWN]:
        player.direction = [1, 1]
    elif keys[pygame.K_LEFT]:
        player.direction = [-1, 0]

    if player.direction[1] == 1:
        player.y += player.speed * player.direction[0] * dt
    elif player.direction[1] == 0:
        player.x += player.speed * player.direction[0] * dt
    else:
        print('player.Direction wrong:', player.direction)


    if player.y < 0:
        player.y = 0
    elif player.y > screenHeight - player.height:
        player.y = screenHeight - player.height

    if player.x < 0:
        player.x = 0
    elif player.x > screenWidth - player.width:
        player.x = screenWidth - player.width

    checkFruit()


    player.rect = [displaySurface, (255, 0, 0), (player.x, player.y, player.width, player.height)]
    fruit.rect = [displaySurface, (255, 255, 255), (fruit.x, fruit.y, fruit.width, fruit.height)]
    displaySurface.fill((0, 0, 0))
    pygame.draw.rect(player.rect[0], player.rect[1], player.rect[2])
    pygame.draw.rect(fruit.rect[0], fruit.rect[1], fruit.rect[2])

    pygame.display.flip()

pygame.quit()