from math import sin, cos, pi
import torch

def find_points(dim):
    values = torch.tensor([-1.0, 1.0])
    points = torch.cartesian_prod(*[values for _ in range(dim)])
    return points

def find_edges(points):
    diff_pos = points.unsqueeze(1) != points.unsqueeze(0)
    diff_counts = diff_pos.sum(dim = 2)
    edge_mat = torch.triu(diff_counts == 1)
    edge_idx = torch.nonzero(edge_mat)
    return tuple(edge_idx.tolist())

class matrix:
    def __init__(self, size):
        self.size = size
        self.mat = torch.eye(size)
        self.sin = [0, 0]
        self.cos1 = [0, 0]
        self.nsin = [0, 0]
        self.cos2 = [0, 0]
        self.angle = 0
    
    def rotate(self, angle):
        self.angle += angle
        sine = sin(self.angle)
        cosine = cos(self.angle)
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
            current.cos1 = [x, x]
            current.sin = [x, y]
            current.nsin = [y, x]
            current.cos2 = [y, y]
            rot_mats.append(current)
    return rot_mats
        
        
dim = 14
points = find_points(dim)
edges = find_edges(points)
mats = create_matrices(dim)
master_mat = matrix(dim)
angle = pi / 2
for mat in mats:
    mat.print()
    mat.rotate(angle)
    master_mat.mat @= mat.mat
master_mat.print()