import random
#started 8.3.24

#inventory
class inventory:
    money = 0
    health = 20
    energy = 100
    contents = []

#loot
def getLoot(table):
    objLoot = random.randint(0, (len(table) - 1))
    item = table[objLoot]
    return item

class basicSword:
    name ='basic sword'
    rarity = 'common'
    damage = 3
    miningDamage = 1
    useType = 'one handed'
    durability = 25
    code = '00000001'


class basicPick:
    name = 'basic pickaxe'
    rarity = 'common'
    damage = 1
    miningDamage = 3
    useType = 'two handed'
    durability = 30
    code = '00000010'

class ironOre:
    name = 'iron ore'
    damage = 2

class coal:
    name = 'coal'
    damage = 1

class stone:
    name = 'stone'
    damage = 1
    durability = 1

rockLoot = [ironOre, coal, coal, stone, stone, stone, stone]

basicLoot = [basicPick, basicSword] 

loot = [basicLoot, rockLoot]

#Enemies
class skeleton:
    name = 'skeleton'
    health = 5
    damage = 1
    loot = basicLoot
    code = '00000011'
    points = 2
    accuracy = 6

class rock:
     name = 'rock'
     health = 3
     damage = 0
     loot = rockLoot
     code = '00000100'
     points = 1
     accuracy = 0

enemies = [skeleton, rock]

#important variables
chests = []
diffScalar = 0
chest = []
nearbyEnemies = []
roomOptions = []
nearbyItems = []
droppedItems = []
room = 0
move = True


#functions
def load():
    inventoryList = [inventory.money, inventory.health, inventory.energy, inventory.contents]
    entities = [enemies, inventoryList]
    with open('savedata.txt', 'r') as openFile:
        for x in openFile:
            data = openFile.readline(x)
            for y in entities:
                for i in y:
                    if data == i.code:
                        print('added', data, ' to inventory')

def save():
    pass

def addToInventory(item):
    inventory.contents.append(item)

def pickUp(deezNutz):
    for x in nearbyItems:
            if deezNutz == x.name:
                addToInventory(x)
                nearbyItems.remove(x)
                print('Item', x, 'added to inventory')
            else:
                response = input('Item not present, please pick another action ')

def drop(item):
    nearbyItems.append(item)
    inventory.contents.remove(item)

def open(thing, part):
    if thing == 'chest':
        for x in part:
            droppedItems.append(x)
            part.remove(x)
        for y in droppedItems:
            nearbyItems.append(y)
        print(droppedItems, 'have been dropped on the floor')
        chests.pop(response - 1)
        droppedItems.clear()
    elif thing == 'door':
        print('You opened the door')
        #add boss room here

def diffScale(diff):
    diff = float(diff) + 0.2
    return diff

def spawnChests():
    NofChests = random.randint(0, 3)
    return int(NofChests)

def makeChest(loot, amount):
    chests.clear()
    t = 0
    while t < amount:
        NofItems = random.randint(1, 3)
        i = 0
        while i < NofItems:
            chest.append(getLoot(loot))
            i += 1 
        chests.append(chest)
        chest.clear()
        t += 1

def checkLoot():
    pass

def spawnEnemies():
    NofEnemies = random.randint(0, 5)
    points = 5 * diffScalar
    i = 0
    nearbyEnemies.clear()
    while i < NofEnemies and points > 0:
        n = random.randint(0, len(enemies))
        enemy = enemies[n]
        nearbyEnemies.append(enemy)
        i += 1
        

def directions():
    options = ['forward', 'left', 'right']
    roomOptions.clear()
    NofOptions = random.randint(0, 2)
    i = 0 
    while i <= NofOptions:
        option = random.randint(0, 2)
        roomOptions.append(options[option])
        i += 1

def makeRoom(y):
    nearbyItems.clear()
    y += 1
    diffScale(diffScalar)
    makeChest(basicLoot, int(spawnChests()))
    spawnEnemies()
    directions()
    if y == 1 and nearbyEnemies == None:
        nearbyEnemies.append(rock)
        print('''
            
            A rock blocks your way
            You must clear it
              
            ''')
    elif y == 5:
        chests.append('door')

def attack(item, enemy):
    for x in nearbyEnemies:
        if x.name == enemy.name:
            x.health = x.health - item.damage
            if x.health <= 0:
                nearbyEnemies.remove(x)
    print('')
    print('you attacked ', enemy.name, ' for ', item.damage, 'damage.')
    print('')

def enemyMove():
    ran = random.randint(1, len(enemies))
    Eattack = enemies[ran - 1]
    hit = random.randint(1, 10)
    if hit >= Eattack.accuracy:
        inventory.health = inventory.health - Eattack.damage

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
        inventory.contents.append('Ancient Text')
        print('''
              
            You grab the book and leave the room as fast as you possibly could
            You hear a voice in your head, it is faint and you cannot tell what it is saying
            but you know it is there
              
            ''')


#game
game = input('Would you like to start? ')

if game == 'yes':#starts the game (should)
    makeRoom(room)
    start = True
    move = True
else:
    game = input('Would you like to start? ')

while start == True:

    print('The room you are currently in contains ', len(chests), ' chests, ', len(nearbyEnemies), ' enemies, and you can move ', str(roomOptions), '.')
    print('There are ', len(nearbyItems), 'items on the floor')
    print('')
    response = input('What do you want to do? ')


    if inventory.health <= 0 or response == 'end game':
        #save()
        start = False #sets the end of the game
    elif response == 'save game':
       # save()
        print('Game saved ')


    
    if response == 'pick up': #sets the pick up action
        response = input('What would you like to pick up? ')
        pickUp(response)


    elif response == 'attack':#sets the attack action
        response = input('What would you like to attack? ')
        print(nearbyEnemies)
        item = input('What item would you like to use? ')
        for x in enemies:
            if response == x.name:
                for y in inventory.contents:
                    if item == y.name:
                        attack(y, x)
                        move = False
                        


    elif response == 'move':#sets the move action
        response = input('What direction would you like to move? ')
        print(roomOptions)
        if response in ['left', 'right', 'forward']:
            makeRoom(room)
            print('')
            print('you entered the next room. ')
            print('')


    elif response == 'open':#sets the open action
        for x in chests:
            if x == 'door':
                print('')
                print('You see a mysterious door ahead,')
                response = input('What do you do? ')

        response = input('What would you like to open? ')

        if response == 'chest':
            print('There are ', len(chests), 'chests nearby. ')
            response = int(input('Which chest do you wish to open? '))
            if response == 1 or 2 or 3:
                open('chest', chests[response - 1])

        elif response == 'door':
            theStalkerEncounter()
                
        elif response in ['cancel', 'back']:
            response = input('What do you want to do? ')

    elif response == 'drop':
        response = input('What do you want to drop? ')
        for x in inventory.contents:
            if response == x.name:
                drop(x)

    
    elif response == 'set':
        response = input('What do you want to set? ')

        if response == 'items':
            response = input('What item? ')
            for x in loot:
                for y in x:
                    if response == y.name:
                        nearbyItems.append(y)
                        print('')
                        print('Item', y, 'added')
                        print('')

        elif response == 'enemies':
            response = input('Which enemy? ')
            count = int(input('How many? '))
            for x in enemies:
                if response == x.name:
                    i = 0
                    while i < count:
                        nearbyEnemies.append(x)
                        print(x, 'summoned')
                        i += 1
                    


    if move == False:
        enemyMove()