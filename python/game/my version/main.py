import random, func

def move(direction):
    if direction == 'right':
        func.player.move(1, 0)
    elif direction == 'left':
        func.player.move(-1, 0)
    elif direction == 'up':
        func.player.move(0, -1)
    elif direction == 'down':
        func.player.move(0, 1)

functions = {'move': move(), }

start = input