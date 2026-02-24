import random, item, entity, var


class map_:
    def addNode():
        structure = entity.structures[random.randint(0, len(entity.structures))]
        enemies = []
        while var.points >= 0:
            n = random.randint(0, len(entity.enemies))
            enemies.append(entity.enemies[n])
            var.points -= entity.enemies[n].pointCost
        items = []
        for x in range(0, 3):
            n = random.randint(0, len(item.items))
            items.append(item.items[n])
        return {'structure': structure, 'enemies': enemies, 'items': items}
    
    def generate(location, type, addToStart, addToEnd):
        try:
            if var.map_[location[0]][location[1]] == None:
                var.map_[location[0]][location[1]] = map_.addNode()
        except KeyError:
            if type == 'x':
                if addToStart:
                    for x in var.map_:
                        x.insert(None)
                    var.map_[location[0]][location[1]] = map_.addNode()
                elif addToEnd:
                    for x in var.map_:
                        x.append(None)
                    var.map_[location[0]][location[1]] = map_.addNode()
            elif type =='y':
                if addToStart:
                    var.map_.insert([None] * len(var.map_[1]))
                    var.map_[location[0]][location[1]] = map_.addNode()
                elif addToEnd:
                    var.map_.append([None] * len(var.map_[1]))
                    var.map_[location[0]][location[1]] = map_.addNode()

    def construct(location):
        return var.map_[location[0]][location[1]]



class player:
    def generate():
        entity.player.species = entity.races[random.randint(0, len(entity.races))]
        entity.player.stats = {
            'str': random.randint(entity.player.species.statPackage[0][0], entity.player.species.statPackage[0][1]),
            'dex': random.randint(entity.player.species.statPackage[1][0], entity.player.species.statPackage[1][1]), 
            'con': random.randint(entity.player.species.statPackage[2][0], entity.player.species.statPackage[2][1]), 
            'int': random.randint(entity.player.species.statPackage[3][0], entity.player.species.statPackage[3][1]), 
            'wis': random.randint(entity.player.species.statPackage[4][0], entity.player.species.statPackage[4][1]), 
            'cha': random.randint(entity.player.species.statPackage[5][0], entity.player.species.statPackage[5][1])
        }
        entity.player.health = 7 * entity.player.stats['con']
    
    def move(x, y):
        if x == -1:
            entity.player.xpos -= 1
            map_.generate([entity.player.xpos, entity.player.ypos], 'x', addToStart = True)
        elif x == 1:
            entity.player.xpos += 1
            map_.generate([entity.player.xpos, entity.player.ypos], 'x', addToEnd = True)
        if entity.player.xpos < 0:
            entity.player.xpos = 0

        if y == -1:
            entity.player.ypos -= 1
            map_.generate([entity.player.xpos, entity.player.ypos], 'y', addToStart = True)
        elif y == 1:
            entity.player.ypos += 1
            map_.generate([entity.player.xpos, entity.player.ypos], 'y', addToEnd = True)
        if entity.player.ypos < 0:
            entity.player.ypos = 0

        var.currentArea = map_.construct([entity.player.xpos, entity.player.ypos])