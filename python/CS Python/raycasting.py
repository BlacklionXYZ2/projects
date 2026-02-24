import pygame
from math import sqrt, sin, cos, tan, atan, pi

pygame.init()
clock = pygame.time.Clock()

screenWidth, screenHeight = 640, 360        
screen = pygame.display.set_mode((screenWidth, screenHeight))

tile_size = 50
map = [[1, 1, 1, 1, 1, 1, 1], 
       [1, 0, 0, 0, 1, 0, 1], 
       [1, 0, 0, 1, 1, 0, 1], 
       [1, 0, 0, 0, 0, 0, 1], 
       [1, 1, 1, 1, 1, 1, 1]]
wall_colour = (0, 0, 255)
floor_colour = (255, 255, 255)

class player:
    def __init__(self, size, speed, x = 50, y = 50, colour = (255, 0, 0)):
        self.width, self.height = size[0], size[1]
        self.speed = speed
        self.x, self.y = x, y
        self.colour = colour
        self.diag_speed_scalar = self.speed / sqrt((self.speed ** 2) * 2)
        self.angle = pi / 2
        self.centre = (self.x + (self.width / 2), self.y - (self.height / 2))

player1 = player((25, 25), 3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(floor_colour)

    dt = player1.speed / clock.tick(120)
    keys = pygame.key.get_pressed()
    rotate_speed = 180 * (pi / 180)

    #diagonal
    if (keys[pygame.K_w] and keys[pygame.K_d]):
        player1.y -= player1.speed * player1.diag_speed_scalar * dt
        player1.x += player1.speed * player1.diag_speed_scalar * dt
    elif (keys[pygame.K_s] and keys[pygame.K_d]):
        player1.y += player1.speed * player1.diag_speed_scalar * dt
        player1.x += player1.speed * player1.diag_speed_scalar * dt
    elif (keys[pygame.K_w] and keys[pygame.K_a]):
        player1.y -= player1.speed * player1.diag_speed_scalar * dt
        player1.x -= player1.speed * player1.diag_speed_scalar * dt
    elif (keys[pygame.K_s] and keys[pygame.K_a]):
        player1.y += player1.speed * player1.diag_speed_scalar * dt
        player1.x -= player1.speed * player1.diag_speed_scalar * dt
    #linear
    elif keys[pygame.K_w]:
        player1.y -= player1.speed * dt
    elif keys[pygame.K_s]:
        player1.y += player1.speed * dt
    elif keys[pygame.K_a]:
        player1.x -= player1.speed * dt
    elif keys[pygame.K_d]:
        player1.x += player1.speed * dt

    #rotation
    if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
        player1.angle += 0
    elif keys[pygame.K_RIGHT]:
        player1.angle += rotate_speed * dt
    elif keys[pygame.K_LEFT]:
        player1.angle -= rotate_speed * dt

    rotated_surf = pygame.transform.rotate(screen, player1.angle)
    rotated_rect = rotated_surf.get_rect(center = player1.centre)
    print(rotated_rect)

   # player1.angle = atan(()) # fix angle between mouse and player

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, player1.colour, rotated_rect)#(player1.x, player1.y, player1.width, player1.height)

    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            if tile == 1:
                rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                pygame.draw.rect(screen, wall_colour, rect)

    pygame.display.flip()

pygame.quit()