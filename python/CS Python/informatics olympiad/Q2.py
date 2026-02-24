print('Oscar Hunt Brown, Ashby School')
from math import ceil

alph = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']

def error(error):
    return 0

response = (input()).split()
config = {'n': int(int(response[0]) if int(response[0]) >= 5 and int(response[0]) <= 26 else error('n')), 's': int(int(response[1]) if int(response[1]) >= 0 and int(response[1]) <= 5000 else error('s')), 'c': int(int(response[2]) if int(response[2]) >= 0 and int(response[2]) <= 51 else error('c')), 'encrypt': response[3] if len(response[3]) <= 10 else error('encrypt')}
n = config['n']
s = config['s']
c = config['c']
encrypt = config['encrypt']

class deck:
    def __init__(self, size):
        self.cards = alph[:size]


alphadeck = deck(n)
betadeck = deck(n)

combineddeck = deck(0)
combineddeck.cards = []
for x in range(len(alphadeck.cards)):
    combineddeck.cards.append(alphadeck.cards[x])
    combineddeck.cards.append(betadeck.cards[x])
alphadeck.cards = []
betadeck.cards = []

for x in range(s):                                          # steps 2-4 repeated s times
    split_point = int(len(combineddeck.cards) / 2)
    alphadeck.cards = combineddeck.cards[:split_point]
    betadeck.cards = combineddeck.cards[split_point:]
    combineddeck.cards = []

    for y in range(len(alphadeck.cards)):
        combineddeck.cards.append(betadeck.cards[y])
        combineddeck.cards.append(alphadeck.cards[y])

    for y in range(c):                                       # c cards moved from the top to the bottom of the deck
        combineddeck.cards.append(combineddeck.cards[0])
        combineddeck.cards.pop(0)

for x in combineddeck.cards:                                 #split the decks
    if x not in alphadeck.cards:
        alphadeck.cards.append(x)
    else:
        betadeck.cards.append(x)


def encrypt_str():
    global encrypt, betadeck, alphadeck
    output = 'a'
    for x in encrypt:
        for card in range(len(alphadeck.cards)):
            if x == alphadeck.cards[0]:
                output += betadeck.cards[0]
                break
            else:
                alphadeck.cards.append(alphadeck.cards[0])
                alphadeck.cards.pop(0)
                betadeck.cards.append(betadeck.cards[0])
                betadeck.cards.pop(0)
        split_point = ceil(len(alphadeck.cards) / 2)
        tempdeck = alphadeck.cards[:split_point]
        tempdeck.append(tempdeck[2])
        tempdeck.pop(2)
        tempdeck.extend(alphadeck.cards[split_point:])
        alphadeck.cards = tempdeck
        tempdeck = betadeck.cards[:split_point]
        tempdeck.append(tempdeck[1])
        tempdeck.pop(1)
        tempdeck.extend(betadeck.cards[split_point:])
        betadeck.cards = tempdeck

    return output[1:]

print(encrypt_str())