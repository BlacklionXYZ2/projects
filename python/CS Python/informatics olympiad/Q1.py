print('Oscar Hunt Brown, Ashby School')
from math import floor

def str_to_idx(value: str):
    return ord(value.upper()) - 65
    
def idx_to_str(value: int):
    return chr(value.upper() + 65)

alph = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' ]

class grid:
    def __init__(self, block):
        self.grid = {'A': block, 'B': block, 'C': block, 'D': block, 'E': block, 'F': block, 'G': block, 'H': block, 'I': block, 'J': block, 'K': block, 'L': block, 'M': block, 'N': block, 'O': block, 'P': block, 'Q': block, 'R': block, 'S': block, 'T': block, 'U': block, 'V': block, 'W': block, 'X': block, 'Y': block}

    def convert_coords(self, coords: list):
        coord_set = []
        for x in coords:
            y = floor(x / 5)
            x -= 5 * y
            coord_set.append([x, y])
        print(coord_set)
        return coord_set
    
    def normalise(self, data: list):
        coords = [0, 0]
        for x in range(len(data)):
            coords[0] += data[x][0] * (5 ** (len(data) - (x + 1)))
            coords[1] += data[x][1] * (5 ** (len(data) - (x + 1)))
        return coords

    def find_node_coords(self, target: str):
        target = [char.upper() for char in target]
        indexes = []
        for x in target:
            indexes.append(str_to_idx(x))
        indexes = self.convert_coords(indexes)
        indexes = self.normalise(indexes)
     

grid1 = grid(None)  # 5 by 5 grid
grid2 = grid(grid1) # 5^2 by 5^2 grid
grid3 = grid(grid2) # 5^3 by 5^3 grid
print(grid2.find_node_coords('BI'))