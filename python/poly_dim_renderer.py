from math import sin, cos, sqrt
import pygame

def find_points(dim):
    n_points = (2 ** dim)
    points = []
    for x in range(n_points):
        point = list(bin(x)[2:])
        point = list(int(pos) for pos in point)
        if len(point) < dim:
            for _ in range(dim - len(point)):
                point.insert(0, 0)
        point = list(-1 if pos == 0 else 1 for pos in point)
        points.append(point)
    return points

def find_edges(points):
    edges = []
    for pointA in range(len(points)):
        for pointB in range(len(points)):
            diff_coords = sum(1 if points[pointA][x] != points[pointB][x] else 0 for x in range(len(points[0])))
            if diff_coords == 1:
                edges.append((pointA, pointB))
    for edge1 in edges:
        for edge2 in edges:
            if edge1[0] == edge2[1] and edge1[1] == edge2[0]:
                edges.remove(edge2)
    return edges

class matrix:
    def __init__(self, size):
        self.size = size
        self.mat = [[0 for _ in range(size)] for _ in range(size)]
        self.sin = [0, 0]
        self.cos1 = [0, 0]
        self.nsin = [0, 0]
        self.cos2 = [0, 0]
    
    def rotate(self, angle):
        sine = sin(angle)
        cosine = cos(angle)
        self.mat[self.cos1[1]][self.cos1[0]] = cosine
        self.mat[self.sin[1]][self.sin[0]] = sine
        self.mat[self.nsin[1]][self.nsin[0]] = -sine
        self.mat[self.cos2[1]][self.cos2[0]] = cosine

    def print(self):
        print('')
        for x in self.mat:
            print(x)
        # print(self.cos1, self.sin)
        # print(self.nsin, self.cos2)

def create_matrices(dim):
    rot_mats = []
    for x in range(dim):
        for y in range(x + 1, dim):
            current = matrix(dim)
            for idx in range(dim):
                current.mat[idx][idx] = 1
            current.cos1 = [x, x]
            current.sin = [x, y]
            current.nsin = [y, x]
            current.cos2 = [y, y]
            rot_mats.append(current)
    return rot_mats

def project_to_2d(points):
    projected = [point[:] for point in points]
    camera_distance = sqrt(len(points[0])) + 1.0
    while len(projected[0]) > 2:
        for i in range(len(projected)):
            point = projected[i]
            z = point[-1]
            scale = camera_distance / (camera_distance - z) if (camera_distance - z) != 0 else 1.0
            projected[i] = [val * scale for val in point[:-1]]

        max_val = max(abs(val) for p in projected for val in p)
        if max_val > 0:
            for i in range(len(projected)):
                projected[i] = [val / max_val for val in projected[i]]
    return projected

def matmul(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])
    result = [[0.0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python Hypercube Renderer")
clock = pygame.time.Clock()

dim = 10
scale = 200
        
points = find_points(dim)
edges = find_edges(points)
mats = create_matrices(dim)
angle = 0

print(f"{len(points)} Vertices, {len(edges)} Edges.")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))

    for idx, mat in enumerate(mats):
        mat.rotate(angle * (1.0 + idx * 0.1))

    master_mat = mats[0].mat
    for i in range(1, len(mats)):
        master_mat = matmul(master_mat, mats[i].mat)

    rot_points = matmul(points, master_mat)
    proj_points = project_to_2d(rot_points)

    screen_points = []
    for p in proj_points:
        x = int(p[0] * scale + screen_width / 2)
        y = int(p[1] * scale + screen_height / 2)
        screen_points.append((x, y))
    for edge in edges:
        pygame.draw.line(screen, (200, 200, 200), screen_points[edge[0]], screen_points[edge[1]], 1)
    for p in screen_points:
        pygame.draw.circle(screen, (0, 255, 255), p, 4)

    pygame.display.flip()
    clock.tick(60)
    angle += 0.05 / dim**1.5