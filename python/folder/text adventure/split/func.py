import random
import var
import ent
#functions

def getLoot(table):
    objLoot = random.randint(0, (len(table) - 1))
    item = table[objLoot]
    return item

# def load():
#     inventoryList = [ent.inventory.money, ent.inventory.health, ent.inventory.energy, ent.inventory.contents]
#     entities = [ent.enemies, inventoryList]
#     with open('savedata.txt', 'r') as openFile:
#         for x in openFile:
#             data = openFile.readline(x)
#             for y in entities:
#                 for i in y:
#                     if data == i.code:
#                         print('added', data, ' to inventory')

# def save():
#     pass

def addToInventory(item):
    ent.inventory.contents.append(item)

def pickUp(item):
    for x in var.nearbyItems: 
        if item == x.name:
            addToInventory(x)
            var.nearbyItems.remove(x)
            print(f'Item {x} added to inventory')
        else:
            var.response = input('Item not present, please pick another action ')

def drop(item):
    var.nearbyItems.append(item)
    ent.inventory.contents.remove(item)

def open(thing, part):
    if thing == 'chest':
        var.droppedItems.clear()
        for x in part:
            store = x
            part.remove(x)
            var.droppedItems.append(store)
        for x in var.droppedItems:
            var.nearbyItems.append(x)
        print(var.droppedItems, 'have been dropped on the floor')
        var.chests.remove(part)
    elif thing == 'door':
        print('You opened the door')
        #add boss room here
    
diffScale = lambda diff : diff + 0.2

def spawnChests():
    NofChests = random.randint(0, 3)
    return NofChests

def makeChest(loot, amount):
    var.chests.clear()
    t = 0
    while t < amount:
        var.chest.clear()
        NofItems = random.randint(1, 3)
        # print(NofItems)
        i = 0
        while i < NofItems:
            item = getLoot(loot)
            # print(item)
            var.chest.append(item)
            i += 1 
        var.chests.append(var.chest)
        t += 1

def checkLoot():
    pass

def spawnEnemies():
    var.nearbyEnemies.clear()
    NofEnemies = random.randint(1, 5)
    points = 5 * var.diffScalar
    i = 0
    #print(i, points)
    while i < NofEnemies and points > 0:
        n = random.randint(0, len(ent.enemies) - 1)
        #print(n)
        enemy = ent.enemies[n]
        points -= ent.enemies[n].points
        #print(enemy)      
        var.nearbyEnemies.append(enemy)
        i += 1
        

def directions():
    options = ['forward', 'left', 'right']
    var.roomOptions.clear()
    NofOptions = random.randint(0, 2)
    i = 0 
    while i <= NofOptions:
        option = random.randint(0, 2)
        if options[option] in var.roomOptions and var.roomOptions != []:
            var.rounds += 1
            if var.rounds >= 1016:
                var.roomOptions = ['forward', 'left', 'right']
                var.rounds = 0
            else:
                directions()
        else:
            var.roomOptions.append(options[option])
            i += 1

def makeRoom(y):
    var.nearbyItems.clear()
    y += 0.2
    diffScale(var.diffScalar)
    makeChest(ent.basicLoot, spawnChests())
    spawnEnemies()
    directions()
    if y == 0.2 and var.nearbyEnemies == None:
        var.nearbyEnemies.append(ent.rock)
        print('''
            
            A rock blocks your way.
            You must clear it.
              
            ''')
    # elif y == 5:
    #     var.chests.append('door')

def attack(item, enemy):
    for x in var.nearbyEnemies:
        if x.name == enemy.name:
            x.health = x.health - item.damage
            if x.health <= 0:
                dropLoot(x)
                var.nearbyEnemies.remove(x)
    diffScale(var.diffScalar)
    print('')
    print(f'you attacked {enemy.name} for {item.damage} damage.')
    print('')

def enemyMove(enemy):
    hit = random.randint(1, 10)
    if hit >= enemy.accuracy:
        ent.inventory.health = ent.inventory.health - enemy.damage

    print(f'{enemy.name}, hit you for {enemy.damage}, damage ')

def dropLoot(enemy):
    rand = random.randint(0, len(enemy.loot) - 1)
    x = enemy
    print(x.loot[rand], 'dropped on the floor')
    var.nearbyItems.append(x.loot[rand])

def durability(item):
    item.durability -= 1
    if item.durability <= 0:
        ent.inventory.contents.remove(item)
        print(f'{item} has broken. ')

def itemCheck(item):
    for x in ent.inventory.contents:
        if item == x.name:
            if x.itemType != 'potion':
                print(f'Name: {x.name}')
                print(f'Damage: {x.damage}')
                print(f'Damage type: {x.damageType}')
                print(f'Durability: {x.durability}')

            elif x.itemType == 'potion':
                print(f'Name: {x.name}')
                print(f'Damage: {x.damage}')
                print(f'Effect:', x.effect)
                print(f'Effect type: {x.effectType}')
                print(f'Durability: {x.durability}')

        else:
            print('Item unavailable ')
            print('')

def bestiary(enemy):
    for x in ent.enemies:
        if enemy == x.name:
            print('')
            print(f'Name: {x.name}')
            print(f'Health: {x.health}')
            print(f'Damage: {x.damage}')
            print(f'Damage type: {x.damageType}')
            print(f'Accuracy: {x.accuracy}')
            print(f'Size: {x.size}')
            print(f'Loot: {x.loot}')
            print('')
            print(f'Description: {x.description}')
            print('')

def heal(amount):
    ent.inventory.health += int(amount)
    if ent.inventory.health > ent.inventory.maxHealth:
        x = ent.inventory.health
        x -= ent.inventory.maxHealth
        x = int(amount) - x
        ent.inventory.health = ent.inventory.maxHealth
        print(f'You were healed for {x} health ')
    else:
        print(f'You were healed for {int(amount)} health ')
    print('')

def inventoryCheck():
    print('')
    print(f'Health: {ent.inventory.health}')
    print(f'Energy: {ent.inventory.energy}')
    print(f'Inventory: {ent.inventory.contents}')
    print('')

def theStalkerEncounter():
    print('''
          
        You see a creature bathed in darkness
        It sees you
        The creature panics and scrambles away
        You notice a book perched on a pedestal
        You creep closer to take a look
          
        ''')
    response = input('Do you take the mysterious text? ')
    if response == 'yes':
        ent.inventory.contents.append('Ancient Text')
        print('''
              
            You grab the book and leave the room as fast as you possibly could
            You hear a voice in your head, it is faint and you cannot tell what it is saying
            but you know it is there
              
            ''')
