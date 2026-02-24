

grid = {
    'a': {
        '1': None,
        '2': None,
        '3': None
    },
    'b': {
        '1': None,
        '2': None,
        '3': None
    },
    'c': {
        '1': None,
        '2': None,
        '3': None
    }
}

gridUI = ['  a     b     c'.format, '1 {grid[a[1]]}   |   {grid[b[1]]}   |   {grid[c[1]]}'.format, '  ---|-----|----'.format, '2 {grid[a[2]]}   |   {grid[b[2]]}   |   {grid[c[2]]}'.format, '  ---|-----|----'.format, '3 {grid[a[3]]}   |   {grid[b[3]]}   |   {grid[c[3]]}'.format]

for x in gridUI:
    print(grid[x])

response = input('What is your first move? ')
response.strip()
response.lower()
print(response)

grid[response[:1], response[:-1]] = 'X'
print(grid)

#unfinished 