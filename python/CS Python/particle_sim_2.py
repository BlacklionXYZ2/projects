import pygame
from random import randint, choice

class particle:
    def __init__(self, x, y, p_type):
        self.x = x
        self.y = y
        self.type = p_type
        self.colour = (255, 255, 255)
        self.updated = False 

    def det_colour(self):
        if self.type == 0:
            self.colour = (255, 255, 255)
        elif self.type == 1:
            self.colour = (194, 178, 128)
        elif self.type == 2:
            self.colour = (0, 0, 255)
        elif self.type == 3:
            self.colour = (139, 69, 19)
        elif self.type == 4:
            self.colour = choice([(255, 0, 0), (255, 140, 0), (255, 215, 0)])
        elif self.type == 5:
            self.colour = choice([(200, 200, 200), (220, 220, 220)])

    def move(self, dx, dy):
        target = grid[self.y + dy][self.x + dx]
        
        if target.type == 4: 
            target.type = self.type
            if self.type == 2:
                self.type = 5 
            else:
                self.type = 0
        else: 
            target.type, self.type = self.type, target.type
            
        target.updated = True
        self.updated = True

    def check_movement(self):
        if self.type == 0 or self.updated:
            return

        can_down = self.y + 1 < n_rows
        can_up = self.y - 1 >= 0
        can_left = self.x - 1 >= 0
        can_right = self.x + 1 < n_cols

        # --- SAND ---
        if self.type == 1: 
            if can_down and grid[self.y + 1][self.x].type in [0, 2, 4, 5]:
                self.move(0, 1)
            elif can_down and can_left and grid[self.y + 1][self.x - 1].type in [0, 2, 4, 5]:
                self.move(-1, 1)
            elif can_down and can_right and grid[self.y + 1][self.x + 1].type in [0, 2, 4, 5]:
                self.move(1, 1)

        # --- WATER ---
        elif self.type == 2: 
            if can_down and grid[self.y + 1][self.x].type in [0, 4]:
                self.move(0, 1)
            elif can_down and can_left and grid[self.y + 1][self.x - 1].type in [0, 4]:
                self.move(-1, 1)
            elif can_down and can_right and grid[self.y + 1][self.x + 1].type in [0, 4]:
                self.move(1, 1)
            elif can_right and grid[self.y][self.x + 1].type in [0, 4]:
                self.move(1, 0)
            elif can_left and grid[self.y][self.x - 1].type in [0, 4]:
                self.move(-1, 0)

        # --- WOOD ---
        elif self.type == 3:
            pass

        # --- FIRE ---
        elif self.type == 4:
            if randint(1, 100) < 15: 
                self.type = 0
                self.updated = True
                return

            neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for dx, dy in neighbors:
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < n_cols and 0 <= ny < n_rows:
                    if grid[ny][nx].type == 3: 
                        if randint(1, 100) < 5: 
                            grid[ny][nx].type = 4
                            grid[ny][nx].updated = True

            if can_up:
                dx = choice([-1, 0, 1]) 
                nx = self.x + dx
                if 0 <= nx < n_cols and grid[self.y - 1][nx].type == 0:
                    self.move(dx, -1)

        # --- STEAM ---
        elif self.type == 5:
            if randint(1, 100) < 5:
                self.type = 0
                self.updated = True
                return

            if can_up:
                dx = choice([-1, 0, 1]) 
                nx = self.x + dx
                if 0 <= nx < n_cols and grid[self.y - 1][nx].type == 0:
                    self.move(dx, -1)
                elif can_left and grid[self.y][self.x - 1].type == 0:
                    self.move(-1, 0)
                elif can_right and grid[self.y][self.x + 1].type == 0:
                    self.move(1, 0)


screen_width, screen_height = 800, 800
pixel_size = 4
n_cols = screen_width // pixel_size
n_rows = screen_height // pixel_size

grid = [[particle(x, y, 0) for x in range(n_cols)] for y in range(n_rows)]

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

current_type = 1 
materials = {1: "Sand", 2: "Water", 3: "Wood", 4: "Fire"}
start = True

while start:
    clock.tick(240)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_type = (current_type % 4) + 1
                print(f"Switched to {materials[current_type]}")

    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0] // pixel_size
    mouse_y = mouse_pos[1] // pixel_size

    if pygame.mouse.get_pressed()[0]:
        try:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if 0 <= mouse_y + dy < n_rows and 0 <= mouse_x + dx < n_cols:
                        grid[mouse_y + dy][mouse_x + dx].type = current_type
        except IndexError:
            pass


    for row in grid:
        for p in row:
            p.updated = False

    for y in range(n_rows - 1, -1, -1):
        for x in range(n_cols):
            grid[y][x].check_movement()


    screen.fill((255, 255, 255))
    for y in range(n_rows):
        for x in range(n_cols):
            pixel = grid[y][x]
            pixel.det_colour() 
            if pixel.type != 0:
                pygame.draw.rect(screen, pixel.colour, (x * pixel_size, y * pixel_size, pixel_size, pixel_size))

    pygame.display.flip()

pygame.quit()