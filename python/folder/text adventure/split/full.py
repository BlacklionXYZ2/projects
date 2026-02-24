import random

response = None
chests = []
diffScalar = 0.0
chest = []
nearbyEnemies = []
roomOptions = []
nearbyItems = []
droppedItems = []
move = True
rounds = 0 



#inventory
class inventory:
    money = 0
    health = 20
    maxHealth = 20
    energy = 100
    contents = []

#loot
class basicSword:
    name ='basic sword'
    damage = 3
    damageType = 'kinetic'
    itemType = 'sword'
    durability = 5


class basicPick:
    name = 'basic pickaxe'
    damage = 3
    damageType = 'mining'
    itemType = 'pickaxe'
    durability = 5

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

class rareSword:
    name = 'rare sword'
    damage = 5
    damageType = 'kinetic'
    itemType = 'sword'
    durability = 10

class rarePick:
    name = 'rare pickaxe'
    damage = 7
    damageType = 'mining'
    itemType = 'pickaxe'
    durability = 10

class blueOrb:
    name = 'blue orb'
    damage = 15
    damageType = 'magic'
    itemType = 'item'
    durability = 1

class healingPotion:
    name = 'healing potion'
    damage = '5'
    damageType = 'potion'
    itemType = 'potion'
    effect = 'healing'
    effectType = 'buff'
    durability = 1

rockLoot = [ironOre, coal, coal, stone, stone, stone, stone]

basicLoot = [basicPick, basicSword, ironOre, healingPotion] 

rareLoot = [rareSword, rarePick, blueOrb, healingPotion]

loot = [basicLoot, rockLoot, rareLoot]

#Enemies
class skeleton:
    name = 'skeleton'
    health = 5
    damage = 1
    size = 'medium'
    description = "The humble skeleton. Fragile. Weak. It is but a mere scout, slay it before more appear."
    damageType = 'kinetic'
    loot = basicLoot
    points = 2
    accuracy = 6
    trFaAtt = True

class rock:
    name = 'rock'
    health = 3
    damage = 0
    size = 'small'
    description = "It's a rock, what did you think it was?"
    damageType = 'kinetic'
    loot = rockLoot
    points = 1
    accuracy = 0
    trFaAtt = False

class golem:
    name = 'golem'
    health = 10
    damage = 4
    size = 'large'
    description = 'A hulking mass of rock here only to give you the first ticket on the pain train to the afterlife. This absolute unit of a boulder is incredibly tough but isnt very smart, take advantage of that.'
    damageType = 'kinetic'
    loot = rareLoot
    points = 3
    accuracy = 3
    trFaAtt = True

enemies = [skeleton, rock, golem]




#functions

def getLoot(table):
    objLoot = random.randint(0, (len(table) - 1))
    item = table[objLoot]
    return item

# def load():
#     inventoryList = [inventory.money, inventory.health, inventory.energy, inventory.contents]
#     entities = [enemies, inventoryList]
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
    inventory.contents.append(item)

def pickUp(item):
    for x in nearbyItems: 
        if item == x.name:
            addToInventory(x)
            nearbyItems.remove(x)
            print(f'Item {x} added to inventory')
        else:
            response = input('Item not present, please pick another action ')

def drop(item):
    nearbyItems.append(item)
    inventory.contents.remove(item)

def open(thing, part):
    if thing == 'chest':
        droppedItems.clear()
        for x in part:
            store = x
            part.remove(x)
            droppedItems.append(store)
        for x in droppedItems:
            nearbyItems.append(x)
        print(droppedItems, 'have been dropped on the floor')
        chests.remove(part)
    elif thing == 'door':
        print('You opened the door')
        #add boss room here
    
diffScale = lambda diff : diff + 0.2

def spawnChests():
    NofChests = random.randint(0, 3)
    return NofChests

def makeChest(loot, amount):
    chests.clear()
    t = 0
    while t < amount:
        chest.clear()
        NofItems = random.randint(1, 3)
        # print(NofItems)
        i = 0
        while i < NofItems:
            item = getLoot(loot)
            # print(item)
            chest.append(item)
            i += 1 
        chests.append(chest)
        t += 1

def checkLoot():
    pass

def spawnEnemies():
    nearbyEnemies.clear()
    NofEnemies = random.randint(1, 5)
    points = 5 * diffScalar
    i = 0
    #print(i, points)
    while i < NofEnemies and points > 0:
        n = random.randint(0, len(enemies) - 1)
        #print(n)
        enemy = enemies[n]
        points -= enemies[n].points
        #print(enemy)      
        nearbyEnemies.append(enemy)
        i += 1
        

def directions():
    options = ['forward', 'left', 'right']
    roomOptions.clear()
    NofOptions = random.randint(0, 2)
    i = 0 
    while i <= NofOptions:
        option = random.randint(0, 2)
        if options[option] in roomOptions and roomOptions != []:
            rounds += 1
            if rounds >= 1016:
                roomOptions = ['forward', 'left', 'right']
                rounds = 0
            else:
                directions()
        else:
            roomOptions.append(options[option])
            i += 1

def makeRoom(y):
    nearbyItems.clear()
    y += 0.2
    diffScale(diffScalar)
    makeChest(basicLoot, spawnChests())
    spawnEnemies()
    directions()
    if y == 0.2 and nearbyEnemies == None:
        nearbyEnemies.append(rock)
        print('''
            
            A rock blocks your way.
            You must clear it.
              
            ''')
    # elif y == 5:
    #     chests.append('door')

