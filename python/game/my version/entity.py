class player:
    xpos = 0
    ypos = 0
    inventory = []
    species = None
    stats = None
    health = 1


structures = ['e','room','tree','grassland','pond','field']

class human:
    statPackage = [[8, 20]] * 6

class elf:
    statPackage = [[1, 10], [8, 20], [1, 20], [10, 20], [10, 20], [1, 20]]

class half_elf:
    statPackage = [[1, 16], [4, 16], [1, 20], [5, 16], [5, 16], [1, 20]]

class changeling:
    statPackage = [[1, 10], [10, 20], [1, 20], [5, 18], [1, 16], [10, 20]]

class tiefling:
    statPackage = [[10, 20], [5, 16], [10, 20], [1, 20], [1, 14], [1, 10]]

races = [human, elf, half_elf, changeling, tiefling]

class skeleton:
    health = 5
    weapon = 'bow'
    pointCost = 2

class zombie:
    health = 7
    weapon = 'sword'
    pointCost = 3

enemies = [skeleton, zombie]