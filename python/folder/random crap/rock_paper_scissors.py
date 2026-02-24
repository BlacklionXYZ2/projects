import random

def winCheck(num1, user):
    if num1 == 1 and user == 1:
        print('Draw')
    elif num1 == 1 and user == 2:
        print('You win')
    elif num1 == 1 and user == 3:
        print('You lose')
    elif num1 == 2 and user == 1:
        print('You lose')
    elif num1 == 2 and user == 2:
        print('Draw')
    elif num1 == 2 and user == 3:
        print('You win')
    elif num1 == 3 and user == 1:
        print('You win')
    elif num1 == 3 and user == 2:
        print('You lose')
    elif num1 == 3 and user == 3:
        print('Draw')
    elif user > 3 or user < 1 or user == None:
        print('Invalid answer, try again')


game = False
while game == False:
    response = input('do you wish to start? ')
    if response == 'yes':
        game = True

while game == True:
    cpu = random.randint(1, 3)
    response = int(input('''
1 = rock
2 = paper
3 = scissors
'''))
    winCheck(cpu, response)