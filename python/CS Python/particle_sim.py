import pygame

class particle:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.colour = (0, 0, 0)

    def values(self):
        return f'x: {self.x}, y: {self.y}, type: {self.type}, colour: {self.colour}'
        
    def det_colour(self):
        if self.type == 0:
            self.colour = (255, 255, 255)
        elif self.type == 1:
            self.colour = (255, 0, 0)
        elif self.type == 2:
            self.colour = (0, 0, 255)

    def update(self, dx = 0, dy = 0):
        next_grid[self.y + dy][self.x + dx].type = self.type

    def check_movement(self):
        try:
            below = grid[self.y + 1][self.x].type
        except IndexError:
            below = None
        try:
            below_l = grid[self.y + 1][self.x - 1].type
        except IndexError:
            below_l = None
        try:
            below_r = grid[self.y + 1][self.x + 1].type
        except IndexError:
            below_r = None
        try:
            left = grid[self.y][self.x - 1].type
        except IndexError:
            left = None
        try:
            right = grid[self.y][self.x + 1].type
        except IndexError:
            right = None    

        if self.type == 1:
            try:
                if below == 0:
                    self.update(0, 1)
                elif below_r == 0:
                    if self.x == len(grid[0]):
                        self.update()
                    else:
                        self.update(1, 1)
                elif below_l == 0:
                    if self.x == 0:
                        self.update()
                    else:
                        self.update(-1, 1)
                else:
                    self.update()
            except IndexError:
                self.update()


        if self.type == 2:
            try:
                if below == 0:
                    self.update(0, 1)
                elif below_r == 0:
                    if self.x == len(grid[0]):
                         self.update()
                    else:
                        self.update(1, 1)
                elif below_l == 0:
                    if self.x == 0:
                        self.update()
                    else:
                        self.update(-1, 1)
                elif right == 0:
                    if self.x == len(grid[0]):
                        self.update()
                    else:
                        self.update(1, 0)
                elif left == 0:
                    if self.x == 0:
                        self.update()
                    else:
                        self.update(-1, 0)
                else:
                    self.update()
            except IndexError:
                self.update()


screen_width, screen_height = 800, 800
pixel_size = 10
n_cols = screen_width // pixel_size
n_rows = screen_height // pixel_size
current_type = 1

grid = [[particle(x, y, 0) for x in range(n_cols)] for y in range(n_rows)]

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

start = True
while start:
    clock.tick(75)
    pygame.key.set_repeat(100)
    keys = pygame.key.get_pressed()
    next_grid = [[particle(x, y, 0) for x in range(n_cols)] for y in range(n_rows)]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

    if keys[pygame.K_SPACE]:
        if current_type == 1:
            current_type = 2
        elif current_type == 2:
            current_type = 1

    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0] // pixel_size
    mouse_y = mouse_pos[1] // pixel_size

    try:
        if pygame.mouse.get_pressed()[0]:
            grid[mouse_y - 1][mouse_x].type = current_type
            grid[mouse_y + 1][mouse_x].type = current_type
            grid[mouse_y][mouse_x - 1].type = current_type
            grid[mouse_y][mouse_x + 1].type = current_type
    except IndexError:
        pass

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x].check_movement()
            next_grid[y][x].det_colour()

    grid = next_grid

    for y, row in enumerate(grid):
        for x, pixel in enumerate(row):
            pixel_rect = pygame.Rect(x * pixel_size, y * pixel_size, pixel_size, pixel_size)
            pygame.draw.rect(screen, pixel.colour, pixel_rect)

    pygame.display.flip()
pygame.quit()