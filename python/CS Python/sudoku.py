import random

response = input('input size (x y)')
dims = []
try:
    for x in response.split():
        dims.append(int(x))
except TypeError:
    print('Invalid input, try again')

grid = [None] * dims[1]
for x in grid:
    x = x * dims[0]
gridSize = len(grid) * len(grid[0])

response = input('what difficulty? (easy/hard)')
if response == 'easy':
    revealed = random.randint(int((2 * gridSize) / 3), int((3 * gridSize) / 4))
elif response == 'hard':
    revealed = random.randint(int(gridSize / 3), int((3 * gridSize) / 4))

for i in range(0, revealed):
    x = random.randint(0, len(grid[0]) - 1)
    y = random.randint(0, len(grid) - 1)
    num = random.randint(1, 9)
    grid[y][x] = num

for x in grid:
    out = 'a'
    for y in x:
        out += y # fix output format later
print(out)

response = input('')