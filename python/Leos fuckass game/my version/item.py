class food: #name: healing value
        complete = [None, 'apple', 'bread', 'golden_banana', 'fish', 'blue_stuff', 'mushrooms', 'orange', 'warm_tea']
        apple = 6
        bread = 10
        golden_banana = 30
        fish = 3
        blue_stuff = 69
        mushrooms = -1
        orange = 6
        warm_tea = 999999999
        
class weapons: #name: damage value
        complete = [None, 'sword', 'dagger', 'halberd', 'zweihandler', 'fat_man', 'glaive', 'longsword', 'battleaxe']
        sword = 3
        dagger = 1
        halberd = 6
        zweihandler = 10
        fat_man = 999999
        glaive = 6
        longsword = 6
        battleaxe = 3
        bow = 2 

items = food.complete + weapons.complete
items = [x for x in items if x != None]