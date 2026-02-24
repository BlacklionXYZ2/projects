
start = True
name = None
score = None
score2 = None
name2 = None
while start == True:
    if name != 'stop' or score != 'stop':
        name = input('What is the name of your team? ')
        score = input('What is the score of your team? ')    
        if int(score) > int(score2):
            name2 = name
            score2 = score
    print(name2, score2)
            
