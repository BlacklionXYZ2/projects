import random
import func
import ent
import var
#started 8.3.24
#v1 finished 12.4.24
l = True

#game
while l == True:
    game = input('Would you like to start? ')

    if game == 'yes':#starts the game (should)
        func.makeRoom(var.diffScalar)
        start = True
        var.move = True
        l = False
    else:
        game = input('Would you like to start? ')

while start == True:

    print(f'The room you are currently in contains {len(var.chests)} chests, {len(var.nearbyEnemies)} enemies, and you can move {str(var.roomOptions)}.')
    print(f'There are {len(var.nearbyItems)} items on the floor')
    print('')
    var.response = input('What do you want to do? ')


    if ent.inventory.health <= 0 or var.response == 'end game':
        #save()
        start = False #sets the end of the game
        print('Game has ended. ')
    elif var.response == 'save game':
       # save()
        print('Game saved ')


    
    if var.response == 'pick up': #sets the pick up action
        print(var.nearbyItems)
        var.response = input('What would you like to pick up? ')

        if var.response in ['cancel', 'back']:
            pass
        
        func.pickUp(var.response)


    elif var.response == 'attack':#sets the attack action
        print(var.nearbyEnemies)
        var.response = input('What would you like to attack? ')

        if var.response in ['cancel', 'back']:
            pass
        
        if var.response != None or 'back':
            item = input('What item would you like to use? ')
            for x in ent.enemies:
                if var.response == x.name:
                    for y in ent.inventory.contents:
                        if item == y.name:
                            func.attack(y, x)
                            var.move = False
                        


    elif var.response == 'move':#sets the move action
        print(var.roomOptions)
        var.response = input('What direction would you like to move? ')
        if var.response in ['left', 'right', 'forward']:
            func.makeRoom(var.diffScalar)
            print('')
            print('you entered the next room. ')
            print('')
        
        elif var.response in ['cancel', 'back']:
            pass


    elif var.response == 'open':#sets the open action
        # for x in var.chests:
        #     if x == 'door':
        #         print('')
        #         print('You see a mysterious door ahead,')
        #         var.response = input('What do you do? ')

        var.response = input('What would you like to open? ')

        if var.response == 'chest':
            print(f'There are {len(var.chests)} chests nearby. ')
            var.response = input('Which chest do you wish to open? ')
            if int(var.response) == 1 or 2 or 3:
                # print(var.chests[int(var.response) - 1])
                func.open('chest', var.chests[int(var.response) - 1])
            else:
                print('Invalid')
                var.response = input('Which chest do you wish to open')

        elif var.response == 'door':
            func.theStalkerEncounter()
                
        elif var.response in ['cancel', 'back']:
            pass


    elif var.response == 'drop':
        var.response = input('What do you want to drop? ')

        if var.response in ['cancel', 'back']:
            pass

        for x in ent.inventory.contents:
            if var.response == x.name:
                func.drop(x)
        
    
    elif var.response == 'set':
        var.response = input('What do you want to set? ')

        if var.response == 'items':
            var.response = input('What item? ')
            for x in ent.loot:
                for y in x:
                    if var.response == y.name:
                        var.nearbyItems.append(y)
                        print('')
                        print('Item', y, 'added')
                        print('')

        elif var.response == 'enemies':
            var.response = input('Which enemy? ')
            count = int(input('How many? '))
            for x in ent.enemies:
                if var.response == x.name:
                    i = 0
                    while i < count:
                        var.nearbyEnemies.append(x)
                        print(x, 'summoned')
                        i += 1

        elif var.response == 'chest':
            var.response = input('What loot should be in the chest?')
            if var.response == 'basic':
                func.makeChest(ent.basicLoot, 1)

        elif var.response in ['cancel', 'back']:
            pass
                    

    elif var.response == 'check':

        var.response = input('What do you  want to check? ')

        if var.response == 'loot gen':
            print(func.getLoot(ent.basicLoot))

        elif var.response == 'chest gen':
            func.makeChest(ent.basicLoot, 1)
            print(var.chests)

        elif var.response == 'inventory':
            func.inventoryCheck()

        elif var.response == 'item':
            var.response = input('Which item do you wish to check? ')

            func.itemCheck(var.response)


    elif var.response == 'bestiary':
        var.response = input('What creature do you hope to know? ')

        func.bestiary(var.response)

    
    elif var.response == 'use':
        print(ent.inventory.contents)
        var.response = input('What item do you want to use? ')

        for x in ent.inventory.contents:
            if var.response == x.name:
                if x.damageType == 'potion':
                    if x.effectType == 'buff': 
                        if x.effect == 'healing':
                            func.heal(x.damage)


            


    if var.move == False:
        for x in var.nearbyEnemies:
            if x.trFaAtt == True:
                func.enemyMove(x)
