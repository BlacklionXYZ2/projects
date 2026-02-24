import random

chests = []
chest = []
base = ['monkey', 'car', 'apple']

def getLoot(table):
    num = random.randint(1, 3)
    item = table[num - 1]
    return item

def makeChest(loot, amount):
    chests.clear()
    t = 0
    while t < amount:
        chest.clear()
        NofItems = random.randint(1, 3)
        print(NofItems)
        i = 0
        while i < NofItems:
            item = getLoot(loot)
            print(item)
            chest.append(item)
            print(chest)
            i += 1 
        hold = chest
        print(hold)
        chests.append(hold)
        print(chests)
        t += 1
    print(chests)

response = input('Y/N')
if response == 'y':
    makeChest(base, 1)
    print(chests)