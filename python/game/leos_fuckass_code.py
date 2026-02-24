import random


class Main:
    game = True
    notInCombat = True
    xpos = 0
    ypos = 0
    move = ['up','right','left','down']
    races = ['human', 'elf', 'half-elf', 'changeling', 'tiefling']
    structures = ['e','chest','room','tree','grassland','pond','field']
    map_ = [['spawn']]
    weaponstwo = ['sword','dagger','halberd','zweihandler','fat man','glaive','long sword','battle axe']
    weapons = { #name: damage value
        'sword':3,
        'dagger':1,
        'halberd':6,
        'zweihandler':10,
        'fat man':999999,
        'glaive':6,
        'long sword':6,
        'battle axe':3
    }
    foodtwo = ['apple','bread','golden banana','fish','blue stuff','funnny mushroom','orange','fresh cups of warm tea']
    food = { #name: healing value
        'apple':6,
        'bread':10,
        'golden banana':30,
        'fish':3,
        'blue stuff':69,
        'funny mushrooms':-1,
        'orange':6,
        'fresh cups of warm tea':999999999
    }
    player = {
        'race': races[random.randint(0, len(races) - 1)],
        'str': random.randint(1, 20),
        'con': random.randint(1, 20),
        'dex': random.randint(1, 20),
        'int': random.randint(1, 20),
        'wis': random.randint(1, 20),
        'chr': random.randint(1, 20),
        'health': random.randint(1, 100),
        'inventory': []
    }
currantMonster = {
    'race':0,
    'str':0,
    'con':0,
    'dex':0,
    'int':0,
    'wis':0,
    'chr':0,
    'health':0
}

class move:
    def left():
        for x in range(0,len(Main.map_)):
            Main.map_[x].insert(0,Main.structures[random.randrange(0, len(Main.structures))])
        Main.xpos -= 1

    def right():
        for x in range(0,len(Main.map_)):
            Main.map_[x].append(Main.structures[random.randrange(0, len(Main.structures))])
        Main.xpos += 1

    def down():
        ref = []
        for x in Main.map_[0]:
            ref.append(Main.structures[random.randrange(0, len(Main.structures))])
        Main.map_.append(ref)
        Main.ypos += 1

    def up():
        ref = []
        for x in Main.map_[0]:
            ref.append(Main.structures[random.randrange(0, len(Main.structures))])
        Main.map_.insert(0,ref)
        Main.ypos -= 1

def gen_monster():
    monster = {
        'race': Main.races[random.randint(0, len(Main.races) - 1)],
        'str': random.randint(0, 20),
        'con': random.randint(0, 20),
        'dex': random.randint(0, 20),
        'int': random.randint(0, 20),
        'wis': random.randint(0, 20),
        'chr': random.randint(0, 20),
        'health':random.randint(0,100)
    }
    return monster
def start():
    print(f'your stats are {Main.player}')
    if Main.player['race'] == 'changeling':
        Main.player['dex'] += 3
        Main.player['chr'] -= 2
    elif Main.player['race'] == 'tiefling':
        Main.player['str'] += 3
        Main.player['chr'] -= 2
    elif Main.player['race'] == 'elf':
        Main.player['dex'] += 4
        Main.player['str'] -= 2
    elif Main.player['race'] == 'half-elf':
        Main.player['dex'] += 2
        Main.player['str'] -= 1

def monster_turn():
    if currantMonster['health'] in range(5,10):
        currantMonster['health'] += currantMonster['con']-10
    save = currantMonster['str'] - 10
    if random.randint(0, 20) + save >= Main.player['con']:
        Main.player['health'] -= currantMonster['str']
        print(f'{currantMonster["race"]} hits you for {currantMonster["str"]} you have {Main.player["health"]}')

