import pygame, torch, math, random

device = str('cuda' if torch.cuda.is_available() else 'cpu')
display_scale = 2
screenWidth, screenHeight = display_scale * 640, display_scale * 360        
displaySurface = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
framerate = 5

class rocket:
    def __init__(self, colour = (255, 0, 0)):
        self.width, self.height = 6, 20
        self.pos = torch.tensor([screenWidth / 2 - self.width / 2, screenHeight - self.height])
        self.velocity = torch.tensor([0, -1])
        self.acceleration = torch.tensor([0, 0])
        self.colour = colour
        
    def rotate(self):
        angle = math.atan(self.velocity[1] / self.velocity[0])
        mat = torch.eye(2)
        sine = math.sin(angle)
        cosine = math.cos(angle)
        mat[0, 0] = cosine
        mat[0, 1] = sine
        mat[1, 0] = -sine
        mat[1, 1] = cosine
        self.pos @= mat
        
    def apply_force(self, force):
        self.acceleration += force
        
    def update(self):
        self.velocity += self.acceleration
        self.pos += self.velocity
        self.acceleration *= 0
        
    def show(self):
        #self.rotate()
        pygame.draw.rect(displaySurface, self.colour, (int(self.pos[0]), int(self.pos[1]), self.width, self.height)) 
        
class population:
    def __init__(self, pop_size):
        self.rockets = []
        
        for x in range(pop_size):
            self.rockets.append(rocket())
            
    def run(self):
        for rocket in self.rockets:
            rocket.velocity[0] = random.randint(-3, 3)
            rocket.update()
            rocket.show()
            
class dna:
    def __init__(self):
        self.genes = []
        self.len = len(self.genes)
            
pop = population(3)
lifespan = 600
    
start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            
    displaySurface.fill((0, 0, 0))        
    
    pop.run()
    
    pygame.display.flip()
    clock.tick(framerate)