def attack(item, enemy):
    for x in nearbyEnemies:
        if x.name == enemy.name:
            x.health = x.health - item.damage
            if x.health <= 0:
                dropLoot(x)
                nearbyEnemies.remove(x)
    diffScale(diffScalar)
    print('')
    print(f'you attacked {enemy.name} for {item.damage} damage.')
    print('')

def enemyMove(enemy):
    hit = random.randint(1, 10)
    if hit >= enemy.accuracy:
        inventory.health = inventory.health - enemy.damage

    print(f'{enemy.name}, hit you for {enemy.damage}, damage ')

def dropLoot(enemy):
    rand = random.randint(0, len(enemy.loot) - 1)
    x = enemy
    print(x.loot[rand], 'dropped on the floor')
    nearbyItems.append(x.loot[rand])

def durability(item):
    item.durability -= 1
    if item.durability <= 0:
        inventory.contents.remove(item)
        print(f'{item} has broken. ')

def itemCheck(item):
    for x in inventory.contents:
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
    for x in enemies:
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
    inventory.health += int(amount)
    if inventory.health > inventory.maxHealth:
        x = inventory.health
        x -= inventory.maxHealth
        x = int(amount) - x
        inventory.health = inventory.maxHealth
        print(f'You were healed for {x} health ')
    else:
        print(f'You were healed for {int(amount)} health ')
    print('')

def inventoryCheck():
    print('')
    print(f'Health: {inventory.health}')
    print(f'Energy: {inventory.energy}')
    print(f'Inventory: {inventory.contents}')
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
        inventory.contents.append('Ancient Text')
        print('''
              
            You grab the book and leave the room as fast as you possibly could
            You hear a voice in your head, it is faint and you cannot tell what it is saying
            but you know it is there
              
            ''')





l = True

#game
while l == True:
    game = input('Would you like to start? ')

    if game == 'yes':#starts the game (should)
        makeRoom(diffScalar)
        start = True
        move = True
        l = False
    else:
        game = input('Would you like to start? ')

while start == True:

    print(f'The room you are currently in contains {len(chests)} chests, {len(nearbyEnemies)} enemies, and you can move {str(roomOptions)}.')
    print(f'There are {len(nearbyItems)} items on the floor')
    print('')
    response = input('What do you want to do? ')


    if inventory.health <= 0 or response == 'end game':
        #save()
        start = False #sets the end of the game
        print('Game has ended. ')
    elif response == 'save game':
       # save()
        print('Game saved ')


    
    if response == 'pick up': #sets the pick up action
        print(nearbyItems)
        response = input('What would you like to pick up? ')

        if response in ['cancel', 'back']:
            pass
        
        pickUp(response)


    elif response == 'attack':#sets the attack action
        print(nearbyEnemies)
        response = input('What would you like to attack? ')

        if response in ['cancel', 'back']:
            pass
        
        if response != None or 'back':
            item = input('What item would you like to use? ')
            for x in enemies:
                if response == x.name:
                    for y in inventory.contents:
                        if item == y.name:
                            attack(y, x)
                            move = False
                        


    elif response == 'move':#sets the move action
        print(roomOptions)
        response = input('What direction would you like to move? ')
        if response in ['left', 'right', 'forward']:
            makeRoom(diffScalar)
            print('')
            print('you entered the next room. ')
            print('')
        
        elif response in ['cancel', 'back']:
            pass


    elif response == 'open':#sets the open action
        # for x in chests:
        #     if x == 'door':
        #         print('')
        #         print('You see a mysterious door ahead,')
        #         response = input('What do you do? ')

        response = input('What would you like to open? ')

        if response == 'chest':
            print(f'There are {len(chests)} chests nearby. ')
            response = input('Which chest do you wish to open? ')
            if int(response) == 1 or 2 or 3:
                # print(chests[int(response) - 1])
                open('chest', chests[int(response) - 1])
            else:
                print('Invalid')
                response = input('Which chest do you wish to open')

        elif response == 'door':
            theStalkerEncounter()
                
        elif response in ['cancel', 'back']:
            pass


    elif response == 'drop':
        response = input('What do you want to drop? ')

        if response in ['cancel', 'back']:
            pass

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

        elif response == 'chest':
            response = input('What loot should be in the chest?')
            if response == 'basic':
                makeChest(basicLoot, 1)

        elif response in ['cancel', 'back']:
            pass
                    

    elif response == 'check':

        response = input('What do you  want to check? ')

        if response == 'loot gen':
            print(getLoot(basicLoot))

        elif response == 'chest gen':
            makeChest(basicLoot, 1)
            print(chests)

        elif response == 'inventory':
            inventoryCheck()

        elif response == 'item':
            response = input('Which item do you wish to check? ')

            itemCheck(response)


    elif response == 'bestiary':
        response = input('What creature do you hope to know? ')

        bestiary(response)

    
    elif response == 'use':
        print(inventory.contents)
        response = input('What item do you want to use? ')

        for x in inventory.contents:
            if response == x.name:
                if x.damageType == 'potion':
                    if x.effectType == 'buff': 
                        if x.effect == 'healing':
                            heal(x.damage)


            


    if move == False:
        for x in nearbyEnemies:
            if x.trFaAtt == True:
                enemyMove(x)