def combat_check():
    global currantMonster
    meet_monster = random.randint(1, 20) + Main.player['dex']
    if meet_monster < 25 and Main.notInCombat == True:
        currantMonster = gen_monster()
        print(f'you encounter a {currantMonster["race"]}')
        Main.notInCombat = False
    elif currantMonster['health'] <= 0:
        Main.notInCombat = True

def turn(command):
    #move commands
    if command == 'up' and Main.notInCombat:
        move.up()
    elif command == 'down' and Main.notInCombat:
        move.down()
    elif command == 'right' and Main.notInCombat:
        move.right()
    elif command == 'left' and Main.notInCombat:
        move.left()
    #stats command
    elif command == 'stats':
        print(Main.player)

    #combat commands
    elif command == 'attack' and not Main.notInCombat:
        save = Main.player['str']-10


        if random.randint(0,20)+save >= currantMonster['con']:
            currantMonster['health'] -= Main.player['str']
            print(f'you hit it for {Main.player["str"]} dmg it has {currantMonster["health"]} left')
            monster_turn()
        else:
            print('you miss')
            monster_turn()


    elif command == 'speak' and not Main.notInCombat:
        input('what do you say > > > ')
        save = Main.player['chr']-10
        if random.randint(0,20)+save >= currantMonster['chr']:
            Main.notInCombat = True
            print(f'the {currantMonster["race"]} has let you off and he even offers to heal you')
            Main.player['health'] += 20
        else:
            monster_turn()


    elif command == 'cmd':
        response = input('cmd > > > ')
        if response in Main.player:
            by_how_much = int(input('by how much > > > '))
            Main.player[response] += by_how_much

        elif response == 'give':
            print(Main.weapons)
            item_to_be_given = input('what items would you like > > > ')
            if item_to_be_given in Main.weapons:
                Main.player['inventory'].append(item_to_be_given)
                print(f'here is a {item_to_be_given}',Main.player['inventory'])

        elif response == 'pos':
            print(Main.ypos)
            print(Main.xpos)

        elif response == 'map':
            print(Main.map_)

    elif command == 'attack with weapon' and not Main.notInCombat:
        print(Main.player['inventory'])
        weapon_used = input('what is the weapon used > > > ')

        if weapon_used in Main.player['inventory']:
            save = Main.player['str'] - 10 +Main.weapons[weapon_used]
            if random.randint(0, 20) + save >= currantMonster['con']:
                currantMonster['health'] -= Main.player['str']+Main.weapons[weapon_used]
                print(f'you hit it for {Main.player["str"]+Main.weapons[weapon_used]} dmg it has {currantMonster["health"]} left')
            else:
                print('you miss')
                monster_turn()

        if weapon_used == 'fat man':
            Main.player['inventory'].remove('fat man')


    elif command == 'open' and Main.map_[Main.ypos][Main.xpos] == 'chest':
        weapon_roll = random.randint(0,len(Main.weaponstwo)-1)
        Main.player['inventory'].append(Main.weaponstwo[weapon_roll])
        rand_counter = random.randint(1,10)
        food_random = Main.foodtwo[random.randint(0, len(Main.foodtwo) - 1)]
        for x in range(0,rand_counter):
            Main.player['inventory'].append(food_random)
        print(f'you find {rand_counter} {food_random} and a {Main.weaponstwo[weapon_roll]}')
        Main.map_[Main.ypos][Main.xpos] = 'e'


    elif command == 'eat':
        print(Main.player['inventory'])
        item = input('which one > > > ')
        if item in Main.player['inventory'] and item in Main.foodtwo:
            Main.player['health'] += Main.food[item]
            Main.player['inventory'].remove(item)

start()

while Main.game:
    if Main.notInCombat:
        print('not in combat')

    if Main.player['health'] <= 0:
        Main.game = False

    if not Main.notInCombat:
        print('combat active')

    turn(input('what doing > > > '))
    #Main turn
    print(f'you are at {Main.map_[Main.ypos][Main.xpos]}')
    #monster check and spawning
    combat_check()