import pygame
from random import randint

screen_width, screen_height = 400, 400
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

grid = pygame.PixelArray(screen)

empty = (255, 255, 255)
sand = (255, 0, 0)

def check_movement(pixel):
    pass # pixel array system to be worked on later. more complex than typical, but if done correctly should handle higher resolutions faster.

start = True
while start:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
