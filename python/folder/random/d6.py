import random

f = True
nums = ['1', '2', '3', '4', '5', '6']

while f == True:
    response = input('Do you wish to roll? ')

    if response == 'yes':

        roll = random.randint(1, 6)
        print(roll)

    elif response in nums:
        
        print(response)