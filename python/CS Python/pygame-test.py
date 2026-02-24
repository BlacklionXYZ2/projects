import pygame
from pygame import Vector2 as vec2, Vector3 as vec3

pygame.init()

screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))

class player:
    def __init__(self, size: tuple, colour: vec3, pos: vec2, surface):
        self.size = size
        self.colour = colour
        self.x = pos[0]
        self.y = pos[1]
        self.surface = surface

player1 = player((25, 25), vec3(255, 0, 0), vec2(300, 300), screen)

start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

    player1.x, player1.y = pygame.mouse.get_pos()[0] - player1.size[0] // 2, pygame.mouse.get_pos()[1] - player1.size[0] // 2

    screen.fill((0, 0, 0))
    print(player1.x, player1.y)
    if player1.x > (screen_width - player1.size[0] / 2) - 1 or player1.x < (-player1.size[0] / 2) + 1:
        pass
    elif player1.y > (screen_height - player1.size[1] / 2) - 1 or player1.y < (-player1.size[1] / 2) + 1:
        pass
    else:
        pygame.draw.rect(player1.surface, player1.colour, (player1.x, player1.y, player1.size[0], player1.size[1]))

    pygame.display.flip()

pygame.quit()