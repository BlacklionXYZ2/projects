# takes a given number and converts it into a given base
responseInt, responseBase = int(input()), int(input())
length = 0
text = 'a'
while responseInt >= 0:
    
    power = 1
    while responseInt <= (responseBase ** power):
        power += 1

    if responseInt <= responseBase:
        text += str(responseInt)
        responseInt = 0
    elif responseInt > responseBase:
        responseInt -= responseBase ** (power - 1)
        text += str(responseBase)

print(text[1:])