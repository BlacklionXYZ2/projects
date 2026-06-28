import pygame, numpy as np
from car import car, screenx, screeny, center, r

pygame.init()
screen = pygame.display.set_mode((screenx, screeny))
clock = pygame.time.Clock()
fr = 60
epoch_time = 300
time = 0

car1 = car(50, (r[0], center[1]))

running = True
while running:
    dt = clock.tick(fr) / 1000
    time += 1
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if time == epoch_time:
        print('generation finished')
        car1.next_generation()
        print('next generation')
        time = 0

    car1.forward()

    mask_x_greater = car1.pos[:, 0] > screenx # if x > max
    car1.pos[mask_x_greater, 0] = screenx
    mask_x_lesser = car1.pos[:, 0] < 0        # if x < 0
    car1.pos[mask_x_lesser, 0] = 0
    mask_y_greater = car1.pos[:, 1] > screeny # if y > max
    car1.pos[mask_y_greater, 1] = screeny
    mask_y_lesser = car1.pos[:, 1] < 0        # if y < 0
    car1.pos[mask_y_lesser, 1] = 0

    car1.force += car1.controls['w'] * dt
    car1.force -= car1.force * car1.controls['s'] * 0.7 * dt
    mask_air_res = car1.controls['w'] + car1.controls['s'] == 0
    car1.force[mask_air_res] -= car1.controls['w'][mask_air_res]
    car1.angle -= car1.controls['a'] * 2
    car1.angle += car1.controls['d'] * 2

    mask_angle_greater = car1.angle > 360
    car1.angle[mask_angle_greater] -= 360
    mask_angle_lesser = car1.angle < 0
    car1.angle[mask_angle_lesser] += 360
    
    mask_force = car1.force < 0
    car1.force[mask_force] = 0

    car1.update_pos(dt * 10)
    car1.check_alive()
    car1.update_scores(center)

    screen.fill(0)
    pygame.draw.circle(screen, (128, 128, 128), center, np.min(center))
    pygame.draw.circle(screen, (32, 128, 32), center, np.min(r))

    for coords in car1.pos:
        pygame.draw.circle(screen, car1.col, coords, 25)

    pygame.display.flip()

pygame.quit()