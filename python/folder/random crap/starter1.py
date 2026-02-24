game = False
mult = 2 

while game == False:

    response = input('do you wish to start? ')

    if response == 'yes':
        game = True


while game == True:
    res = int(input('Pick a number '))

    if res != 0:
        num = res * mult
        print(num)
        print('')

    elif res == 0:
        game = False
        print('Program has ended.')

    else:
        print('invalid response ')
        print('')