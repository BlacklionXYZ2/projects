
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