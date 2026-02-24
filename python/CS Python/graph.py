
graph = {'A':[['D', 10]],
         'B': [['C', 7], ['D', 3]], 
         'C': [['B', 10]],
         'D': [['A', 5], ['B', 5]]}
maxProb = 10

for x in graph:
    locate = []
    probs = []
    for y in graph[x]:
        locate.append(y[0])
        probs.append(y[1] / maxProb)
    print(f'{x} connects to {locate}')