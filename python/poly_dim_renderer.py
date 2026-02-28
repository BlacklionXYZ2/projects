from math import sin, cos, pi

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
        
        
dim = 10
points = find_points(dim)
edges = find_edges(points)
mats = create_matrices(dim)
for x in mats:
    x.rotate(pi / 2)
    x.print()